import matplotlib.pyplot as plt
import pandas as pd

#tabela com os dados fixos (dados iniciais do mercado)
tabelafixa = pd.read_excel("D:\Mercado.xlsx")

def mercado():
        figura = plt.figure(figsize=(40,40))
        figura.suptitle('Grafico de Mercado')

        tabela = pd.read_excel("D:\Mercado.xlsx")
        tabela2 = pd.read_excel("D:\MercadoOferta.xlsx")
        tabela3 = pd.read_excel("D:\MercadoDemanda.xlsx")

        mercado = tabela[['Preco','Demanda','Oferta','Status']]
        mercado2 = tabela3[['Preco','DemandaAlta','StatusAlto','DemandaBaixa','StatusBaixo','Oferta']]
        mercado3 = tabela2[['Preco','OfertaAlta','StatusAlto','OfertaBaixa','StatusBaixo','Demanda']]
        column_labels= ['Preco','Demanda','Oferta','Status de Mercado']

        figura.add_subplot(321)
        plt.plot(tabela['Demanda'], tabela['Preco'], label='Demanda', color='k')
        plt.plot(tabela['Oferta'], tabela['Preco'], label='Oferta', color='b')
        plt.scatter(tabela['Demanda'][4], tabela['Preco'][4], label='Equilibrio de Mercado', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Gráfico de Mercado')
        plt.legend()
        


        df= pd.DataFrame(mercado, columns=['Preco','Demanda','Oferta','Status'])
        table = plt.table(
                cellText=df.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        table.set_fontsize(15.0)
        table.scale(4, 6)

        figura.add_subplot(323)
        plt.plot(tabela['Demanda'], tabela['Preco'], label='Demanda', color='k')
        plt.plot(tabela['Oferta'], tabela['Preco'], label='Oferta', color='b')
        plt.plot(tabela3['DemandaAlta'], tabela2['Preco'], label='Deslocamento de Demanda', color='r')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.title('Alta Demanda no Mercado')
        plt.legend()
        


        df2= pd.DataFrame(mercado2, columns=['Preco','DemandaAlta','Oferta','StatusAlto'])
        table = plt.table(
                cellText=df2.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        table.set_fontsize(15.0)
        table.scale(4, 6)
        
        figura.add_subplot(325)
        plt.plot(tabela['Demanda'], tabela['Preco'], label='Demanda', color='k')
        plt.plot(tabela['Oferta'], tabela['Preco'], label='Oferta', color='b')
        plt.plot(tabela2['OfertaAlta'], tabela2['Preco'], label='Deslocamento de Oferta', color='g')
        plt.xlabel('Quantidade')
        plt.ylabel('Preço')
        plt.legend()


        df3= pd.DataFrame(mercado3, columns=['Preco','Demanda','OfertaAlta','StatusAlto'])
        table = plt.table(
                cellText=df3.values,
                colLabels=column_labels,
                colWidths= [0.09] * 4,
                cellLoc='center',
                loc="right")
        table.set_fontsize(15.0)
        table.scale(4, 6)
        plt.title('Alta Oferta no Mercado')
        plt.show()
