# alias-installer
## This is the repo for my Python-based Bash alias installer!
### Requirements
- Python 3.x
- Bash Shell

---
### How do I use it?
The way it works is simple, You download the script, named AliasInstaller.py, and create a file called *.com_alias, The script, when run, via double-clicking or through `python AliasInstaller.py`, will scan your home directory **non-recursively**, for these files, so make sure before making an issue, that you do in fact have them in the home directory, and edit the .bashrc file in your home directory, and add the alias defined in the *.com_alias file

### Syntax
For syntax examples see [this file](https://github.com/KirbyJeff/alias-installer/tree/main/ex/example.com_alias).
- Any empty lines are counted as separators to allow adding multiple aliases in one file.
- ALIAS_NAME is the name used in the terminal
- ALIAS_FOR is the command to be called when using the alias.
- ALIAS_GLOBAL is a boolean (true/false) value that determines whether the alias is a global alias.

### Feedback is welcome!
Feel free to DM me on [reddit](https://www.reddit.com/u/KirbyJeef) if you would like to share your .com_alias files and have them added to this repo.
- Also, aas of right now, the is no way to check for conflicting aliases, so you are advised to check your current aliases to make sure nothing conflicts.
