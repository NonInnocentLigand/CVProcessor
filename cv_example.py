from cv_logic import CVProcessor


path_info = {
    'sample_file_path': 'CVProcessor/Example Data/Sample.txt',
    'fc_file_path': 'CVProcessor/Example Data/FC.txt',
    'blank_file_path': 'CVProcessor/Example Data/Blank.txt',
}

Processor = CVProcessor()

df_list_plot = [
    Processor.get_current_and_potential(path_info['sample_file_path']),
    Processor.get_current_and_potential(path_info['fc_file_path']),
    Processor.get_current_and_potential(path_info['blank_file_path']),
]

df_names = [
    'sample',
    'fc',
    'blank',
]

sample_df = Processor.get_current_and_potential(path_info['sample_file_path'])
sample_df_vs_fc = Processor.cv_vs_fc(path_info['sample_file_path'], path_info['fc_file_path'], 'THF')
sample_df_vs_fc_background = Processor.cv_blank_fc_corrected(path_info['sample_file_path'], path_info['fc_file_path'], 'THF', path_info['blank_file_path'])

fc_df = Processor.get_current_and_potential(path_info['fc_file_path'])
fc_df_vs_fc = Processor.cv_vs_fc(path_info['fc_file_path'], path_info['fc_file_path'], 'THF')

blank_df = Processor.get_current_and_potential(path_info['blank_file_path'])
blank_df_vs_fc = Processor.cv_vs_fc(path_info['blank_file_path'], path_info['fc_file_path'], 'THF')

image_filepath_1 = '/Users/leoparsons/Desktop/Coding_Projects/Python_Projecs/Cyclic_Voltammetry_v2/example_1.png'
image_filepath_1a = '/Users/leoparsons/Desktop/Coding_Projects/Python_Projecs/Cyclic_Voltammetry_v2/example_1a.png'
image_filepath_2 = '/Users/leoparsons/Desktop/Coding_Projects/Python_Projecs/Cyclic_Voltammetry_v2/example_2.png'
image_filepath_2a = '/Users/leoparsons/Desktop/Coding_Projects/Python_Projecs/Cyclic_Voltammetry_v2/example_2a.png'
image_filepath_3 = '/Users/leoparsons/Desktop/Coding_Projects/Python_Projecs/Cyclic_Voltammetry_v2/example_3.png'


## call these methods to generate the figures shown in the README.md file
# Processor.plot_cv_overlay(df_list_plot, df_names, 'Overlay', save_plot=True, image_filepath=image_filepath_1)
# Processor.plot_cv_stacked(df_list_plot, df_names=df_names, save_plot=True, image_filepath=image_filepath_1a)
# Processor.plot_cv_overlay([sample_df, sample_df_vs_fc], ['sample', 'sample_vs_fc'], 'Overlay', save_plot=True, image_filepath=image_filepath_2)
# Processor.plot_cv_overlay([fc_df, fc_df_vs_fc], ['fc', 'fc_vs_fc'], 'Overlay', save_plot=True, image_filepath=image_filepath_2a)
# Processor.plot_cv_overlay([sample_df_vs_fc, blank_df_vs_fc], ['sample_vs_fc', 'blank_vs_fc'], 'Overlay', save_plot=True, image_filepath=image_filepath_3)

