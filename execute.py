from subprocess import call
import sys


command = '''cd Desktop
if [ -d Gymnasiearbete ]; then
    cd Gymnasiearbete
    git pull
else
    git clone https://github.com/gkraften/Gymnasiearbete.git
    cd Gymnasiearbete
fi

cd Robot
sudo python3 main.py'''

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
    call(["osascript", "-e", applescript.replace("command", "ssh pi@raspberrypi.local '{}'; read; exit".format(command))])
else:
    print("Det fungerar inte på den här datorn än")