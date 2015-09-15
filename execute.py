from subprocess import call
import sys


command = '''\
#!/bin/bash
type=daemon
cd Desktop
if [ -d Gymnasiearbete ]; then
    cd Gymnasiearbete
    git pull
    if [ $? -ne 0 ]; then
        echo Något blev fel när projektet skulle synkas med github
        echo -n Tryck på enter för att avsluta
        read
        exit
    fi
else
    git clone https://github.com/gkraften/Gymnasiearbete.git
    if [ $? -ne 0 ]; then
        echo Något blev fel när projektet skulle hämtas från github
        echo -n Tryck på enter för att avsluta
        read
        exit
    fi
    cd Gymnasiearbete
fi

cd Robot
if [[ $type == daemon ]]; then
    sudo python3 main.py > /home/pi/Desktop/meddelanden.txt 2> /home/pi/Desktop/fel.txt &
else
    sudo python3 main.py || read
fi'''

if sys.platform == "darwin":
    applescript = ('if application "Terminal" is running then\n'
                   '	tell application "Terminal"\n'
                   '		activate\n'
                   '		do script "command"\n'
                   '	end tell\n'
                   'else\n'
                   '	tell application "Terminal"\n'
                   '		activate\n'
                   '		do script "command" in window 1\n'
                   '	end tell\n'
                   'end if')
    call(["osascript", "-e", applescript.replace("command", "ssh pi@raspberrypi.local '{}'; exit".format(command))])
else:
    print("Det fungerar inte på den här datorn än")