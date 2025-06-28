# Persona3 Reload | Save Editor
![Python3](https://img.shields.io/badge/python-3.10-blue?logo=python)
> Tool to edit savefiles for Persona 3 Reload \
Edit your save file with relative ease : change money, names, characters stats, playtime, social rank and world position...

## Usage
```shell
$> python3 main.py Yoursavefile.sav
```

Copy your save file in the folder next to the main.py file \
Launch console command as mentioned earlier \
Type what you want in the prompt, everything is said in it (or type `help` to get more instructions)

## Notices
### Saves ID
Original dev said the game have changed the internal IDs, so use this tool with caution. \
You should add +4 on IDs to fix this issue

### Platform compatibility
Original dev assume this tool could work with MS Store/PS4 version (but not tested) \
In these case, you may have to decrypt yourselves the save file with [this method for PS4 version](https://www.youtube.com/watch?v=QA1lLxn_klA)

### Characters stats limitation
You only can change values for PC/Yukari/Junpei 

### Backup your files !
Even this tool make some backup files, always keep a copy at safe location ! This tool can softlock your save.
If you want to recover your file by default when saving the program backup the file to : {original-file-path}/backup/{timestamp}_{filename}.sav


## Credits
* https://github.com/afkaf/Python-GVAS-JSON-Converter
* https://github.com/RealDarkCraft/persona-3-reload-save-editor