# ---------------------------------------------------------------
# python importa la libreria OS che controlla il sistema operativo
import os
# ---------------------------------------------------------------
# python importa la libreria Pandas che permette l'importazione ed analisi dei dati: potrà essere richiamata come PD
import pandas as pd

#importo le librerie di visualizzazione dei grafici
#%matplotlib inline

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#posizione_del_dataset = os.path.join(os.getcwd(), "Appendice-statistica-2016", "11.Ricerca e innovazione", "Cap_11_Ricerca e innovazione 02.xlsx")
#nome_del_foglio = 'REG totale'
def seleziona_dataset(posizione_del_dataset, nome_del_foglio):
    '''
    
    :param posizione_del_dataset: la posizione del dataset (vedi "indice dei dataset bes.html 
    :param nome_del_foglio: il nome del foglio di calcolo
    :return dati caricati: 
    '''
    try:
        dati = pd.read_excel(posizione_del_dataset, sheetname=nome_del_foglio)
    except:
        dati = pd.read_excel(posizione_del_dataset, sheetname=None)
        # print(list(dati.keys()))
        print(
            "c'è un problema con il foglio selezionato: riprova selezionando il nome del foglio fra questi nella cella precedente: {}".format(
                list(dati.keys())))

    return dati

def pulitura_dataset(dati, riga_intestazione_colonna):
    # individua la riga corrispondente all'intestazione di colonna e inserisci il valore
    intestazione_colonna = riga_intestazione_colonna
    dati.columns = dati.loc[intestazione_colonna]
    dati.drop(intestazione_colonna, inplace=True)

    # rimuovi le righe senza valori oppure con dati esterni alla tabella
    dati.dropna(axis=1, inplace=True, how="all")
    dati.dropna(inplace=True)

    return dati

def seleziona_sottotabella(dati = "dataset", riga = None):
    '''
    estrai sotto tabella (es. maschi o femmine)
    :param riga:
    :return:
    '''
    if riga == None:
        return dati
    else:
        dati = dati.loc[:riga]
        return dati

def inserisci_indice(dati, indice_di_riga = 'REGIONI E \nRIPARTIZIONI\nGEOGRAFICHE'):
    dati.set_index(indice_di_riga, inplace = True)
    return dati


if __name__ == "__main__":
    print(seleziona_dataset(os.path.join(os.getcwd(), "Appendice-statistica-2016", "11.Ricerca e innovazione", "Cap_11_Ricerca e innovazione 02.xlsx"), 'REG totale'))

