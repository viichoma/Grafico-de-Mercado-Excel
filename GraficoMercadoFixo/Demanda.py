import matplotlib.pyplot as plt
import pandas as pd

#tabela com os dados fixos (dados iniciais do mercado)
tabelafixa = pd.read_excel("D:\Mercado.xlsx")

#Utilizado funçao para ser usado nos botões
def demanda():
        figura = plt.figure(figsize=(40,40))
        figura.suptitle('Grafico de Demanda')

        tabela = pd.read_excel("D:\MercadoDemanda.xlsx") #tabela com as variaçao de demanda
        demanda = tabelafixa[['Preco','Demanda']]
        demanda2 = tabela[['Preco','DemandaAlta']]
        demanda3 = tabela[['Preco','DemandaBaixa']]

        column_labels= ['Preco','Demanda'] 

        figura.add_subplot(321) #adicionar figura (3 linhas, 2 colunas, posição 1)
        plt.plot(tabelafixa['Demanda'], tabelafixa['Preco'], label='Demanda', color='k') #Grafico com os dados de Demanda e Preço
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Gráfico de Demanda')
        plt.legend()
        
        #pegar dados da planilha de excel para gerar uma tabela ao lado do grafico
        df= pd.DataFrame(demanda, columns=['Preco','Demanda'])
        table = plt.table(
                cellText=df.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")

        table.set_fontsize(15.0)
        table.scale(4, 6)


        figura.add_subplot(323)

        plt.plot(tabelafixa['Demanda'], tabelafixa['Preco'], label='Demanda', color='k')
        plt.plot(tabela['DemandaAlta'], tabela['Preco'], label='Deslocamento de Demanda', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Alta Demanda')

        plt.legend()
        

        df2 = pd.DataFrame(demanda2, columns= ['Preco','DemandaAlta'])
        tab = plt.table(
                cellText=df2.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        tab.set_fontsize(15.0)
        tab.scale(4, 6)
        plt.show()

        figura.add_subplot(325)

        plt.plot(tabelafixa['Demanda'], tabelafixa['Preco'], label='Demanda', color='k')
        plt.plot(tabela['DemandaBaixa'], tabela['Preco'], label='Deslocamento de Demanda', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Baixa Demanda')
        plt.legend()

        df3 = pd.DataFrame(demanda3, columns= ['Preco','DemandaBaixa'])
        tab = plt.table(
                cellText=df3.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        tab.set_fontsize(15.0)
        tab.scale(4, 6)
        plt.show()