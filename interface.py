import customtkinter as ctk
from tkinter import *
from trainer import*
# from test import predict_spam

# interface = CTk()

# interface.title('Test de spam')
# interface.iconbitmap('icone.ico')
# interface.minsize(400, 400)
# interface.maxsize(600, 600)
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        def TEST():
            mess = phrase.get("0.0", "end")
            message_transformed = vectorizer.transform([mess])
            prediction = model.predict(message_transformed)
            if prediction == [0]:
                resultat.configure(text=f'Résultat : ce message n\'est pas un spam',text_color="green")
            else:
                resultat.configure(text=f'Résultat : ce message est un spam', text_color="red")


        self.title("Test de spam")
        self.iconbitmap('icone.ico')
        self.geometry("400x400")
        self.minsize(400, 400)
        self.maxsize(400,400)

        label1 = ctk.CTkLabel(self, text="Test de spam", text_color='blue', font=('Arial',40, "bold"))
        label1.grid(pady=20, row=0)

        label2 = ctk.CTkLabel(self, text="Entrez une phrase à vérifier", text_color='gray', font=('helvetica', 16))
        label2.grid(pady=5, padx=20, row=1, column=0)

        phrase = ctk.CTkTextbox(self, width=360, height=100)
        phrase.grid(pady=5, padx=20, row=2, column=0)


        def ANNULER():
            phrase.delete("1.0", "end")
            resultat.configure(text=" ")
        
        tester = ctk.CTkButton(self, text="Tester", border_width=1, border_color="blue", fg_color="white", text_color="blue", command=TEST)
        tester.grid(row=3, column=0, padx=1, pady=20)
        annuler = ctk.CTkButton(self, text="Annuler", border_color="red", border_width=1, fg_color="white", text_color="red", command=ANNULER)
        annuler.grid(row=4, column=0, pady=2)

        resultat = ctk.CTkLabel(self, text=" ", text_color='green', font=('Arial', 16))
        resultat.grid(pady=20, row=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()