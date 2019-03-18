import shutil

#firefox-trunk

f=open("/usr/share/applications/firefox-trunk.desktop","r")
contents=f.readlines()
f.close()
if "StartupWMClass=Nightly\n" not in contents:
    shutil.copyfile("usr/share/applications/firefox-trunk.desktop","usr/share/applications/firefox-trunk.desktop.bk")
    contents.insert(contents.index("[Desktop Action new-window]\n")-1,"StartupWMClass=Nightly\n")
    f=open("/usr/share/applications/firefox-trunk.desktop","w")
    f.writelines(contents)
    f.close()
    print("fixed firefox-trunk")
else:
    print("firefox-trunk is okay")
