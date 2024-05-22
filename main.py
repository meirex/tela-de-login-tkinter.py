from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores -------------------
co0 = "#f0f3f5"  # Preta 
co1 = "#feffff"  # branca 
co2 = "#008000"  # verde
co3 = "#38576b"  # valor 
co4 = "#403d3d"  # letra 




#JANELA
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(background= co1)
janela.resizable(width=FALSE, height= FALSE)


#dividir a janela
frame_cima = Frame(janela, width=310, height=50, bg= co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg= co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#frame de cima
nome = Label(frame_cima, text='APP DE LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
nome.place(x=5, y=5)

linha = Label(frame_cima, text='', width=98, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
linha.place(x=10, y=45)



infos = ['Gabriel@mail', '123456']
def validar_usuario(usuario):
    if '@' not in usuario:
        messagebox.showerror("Erro de Validação", "O usuário deve conter '@'")
        return False
    return True

def validar_senha(senha):
    if len(senha) < 6:
        messagebox.showerror("Erro de Validação", "A senha deve conter no mínimo 6 caracteres")
        return False
    return True

def verificarSenha():
    usuario = entryUsuario.get()
    senha = entrySenha.get()

    if not validar_usuario(usuario) or not validar_senha(senha):
        return

    if usuario == 'adm@' and senha == 'adm123':
        messagebox.showinfo('Login', 'Seja bem vindo, adm')
    elif infos[0] == usuario and infos[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta ' + infos[0])
    else:
        messagebox.showwarning('Erro', 'Erro, verifique o usuário e senha novamente')




#frame baixo
nome = Label(frame_baixo, text='Usuario (email)', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
nome.place(x=10, y=20)
entryUsuario= Entry(frame_baixo, width=25, justify='left', font=('', 12), highlightthickness=1, relief= 'solid')
entryUsuario.place(x=14, y=50)

senha = Label(frame_baixo, text='Senha', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
senha.place(x=10, y=95)
entrySenha= Entry(frame_baixo, width=25, justify='left',show='*',  font=('', 12), highlightthickness=1, relief= 'solid')
entrySenha.place(x=14, y=130)

botaoConfirmar = Button(frame_baixo, command=verificarSenha,  text='Entrar', width=10, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief= RIDGE)
botaoConfirmar.place(x=15, y=180) 










janela.mainloop()