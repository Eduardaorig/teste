import customtkinter as ctk




class Aplication():
    
    def __init__(self):
       self.janela = ctk.CTk()
       self.tela()
       self.mensagem()
       self.janela.mainloop()
       
    def tela(self):
        self.janela.title("TESTE DE BRANCH")
        self.janela.geometry("700x500")
        self.janela.resizable(False, False)
        self.janela._set_appearance_mode("dark")
    
    def mensagem(self):
        label_ola = ctk.CTkLabel(master= self.janela, text= "OLÁ MUNDO!")
        label_ola.pack()
        
        


Aplication()