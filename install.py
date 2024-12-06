import os, shutil

RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"; BLUE = "\033[94m"; LIGHT_BLUE="\033[96m"; MAGENTA = '\033[95m'; RESET = "\033[0m"
GRUB_THEMES_FOLDER = "/boot/grub/themes"
GRUB_CONFIGURATION_FILE = "/etc/default/grub"
GRUB_CONFIGURATION_BACKUP_FILE = os.path.expanduser('~') + "/grubcfg_backup"

if(os.geteuid() != 0):
    print(RED + "\033[1mERROR:\033[0m" + RED + " You need to execute this script as root!")
    exit(1)

if input(LIGHT_BLUE + "This script was created to automate the process of setting the ASUSTeK GRUB Theme as the current theme for GRUB. Once it's all done, the ASUSTeK theme will be the default theme for GRUB. Are you sure to continue? (Y/n): " + RESET).lower() == 'n':
    print(GREEN + "Execution successfuly canceled!")
    exit(0)

os.makedirs(GRUB_THEMES_FOLDER, exist_ok=True)
print(YELLOW + "Copying the theme folder to " + GRUB_THEMES_FOLDER)
destination_folder = os.path.join(GRUB_THEMES_FOLDER, "asus")
if os.path.exists(destination_folder):
    print(YELLOW + "Removing old theme folder to avoid file conflicts..")
    shutil.rmtree(destination_folder)
shutil.copytree("asus", destination_folder)
print(GREEN + "Theme folder successfuly copied!")

print(YELLOW + "Backing up old GRUB configuration file...")
shutil.copy(GRUB_CONFIGURATION_FILE, GRUB_CONFIGURATION_BACKUP_FILE)
print(GREEN + "Backup file successfuly created at", GRUB_CONFIGURATION_BACKUP_FILE)

print(YELLOW + "Opening GRUB configuration file...")
with open(GRUB_CONFIGURATION_FILE, "r") as file: original_text = file.readlines()
print(YELLOW + "Generating new configuration...")
filtered_lines = [line for line in original_text if not any(excluded in line for excluded in ['GRUB_GFXMODE', 'GRUB_BACKGROUND', 'GRUB_THEME'])]
filtered_lines.append("""GRUB_GFXMODE=auto
GRUB_BACKGROUND="/boot/grub/themes/asus/background.png"
GRUB_THEME="/boot/grub/themes/asus/theme.txt\"""")

print(YELLOW + "Saving new configuration...")
with open(GRUB_CONFIGURATION_FILE, "w") as file: file.writelines(filtered_lines)
print(GREEN + "New configuration file saved at", GRUB_CONFIGURATION_FILE)

if input("""
\u001b[95m\033[1mWARNING:\033[0m
\u001b[95mDo you wanna execute the default command and try to update GRUB configuration now? (Y/n): \u001b[0m""").lower() == 'n':
    print("""
\u001b[94mExiting now...
\u001b[93m\033[1mRemember to update the GRUB configuration to see the theme in action!\033[0m
\033[96mBye ;)
""")
    exit(0)

print(YELLOW + "Updating GRUB configuration..." + RESET)
if os.system("grub-mkconfig -o /boot/grub/grub.cfg") == 0:
    print(GREEN + "\nGRUB configuration was completed with no errors")
else:
    print(RED + "\n\033[1mERROR:\033[0m" + RED + "Something went wrong while trying to configure GRUB. Please, check the docs of your distro, see if there's a different command there to update GRUB configuration and run it later")

print(f"""
{LIGHT_BLUE}\033[1mMESSAGE:\033[0m
{LIGHT_BLUE}- The execution of the script was fully completed.
- A backup of the previous configuration file was stored at {GRUB_CONFIGURATION_BACKUP_FILE}.
- You should see the ASUSTeK GRUB Theme next time you boot.
""")