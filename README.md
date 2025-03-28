# Cyclic Voltammetry (CV)

---

I wrote these scripts to process the data from cyclic voltammetry experiments I ran as a PhD student. Sure beats the cutting and pasting from excel ...not that'd I'd ever admit to having done that...

---

## The general workflow

After data collection, some additional processing is needed to make plots of the voltammograms and analyze the data. The scripts help with the following:

1. Clean up the .txt files from the instrument and write a .csv file
2. Determine the half wave potential (E<sub>1/2</sub>), the midpoint between the cathodic (E<sub>pc</sub>) and anodic (E<sub>pa</sub>) peak potentials, of the reference molecule (Ferrocene in this example)
3. Reference the potentials for the measurements of the molecule of interist to that of the reference molecule and reference electrode
4. Background subtraction of the baseline current

---

### Example outputs

Overlays of all plots from step 1.

Overlay of the reference molecule before and after correcting

Overlay of subject molecule before and after referencing vs the reference molecule

Overlay of the background and subject molecule

overlay of the background molecule following subtraction of the baseline current

---
### Notes

Feel free to modify this code to clean up your own voltammograms :)
