f=open("/usr/share/applications/firefox-trunk.desktop","r")
contents=f.readlines()
f.close()

contents.insert(contents.index("[Desktop Action new-window]\n")-1,"StartupWMClass=Nightly\n")

f=open("/usr/share/applications/firefox-trunk.desktop","w")
f.writelines(contents)
f.close()
