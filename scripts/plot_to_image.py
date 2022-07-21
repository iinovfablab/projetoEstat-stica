from calendar import c
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scripts.tools import read_file_list, auto_padding, range_variation
import os

sns.set_style("darkgrid")

def plot_to_image(df, **config):

    N_ = len(df["Cursos"])
    NUM_COLORS = N_
    func_filt = lambda x: x.endswith(".xlsx") 
    files = list(filter(func_filt, os.listdir(os.path.abspath(read_file_list(2, path=True)))))
    cm = plt.get_cmap('Paired')

    lc =[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]
    d = []

    t = np.linspace(-0.2, 12, 40) # variações dos meses
    
    for k in range(N_):
        d.append(np.linspace(0, 11, len(df.columns[1:])))
    d = np.array(d)

    for p in range(N_):
        for q in range(len(df.columns[1:])):
            d[p][q] = d[p][q]+t[p]



    var = range_variation(df)

    ze = np.array([])
    for o in range(len(var)):
        ze = np.append(ze, auto_padding(var[o], len(df["Cursos"]), 10))
    
    ze = ze.reshape(len(df.columns[1:]), len(df["Cursos"])).T

    
    for v in range(ze.shape[0]-1):
        for p in range(ze.shape[1]-1):
            if((ze[v][p] - ze[v][p+1]) and (np.count_nonzero(ze.T[p]) > 2)):
                ze[v][p] = ze[v][p]+0.1



    condition = "Numero de Treinamentos relaizado" if files != "Horas maquina" else "Horas"
    #===========================================================
    plt.rcParams['figure.figsize'] = config['figsize']         #
    plt.rcParams['figure.autolayout'] = config['autolayout']   #
    cm = plt.get_cmap('tab20')                                 #
    fig, ax = plt.subplots()                                   #
    ax.set_xticks(range(0,len(df.columns[1:])),labels=df.columns[1:])

    ax.set_ylabel(condition)                                   #
    ax.set_title(config['title'])                              #
    #===========================================================


    for i in range(N_):
        ax.bar(np.arange(len(df.columns[1:]))+ze[i], df.iloc[i,1:], align='center', width=0.05, color=lc[i])
        plt.plot(np.arange(len(df.columns[1:]))+ze[i], df.iloc[i,1:])

    ax.legend(df['Cursos'], loc='best')
    #plt.show()
    fig.savefig(config['files']+'\\'+config['title'])


def plot_to_dataframe(df, filename, **config):

    NUM_COLORS = len(df["Cursos"])
    cm = plt.get_cmap('tab20')
    lc =[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]

    _rmax = np.mean(df.iloc[:, 1:-1]).max()


    
    config['color'] = lc
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 250
    plt.rcParams.update({'font.size': 20})
    cm = plt.get_cmap('Paired')
    config['ylabel'] = "N° Treinamentos Realizado" if not config['title'].startswith("Horas") else "Horas Maquinas"
    print(config['title'])

    if(config['title'].startswith("Variação")):
        ax = df.T.iloc[1:,1:-1].plot(kind='bar', **config)
    else:
        ax = df.T.iloc[1:,1:].plot(kind='bar', **config)
    
    ax2 = ax.twinx()
    ax2.plot(np.mean(df.iloc[:, 1:]), c='grey', marker='s')



    gvalue = 0
    for value in ax.get_yticks():
        if(value > _rmax):
            gvalue = value
            break
    gvalue
    
    Ylim =  max(ax.get_ylim())+5
    ax.set_ylim((0, Ylim))

    ax2.set_yticks(ax.get_yticks())
    ax2.set_ylim((0,Ylim))

    ax.legend(df["Cursos"])
    ax2.legend(["média"], loc='upper left') 
    ax.set_xticklabels(df.columns[1:])
    fig = ax.get_figure()
    fig.savefig(filename+'\\'+config['title'])
    
    
    