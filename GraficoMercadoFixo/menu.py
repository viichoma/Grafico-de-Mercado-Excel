import Demanda
import Oferta
import Mercado
import matplotlib.pyplot as plt
from matplotlib.widgets import  Button

#Criando um botao
axButton1 = plt.axes([0.25, .8, 0.5, 0.1])
btn1 = Button(axButton1, 'Grafico de Demanda')

#Dando funçao ao botão
def btndemanda(event):
        Demanda.demanda()
btn1.on_clicked(btndemanda)

axButton2 = plt.axes([0.25, .65, 0.5, 0.1])
btn2 = Button(axButton2, 'Grafico de Oferta')

def btnoferta(event):
        Oferta.oferta()
btn2.on_clicked(btnoferta)

axButton3 = plt.axes([0.25, .5, 0.5, 0.1])
btn3 = Button(axButton3, 'Grafico de Mercado')

def btnmercado(event):
        Mercado.mercado()
btn3.on_clicked(btnmercado)

plt.show()