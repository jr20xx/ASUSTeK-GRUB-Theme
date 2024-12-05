## ASUSTeK GRUB Theme

### Table of Contents
- [Disclaimer](#disclaimer)
- [Usage](#usage)
- [Contribution](#contribution)

## Disclaimer

The pieces for this theme were put together by me, using some free resources I found on the Internet, with the purpose of creating a nice [GRUB](https://en.wikipedia.org/wiki/GNU_GRUB) theme for the laptop where I currently do all my work. The original image used for the background can be found in [this website](https://wallhere.com/en/wallpaper/1510751) and the template and fonts I used for the theme can be found in [this GitHub repository](https://github.com/vinceliuice/grub2-themes).

I have no relation with [ASUSTeK Computer Inc.](https://www.asus.com/), its partners or any of the projects I mentioned above. All the information and logos found inside this project are property of their respective owners; with exception of the few ones created by me.

## Usage

First, clone this repo by opening a terminal and executing the following command:
```bash
git clone https://github.com/jr20xx/ASUSTeK-GRUB-Theme
```
Once you've successfuly cloned this repo, copy the `asus` directory to `/boot/grub/themes`. Please notice that the destination is a system protected directory and you may need to get root permission to copy files in it. If you want, you can do it all from a terminal by executing:
```bash
sudo cp -rv asus /boot/grub/themes
```
After copying the theme, you have to setup GRUB to make use of it. You might need to read the docs of your distro to perform this step, but the location of the configuration file in most distros is `/etc/default/grub`. Open that file with your prefered text editor and then locate the following texts:
- **GRUB_GFXMODE**
- **GRUB_BACKGROUND**
- **GRUB_THEME**

In case any of those texts is located in a line starting with a **#** symbol, remove the **#** symbol before doing any change or, if those texts can't be found, add them. Here's what needs to be written and saved inside of the configuration file of GRUB:
```
GRUB_GFXMODE=auto
GRUB_BACKGROUND="/boot/grub/themes/asus/background.png"
GRUB_THEME="/boot/grub/themes/asus/theme.txt"
```

> [!WARNING]
>- Please make sure to **make a backup** of your original configuration file to ease the process of rolling back your changes.
>- **DO NOT** remove all the content of that file and then just leave only those three lines inside all by themselves under any concept or you may break the GRUB configuration. The remaining texts in the file need to remain untouched, unless you know what you are doing.

After doing those three changes, you have to rebuild the GRUB configuration. Once again, you might need to read the docs of your distro to perform this step, but taking [Arch Linux](https://archlinux.org/) as example, the command needed to perform this operation is the following:
```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```
After updating the GRUB configuration, just reboot and then you should see this theme in action.

## Contribution

Any kind of contribution will be really valued and we encourage you to submit pull requests and to provide tutorials or other relevant content that might help to improve this project. 

You can also contribute to this repo by adding a star to it and/or sharing the link if you find it helpful in some way. Any form of help will be highly appreciated.