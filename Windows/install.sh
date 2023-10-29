#!/bin/bash

powershell -command "start-process PowerShell -verb runas"
powershell -command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"

choco upgrade chocolatey
choco install git
git -V

git clone https://github.com/dandude975/ChemicalDatabase

choco install mysql
mysql -V
choco services start mysql
choco install pyenv

pyenv install 3.12

python312 -m ensurepip
python312 -m pip install mysql-connector-python
Python312 .\ChemicalDatabase\firstLaunch.py

rm .\ChemicalDatabase\install
