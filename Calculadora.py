import tkinter as tk 

janela=tk.Tk()
janela.title('Projeto Calculadora - FABRICIO ') # -- TITULO DA JANELA
janela.geometry('700x700+200+200') # -- DIMENSÃO DA JANELA PRINCIPAL
janela['bg'] = 'black' # -- COR DE FUNDO OU BACKGROUND

#-- CRIAÇÃO DA JANELA 
tela = tk.Label(janela, text='', bg='white', font= 20, width=70, height=5, border=5)
tela.grid(row= 0, column= 0, columnspan= 5, padx= 20, pady=50)

# -- BOTÃO 1 
def apertou1():
    tela['text'] += '1'

bt_1 = tk.Button(janela, text='1', width= 10, height=2, border=10, font= 40, command=apertou1)
bt_1.grid(row= 7, column=0, pady= 10)

# -- BOTÃO 2 
def apertou2():
    tela['text'] += '2'

bt_2 = tk.Button(janela, text='2', width= 10, height=2, border=10, font= 40, command=apertou2)
bt_2.grid(row= 7, column=1, pady= 10)

# -- BOTÃO 3 
def apertou3():
    tela['text'] += '3'

bt_3 = tk.Button(janela, text='3', width= 10, height=2, border=10,font= 40, command=apertou3)
bt_3.grid(row= 7, column=2, pady= 10)

# -- BOTÃO 4 
def apertou4():
    tela['text'] += '4'

bt_4 = tk.Button(janela, text='4', width= 10, height=2, border= 10, font= 40, command=apertou4)
bt_4.grid(row= 8, column=0, pady= 10)

# -- BOTÃO 5 
def apertou5():
    tela['text'] += '5'

bt_5 = tk.Button(janela, text='5', width= 10, height=2, border= 10,font= 40, command=apertou5)
bt_5.grid(row= 8, column=1, pady=10)

# -- BOTÃO 6 
def apertou6():
    tela['text'] += '6'

bt_6 = tk.Button(janela, text='6', width= 10, height=2, border= 10,font= 40, command=apertou6)
bt_6.grid(row= 8, column=2, pady=10)

# -- BOTÃO 7 
def apertou7():
    tela['text'] += '7'

bt_7 = tk.Button(janela, text='7', width= 10, height=2, border= 10,font= 40, command=apertou7)
bt_7.grid(row= 9, column=0, pady=10)

# -- BOTÃO 8 
def apertou8():
    tela['text'] += '8'

bt_8 = tk.Button(janela, text='8', width= 10, height=2, border= 10,font= 40, command=apertou8)
bt_8.grid(row= 9, column=1, pady=10)

# -- BOTÃO 9 
def apertou9():
    tela['text'] += '9'

bt_9 = tk.Button(janela, text='9', width= 10, height=2, border= 10,font= 40, command=apertou9)
bt_9.grid(row= 9, column=2, pady=10)

# -- BOTÃO 0 
def apertou0():
    tela['text'] += '0'

bt_0 = tk.Button(janela, text='0', width= 10, height=4, border= 10,font= 40, command=apertou0)
bt_0.grid(row= 10, column=0, pady=10)

# -- BOTÃO C 
def limpa_tela():
    tela['text'] = ''

bt_c = tk.Button(janela, text='C', width= 10, height=4, border= 10,font= 40, background='red', fg='white', command=limpa_tela)
bt_c.grid(row= 10, column=1, pady=10)

# -- BOTÃO RAIZ 

def apertou_Raiz():
    tela['text'] += '**0.5'

bt_raiz = tk.Button(janela, text='RAIZ', width= 10, height=4, border= 10,font= 40, background='blue', fg='white',command=apertou_Raiz )
bt_raiz.grid(row= 10, column=2, pady=10)

# -- BOTÃO SOMAR 

def apertou_Somar():
    tela['text'] += '+'

bt_somar = tk.Button(janela, text='+', width= 12, height=2,border= 10, font= 40,command=apertou_Somar )
bt_somar.grid(row= 7, column=4, pady=10)

# -- BOTÃO SUBTRAIR

def apertou_Subtrair():
    tela['text'] += '-'

bt_subtrair = tk.Button(janela, text='-', width= 12, height=2,border= 10, font= 40, command=apertou_Subtrair)
bt_subtrair.grid(row= 8, column=4, pady=10)

# -- BOTÃO MULTIPLICAR

def apertou_Multiplicar():
    tela['text'] += '*'

bt_multiplicar = tk.Button(janela, text='*', width= 12, height=2,border= 10, font= 40, command=apertou_Multiplicar)
bt_multiplicar.grid(row= 9, column=4, pady=10)

# -- BOTÃO DIVIDIR 

def apertou_Dividir():
    tela['text'] += '/'

bt_dividir = tk.Button(janela, text='/', width= 12, height=2, border= 10,font=40, command=apertou_Dividir)
bt_dividir.grid(row= 10, column=4, pady=10)

# -- BOTÃO RESULTADO

def res():
    tela['text'] = str(eval(tela['text']))

bt_res = tk.Button(janela, text='=', width= 12, height=2, border= 10, font= 40, background='orange', command=res)
bt_res.grid(row= 11, column=4, pady=10)


# -- COMANDO QUE RODA A JANELA OU SEJA MANTEM ELA ABERTA EM LOOP INFINITO
janela.mainloop()