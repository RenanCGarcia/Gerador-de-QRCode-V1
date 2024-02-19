import customtkinter
from tkinter import *
import qrcode
from PIL import Image

def gerarQR():
    qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link.get())

    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Gerador de QRCODE v2/qrcode.png")
    
    QRimg = Image.open('Gerador de QRCODE v2/qrcode.png')
    QRimg.show()


customtkinter.set_appearance_mode("Dark")

janela = customtkinter.CTk()
janela.title("Gerador de QRCODE")
janela.iconbitmap('Gerador de QRCODE v2/icon.ico')
janela.geometry("500x150")
janela.resizable(width=False, height=False)

texto = customtkinter.CTkLabel(janela, text="GERADOR DE QRCODE")
texto.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(janela, width=400, placeholder_text="Insira o link")
link.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="GERAR", command=gerarQR)
botao.pack(padx=10, pady=10)

janela.mainloop()
