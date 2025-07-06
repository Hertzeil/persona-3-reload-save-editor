# Persona3 Reload | Save Editor

![Python3](https://img.shields.io/badge/python-3.10-blue?logo=python)

> Tool to edit savefiles for Persona 3 Reload \
Edit your save file with relative ease : change money, names, characters stats, playtime, social rank and world position...

> **DISCLAIMER :** I don't know Python. I may messed up heavily the tool's original source code as I nearly rewrite it entirely. \
Use this tool at your own risk, I'll offer no support (but feel free to submit pull request). 

## Usage
```shell
$> python3 main.py Yoursavefile.sav
Type help to see usages
P3REditor> 
```

1. Copy your save file in the folder next to the main.py file \
2. Launch console command as mentioned earlier \
3. Type what you want in the prompt, everything is said in it (or type `help` to get more instructions)

I don't port the automatic get/set methods yet. Use read/write command instead, seek for IDs in the `P3REditor/p3rpaddings.py` file. \
I might rewrite the original get/set methods... One day.

## Notices
### Backup your files !
Even this tool make some backup files, always keep a copy at safe location ! This tool may softlock your save. \
This script no longer erase original file (the one you put in root folder), instead it writes a new file in the `generated` subfolder.

### Saves ID
The original developer mentioned that the ids had changed during a game update. \
I added an attempt to automatically handle this offset in the code based on my own copy of the game (steam version, build id 17964130). \
Experience may vary, as usual... **MAKE BACKUP !**

### Platform compatibility
Original dev assume this tool could work with MS Store/PS4 version (but not tested). \
In these case, you may have to decrypt yourselves the save file with [this method for PS4 version](https://www.youtube.com/watch?v=QA1lLxn_klA). \
As I only got a steam version, I can't test on these and I'll not give support for any other version.

### Characters stats limitation
Original version of this tool give support for MC/Yukari/Junpei. \
I added the IDs for Akihiko but I will add the IDs of the other NPCs as I progress through the game (I've only unlocked Akihiko ATM).

### Make backups !
Did I tell you to back up your files? ***Do it, now!***

## Credits
* https://github.com/afkaf/Python-GVAS-JSON-Converter
* https://github.com/RealDarkCraft/persona-3-reload-save-editor