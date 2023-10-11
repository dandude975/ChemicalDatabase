import os

print("I AM BEING RUN!!!")

def installation(os):
    if os.lower() == "mac":
        print("Installing libraries...")

        os.system('BIN="/usr/local/bin/askpass"; touch $BIN; chmod 755 $BIN')
        os.system('security add-generic-password -a $USER -s login -T "" -w')
        os.system('echo "#!/bin/sh\\nsecurity find-generic-password -a $USER -s login -w" > $BIN')
        os.system('echo "\\n# Set sudo helper.\\nexport SUDO_ASKPASS=$BIN" >> ~/.${SHELL##/*/}rc')

        os.system('SUDO_ASKPASS=#!/bin/sh /usr/local/bin/askpass sudo -A /bin/bash -c "$(curl -fsSL '
                  'https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system("python3 -m pip install mysql-connector-python")
        print("Press [enter] to go to the MySQL downloads page and install the correct version, then return here")
        input()
        os.system('open https://dev.mysql.com/downloads/shell/')
        install = False
        while not install:
            print("Have you installed MySQL Shell?")
            answer = input("y/n: ")
            if answer == 'y':
                os.system('MySQL -V')
                install = True
            else:
                print("Install MySQL to use this program")
                print()
    elif os.lower() == "windows":
        print("Not supported for Windows currently")
        exit()
    elif os.lower() == 'linux':
        print("Not supported for Linux currently")
        exit()
