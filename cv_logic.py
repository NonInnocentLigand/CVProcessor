import pandas as pd
import matplotlib.pyplot as plt


class CVProcessor:
    def __init__(self):
        pass

    def get_file_path_info(self, file_path: str):
        if not file_path[-3:] == 'txt' or file_path[-3:] == 'csv':
            raise Exception('file_path must be a .txt or .csv file')
        file_directory = '/'.join(file_path.split('/')[:-1])
        file_name_with_extension = file_path.split('/')[-1]
        file_name_no_extension = file_name_with_extension[:-(file_name_with_extension[::-1].find('.') + 1)]
        return {'file_path': file_path,
                'file_directory': file_directory,
                'file_name_with_extension': file_name_with_extension,
                'file_name_no_extension': file_name_no_extension}


    def get_current_and_potential(self, file_path: str):
        with open(file_path, 'r') as txt_file:
            txt_file_list = [line.rstrip('\n') for line in txt_file]
            potential_current_list = txt_file_list[(txt_file_list.index('Potential/V, Current/A')+2):]  # +2 to move past blank line in txt file
            potential_current_dic = {}
            potential_current_dic['Potential/V'] = list(map(lambda x: float(x.split(',')[0]), potential_current_list))
            potential_current_dic['Current/A'] = list(map(lambda x: float(x.split(',')[1]), potential_current_list))
            df = pd.DataFrame.from_dict(potential_current_dic)
            return df


    def plot_cv(self, file_path: str, save_plot=False, image_filepath=''):
        df = self.get_current_and_potential(file_path)
        file_name = self.get_file_path_info(file_path)
        fig, axs = plt.subplots(layout='constrained')
        axs.plot(df['Potential/V'].to_numpy(), df['Current/A'].to_numpy())
        axs.invert_xaxis()
        axs.set_title(file_name['file_name_no_extension'])
        if save_plot:
            plt.savefig(image_filepath)
        plt.show()


    def plot_cv_stacked(self, df_list: list, df_names: list, save_plot=False, image_filepath=''):
        number_of_plots = len(df_list)
        fig, axs = plt.subplots(number_of_plots, 1, sharex=True, layout='constrained')
        for index in range(number_of_plots):
            df = df_list[index]
            axs[index].plot(df['Potential/V'].to_numpy(), df['Current/A'].to_numpy())
            axs[index].invert_xaxis()
            axs[index].set_ylabel('Current/A')
            axs[index].set_title(df_names[index])
        axs[number_of_plots-1].set_xlabel('Potential/V vs SCE')
        if save_plot:
            plt.savefig(image_filepath)
        plt.show()

    def plot_cv_overlay(self, df_list: list, df_names: list, plot_name: str, save_plot=False, image_filepath=''):
        fig, axs = plt.subplots(layout='constrained')
        for df in df_list:
            axs.plot(df['Potential/V'].to_numpy(), df['Current/A'].to_numpy())
        axs.set_title(plot_name)
        axs.set_ylabel('Current/A')
        axs.set_xlabel('Potential/V vs SCE')
        plt.legend(df_names)
        axs.invert_xaxis()
        if save_plot:
            plt.savefig(image_filepath)
        plt.show()


    def get_vs_fc(self, df_fc: pd.DataFrame, solvent:str):
        solvent_dictionary = {
            'THF': 0.52,
            'MECN': 0.4
        }
        if solvent.upper() in list(solvent_dictionary.keys()):
            e_half_fc_lit = solvent_dictionary[solvent.upper()]
        if solvent.upper() not in list(solvent_dictionary.keys()):
            raise Exception(f'the solvent argument provided, "{solvent}", was not in the solvent dictionary,'
                  f'please select an appropriate solvent from the list:\n{list(solvent_dictionary.keys())}')
        fc_max_v = df_fc['Potential/V'].loc[df_fc['Current/A'].idxmin()]
        fc_min_v = df_fc['Potential/V'].loc[df_fc['Current/A'].idxmax()]
        e_half_fc = fc_max_v - (fc_max_v - fc_min_v) / 2
        return -(e_half_fc - e_half_fc_lit)  # gives the potential you need to shift all values by


    def cv_vs_fc(self, file_path: str, fc_file_path: str, solvent: str):
        df = self.get_current_and_potential(file_path)
        vs_fc = self.get_vs_fc(self.get_current_and_potential(fc_file_path), solvent)
        df_copy = df.copy()
        df_copy['Potential/V'] = df['Potential/V'] + vs_fc
        return df_copy


    def cv_minus_blank(self, df_file: pd.DataFrame, df_blank: pd.DataFrame):
        df_file_copy = df_file.copy()
        df_file_copy['Current/A'] = df_file['Current/A'] - df_blank['Current/A']
        return df_file_copy


    def cv_blank_fc_corrected(self, file_path: str, fc_file_path: str, solvent: str, blank_file_path: str):
        df_vs_fc = self.cv_vs_fc(file_path, fc_file_path, solvent)
        df_blank_vs_fc = self.cv_vs_fc(blank_file_path, fc_file_path, solvent)
        df_blank_and_fc_corrected = self.cv_minus_blank(df_vs_fc, df_blank_vs_fc)
        return df_blank_and_fc_corrected



