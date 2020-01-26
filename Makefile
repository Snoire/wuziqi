.PHONY : all install uninstall

all : install

install :
	-/bin/cp wuzi.desktop /usr/share/applications/
	-/bin/cp wuzi.py /usr/games/wuzi
	-mkdir /usr/share/icons/wuziqi
	-/bin/cp wuzi.png /usr/share/icons/wuziqi/

uninstall :
	-/bin/rm -rf /usr/share/icons/wuziqi/ /usr/share/applications/wuzi.desktop /usr/games/wuzi
