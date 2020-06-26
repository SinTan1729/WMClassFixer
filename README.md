
# Info

Some applications (e.g. firefox-trunk) don't have proper desktop files. Hence, when they're launched from dash, instead of being grouped, each is opened separately in the dash. This simple script fixes that.
Currently, the supported apps are:

    1. firefox-trunk

More apps might be added later as I encounter them or someone makes a request.

# Installation and use

This script is only dependent on python. If you're using Ubuntu, just run the following script:
```bash
sudo apt-get install python
git clone https://github.com/SinTan1729/WMClassFixer
cd WMClassFixer
sudo python WMCfix.py
```
For other distros, simply clone the git and run the script as superuser.

# How to make a request/bug report

For request, please provide the package name and PPA. In case of bugs, please provide the package name, PPA and the desktop file (both before (the .bk file) and after editing).

### _You might buy me a cup of coffee:_

**UPI (preferred) : sintan@ybl**

**PayPal : sayantan.santra689@gmail.com** 