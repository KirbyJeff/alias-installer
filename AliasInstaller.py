import os
import glob

def add_aliases_to_bashrc():
    home_dir = os.path.expanduser("~")
    bashrc_path = os.path.join(home_dir, ".bashrc")
    alias_files = glob.glob(os.path.join(home_dir, "*.com_alias"))

    with open(bashrc_path, "a") as bashrc:
        for alias_file in alias_files:
            with open(alias_file, "r") as file:
                alias_name = ""
                alias_for = ""
                alias_global = False

                for line in file:
                    line = line.strip()
                    if not line:
                        if alias_name and alias_for:
                            if alias_global:
                                bashrc.write(f"alias -g {alias_name}='{alias_for}'\n")
                            else:
                                bashrc.write(f"alias {alias_name}='{alias_for}'\n")
                            alias_name = ""
                            alias_for = ""
                            alias_global = False
                        continue

                    if line.startswith("ALIAS_NAME="):
                        alias_name = line.split("=")[1].strip().strip('"')
                    elif line.startswith("ALIAS_FOR="):
                        alias_for = line.split("=")[1].strip().strip('"')
                    elif line.startswith("ALIAS_GLOBAL="):
                        alias_global = line.split("=")[1].strip().strip('"').lower() == "true"

                # Write the last alias if the file does not end with an empty line
                if alias_name and alias_for:
                    if alias_global:
                        bashrc.write(f"alias -g {alias_name}='{alias_for}'\n")
                    else:
                        bashrc.write(f"alias {alias_name}='{alias_for}'\n")

if __name__ == "__main__":
    add_aliases_to_bashrc()