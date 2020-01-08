# tidalhelper

## about
tidalhelper is a command line utility for automatically organizing large collections of audio samples into folders for use with tidalcycles.

## installation/usage
* make sure that the samples you want to organize are all in one folder, and begin with a logical prefix separated by an underscore, e.g. `guitar_1.wav`
* install python3
* open a terminal and run `git clone https://github.com/isaacpearl/tidal-helper`
* run `cd tidal-helper` to navigate to the project folder
* run `python3 tidalhelper.py <targetdirectory>`, replacing `<targetdirectory>` with the full path to the directory containing samples you want to organize. Make sure to include a `/` on the end of this filepath :)
* there will be a new folder inside your `<targetdirectory>` called 
`tidal_samples/` with populated directories, named for each sample prefix.
* move `tidal_samples/` to wherever you keep your tidalcycles samples
* ♫♫♫♫♫♫♫♫

## roadmap
* arbitrary filenames as input (no underscores required)
* distribute package with `pip`
* output guide to new folders (`.txt` or print) and their contents
* design specific sample naming convention including category/key/bpm, and add reorganization functionality (e.g. being able to reorganize folder structure based on sample group, key, bpm with flags - no sample renaming needed)
* gui
* smart categorization/folder naming (ml? audio analysis?)
