import os

os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)')
os.system('brew install mysql')
os.system('brew unlink mysql')
os.system('brew install mysql-connector-c')
os.system('pip install MySQL-python')
os.system('brew unlink mysql-connector-c')
os.system('brew link mysql')