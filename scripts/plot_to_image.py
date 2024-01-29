
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scripts.tools import read_file_list, auto_padding, range_variation
import os
import shutil

def plot_to_image(df, **config):
    
    N_ = len(df["Cursos"])
    NUM_COLORS = N_
    func_filt = lambda x: x.endswith(".xlsx") 
    files = list(filter(func_filt, os.listdir(os.path.abspath(read_file_list(2, path=True)))))
    cm = plt.get_cmap('tab20')

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
    ax.legend(df['Cursos'], loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=34)  
    #ax.legend(df['Cursos'], loc='best')
    #plt.show()
    fig.savefig(config['files']+'\\'+config['title'])


def plot_to_dataframe(df, filename, *date, **config):
    sns.set()
    #plt.style.use('fivethirtyeight')
    NUM_COLORS = len(df["Cursos"])
    cm = plt.get_cmap('tab20')
    lc =[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)] 
    config['color'] = lc
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 200
    plt.rcParams.update({'font.size': 6})
    params = {'legend.fontsize': 11,
          'legend.handlelength': 2}
    plt.rcParams.update(params)
    config['ylabel'] = "N° Treinamentos Realizado" if not config['title'].startswith("Horas") else "Horas Maquinas"
    
    df['Cursos'] = df['Cursos'].apply(lambda x: "".join(x.split('-')[-1]))
    if(len(df[df['Cursos']==' UNISANTA'].index)==0):
        pass
    else:
        df = df.drop(index=df[df['Cursos']==' UNISANTA'].index[0], errors='ignore')

    try:
        if(config['title'].startswith("Variação")):
            title_temp = config['title']
            if len(date) > 1:
                config['title'] = config['title']+f" ({date[0]}/{date[1]})"
                ax = df.T.iloc[1:,1:-1].plot(kind='bar', **config, joinstyle='round')
                config['title'] = title_temp
            else:
                config['title'] = config['title']+f" ({date[0]})"
                ax = df.T.iloc[1:,1:-1].plot(kind='bar', **config, joinstyle='round')
                config['title'] = title_temp

            
            
        else:
            title_temp = config['title']
            if len(date) > 1:
                config['title'] = config['title']+f" ({date[0]}/{date[1]})"
                ax = df.T.iloc[1:,1:-1].plot(kind='bar', **config, joinstyle='round')
                config['title'] = title_temp
            else:
                config['title'] = config['title']+f" ({date[0]})"
                ax = df.T.iloc[1:,1:-1].plot(kind='bar', **config, joinstyle='round')
                config['title'] = title_temp
            

        #ax2 = ax.twinx()
        #ax2.plot(np.mean(df.iloc[:, 1:]), c='grey', marker='s') 

        
        Ylim =  max(ax.get_ylim())+5
        ax.set_ylim((0, Ylim))

        #ax2.set_yticks(ax.get_yticks())
        #ax2.set_ylim((0,Ylim))
        ax.legend(df['Cursos'],loc='center left', bbox_to_anchor=(1, 0.5))
        #ax.legend(df['Cursos'], loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=34)  
        #ax.legend(df["Cursos"])
        #ax2.legend(["média"], loc='upper left')
        if(config['title'] in ["Relação Anual de Treinamentos", "Horas maquina"]):
            #ax.legend(df['Cursos'], loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=34)
            ax.legend(df['Cursos'],loc='center left', bbox_to_anchor=(1, 0.5))
        
        ax.set_xticklabels(df.columns[1:])
        fig = ax.get_figure()
        fig.savefig(filename+'\\'+config['title'])


    except:
        pass
        #shutil.copy(filename+'\\'+'MANUTENÇÃO.png',filename+'\\'+config['title']+'.png')

    
    
    
    