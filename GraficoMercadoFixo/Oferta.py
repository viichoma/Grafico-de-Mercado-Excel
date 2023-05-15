import matplotlib.pyplot as plt
import pandas as pd

#tabela com os dados fixos (dados iniciais do mercado)
tabelafixa = pd.read_excel("D:\Mercado.xlsx")

def oferta():
        figura = plt.figure(figsize=(40,40))
        figura.suptitle('Grafico de Oferta')

        tabela = pd.read_excel("D:\MercadoOferta.xlsx")
        oferta = tabelafixa[['Preco','Oferta']]
        oferta2 = tabela[['Preco','OfertaAlta']]
        oferta3 = tabela[['Preco','OfertaBaixa']]
        column_labels= ['Preco','Oferta']

        figura.add_subplot(321)
        plt.plot(tabelafixa['Oferta'], tabelafixa['Preco'], label='Oferta', color='k')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Gráfico de Oferta')
        plt.legend()
        # plt.scatter(qntfx[3],precofx[3], color='b')


        df= pd.DataFrame(oferta, columns=['Preco','Oferta'])
        table = plt.table(
                cellText=df.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        table.set_fontsize(15.0)
        table.scale(4, 6)

        figura.add_subplot(323)

        plt.plot(tabelafixa['Oferta'], tabelafixa['Preco'], label='Oferta', color='k')
        plt.plot(tabela['OfertaAlta'], tabela['Preco'], label='Deslocamento de Oferta', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Alta Oferta')

        plt.legend()
        #plt.scatter(tabelafixa['Oferta'][3], tabelafixa['Preco'][3], color='b')

        df2 = pd.DataFrame(oferta2, columns= ['Preco','OfertaAlta'])
        tab = plt.table(
                cellText=df2.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        tab.set_fontsize(15.0)
        tab.scale(4, 6)
        
        figura.add_subplot(325)

        plt.plot(tabelafixa['Oferta'], tabelafixa['Preco'], label='Oferta', color='k')
        plt.plot(tabela['OfertaBaixa'], tabela['Preco'], label='Deslocamento de Oferta', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Baixa Oferta')
        plt.legend()

        
        df3 = pd.DataFrame(oferta3, columns= ['Preco','OfertaBaixa'])
        tab = plt.table(
                cellText=df3.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        tab.set_fontsize(15.0)
        tab.scale(4, 6)

        plt.show()
