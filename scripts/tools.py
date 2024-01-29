from copy import copy
import os
import numpy as np
import math
from collections import defaultdict
import matplotlib.pyplot as plt
from .dataframe_to_image import dataframe_to_image
import pandas as pd
import calendar
import re


def hcol(x):
    s = x['Cursos']
    if s in ['Total/Máquina', 'Total/Treinamentos', 'Total/Treinamentos Anuais']:
        css = 'background-color: #ACCA'
    else:
        css = 'background-color: transparent'
    return [css]*len(x)

def rename_date_title(html, month_selected, year):
    if(month_selected):
        dd = f"*{calendar.month_name[month_selected]}/{year}*"
    else:
        dd = f"*{year}*"

    pattern = r"[*].*\d\w.[*]"
    html = html.split('\n')
    for line in range(len(html)):
        if(re.sub(pattern, '*zezinho*', html[line]) != html[line]):
            html[line] = re.sub(pattern, dd, html[line])

    return '\n'.join(html)




def courses_name(df, *exclude) -> pd.DataFrame:

    new_ind = list(map(lambda u: u.split('-')[-1] if u not in exclude else u , df.index))
    df = df.rename(index=dict(zip(df.index, new_ind)))
    return df

def reverse_key_to_value(d: list) -> dict:
    return dict(map(lambda x: x[::-1], d))


def read_file_list(level, path=False, dirname="files"):
    current_path = "\\".join(os.path.abspath(__file__).split('\\')[:-level])
    path_file = os.path.join(current_path, dirname)
    if not path:
        files = list(filter(lambda x: x.endswith(".xlsx"), os.listdir(os.path.abspath(path_file))))
        return files
    return path_file


def auto_padding(y, range_at, range_value=10):

    # Função para definir espaçamento entre os cursos
    """

    parametro: y: quantidade de elementos do mínimo até o máximo
                  exemplo(y = 3)-> [0.1, 0,-0.1 ]

               range_at: completa a lista com zeros até o limite do range_at.
               exemplo(y = 3, range_at = 10)-> [0.1, 0, -0.1, 0, 0, 0, 0, 0, 0, 0]

               range_value: define um divisor de espaçamentos entre cada indice

    """

    min_ = -(math.floor(y/2))
    even_ = (y/2) > math.floor(y/2)
    max_ = abs(min_)

    a = np.asarray(np.linspace(0, min_/range_value, max_+1)[::-1][:-1])
    b = np.asarray((abs(a)[::-1]))
    j = np.append(a, b)

    if(even_):
        j = np.insert(j, max_, 0)
    j = np.append(j, np.zeros((1, (range_at-y))))

    return j


def range_variation(df) -> list:
    def f(x): return x > 0
    d = []
    columns = df.columns[1:]
    for c in range(len(df.columns[1:])):
        d.append(len(list(filter(f, df.iloc[:, c+1]))))

    return d


def reduction_col(df):
    for col in df.columns:
        if(len(col) > 10):
            return True
    return False


def add_row(df, c):
    
    d = defaultdict(lambda: 0)
    c = list(dict(c).values())
    courses = list(df.iloc[:,0])[:-1]
    columns = list(df.columns)
    xxx = list(filter(lambda x: x not in courses, c))
    lista_cursos = []
    for l in xxx:
        for c in columns:
            if c.startswith('Cursos'):
                d[c] = l
            else:
                d[c]
        lista_cursos.append(dict(d))
    return lista_cursos

def rename_rank(df, file, month, year, rang=3):
    cc = read_file_list(2, path=True, dirname="files\\")
    ccl = ['#1f77b4','#ff7f0e', '#2ca02c','#d62728','#9467bd']
    c=['background-color:#1f77b4','background-color:#ff7f0e','background-color:#2ca02c', 'background-color:#d62728', 'background-color:#9467bd']
    t = df.sum(numeric_only=True, axis=1)
    t.sort_values()
    col = [df['Cursos'][x] for x in t.sort_values(ascending=False).index]

    col = list(map(lambda u: u.split('-')[-1], col))
    df = df.fillna(0)
    ax = df.sum(numeric_only=True, axis=1, skipna=True).sort_values(ascending=False)[:rang].plot.pie(autopct='%1.1f%%', 
                                                                                            figsize=(1.5,1.5), 
                                                                                            labels=None, 
                                                                                            textprops={'fontsize':3, 'color':'white'}, 
                                                                                            colors = ccl)

    plt.xlabel("")
    plt.ylabel("")
    fig = ax.get_figure()
    fig.savefig(read_file_list(2, path=True, dirname="images")+'\\'+"rank_pie.png", dpi=600)
    
    dd = df.sum(numeric_only=True, axis=1).sort_values(ascending=False)[:rang]

    dd2 = pd.DataFrame((dd/dd.sum())*100)
    dd2 = dd2.rename(index=dict(zip(dd2.index, col)))
    dd2.columns = ['Uso do Laboratório (%)']
 
    dd2.to_excel(cc+'rank.xlsx')

    map_ind = {x:y for x, y in zip(dd2.index, c)}
 

    
    dd2 = dd2.style.apply(lambda x: x.index.map(map_ind))
    dd2 = dd2.set_properties(**{'color':'white'})
    dataframe_to_image(dd2, read_file_list(2, path=True, dirname="images")+'\\'+file[:-5]+"_rank"+".png")

    with open("teste.html", "r", encoding='utf-8') as f:
        text = f.read()


    podium = list(map(lambda s: f"[{s.split('-')[-1]}]", dd2.index))

    if len(podium) == 0:
        podium = ["[Unisanta]", "[Unisanta]", "[Unisanta]"]
        text = rename_date_title(text, month, year)
        text = replace_html(text, podium)
        with open("teste.html", "w", encoding='utf-8') as f:
            f.write(text)
    else:
        podium = [podium[1], podium[0], podium[2]]
        text = rename_date_title(text, month, year)
        text = replace_html(text, podium)
        with open("teste.html", "w", encoding='utf-8') as f:
            f.write(text)


def one_more_time(df, pdc):
    df = pd.concat([df, pdc], axis = 1)
    df = df.drop('x', axis=1)
    #===================================
    df = df.fillna(0)
    df = courses_name(df, *["EX-ALUNO UNISANTA", "PROFESSOR PÓS-GRADUAÇÃO UNISANTA","ALUNO PÓS-GRADUAÇÃO UNISANTA"])
    filter_ = df.index == " UNISANTA"
    df = df.drop(index=df[filter_].index[0])
    return df



def hcol(x):
    s = x['Cursos']
    if s in ['Total/Máquina', 'Total/Treinamentos', 'Total/Treinamentos Anuais']:
        css = 'background-color: #ACCA'
    else:
        css = 'background-color: transparent'
    return [css]*len(x)

def rename_date_title(html, month_selected, year):
    if(month_selected):
        dd = f"*{calendar.month_name[month_selected]}/{year}*"
    else:
        dd = f"*{year}*"

    pattern = r"[*].*\d\w.[*]"
    html = html.split('\n')
    for line in range(len(html)):
        if(re.sub(pattern, '*zezinho*', html[line]) != html[line]):
            html[line] = re.sub(pattern, dd, html[line])

    return '\n'.join(html)




def courses_name(df, *exclude) -> pd.DataFrame:

    new_ind = list(map(lambda u: u.split('-')[-1] if u not in exclude else u , df.index))
    df = df.rename(index=dict(zip(df.index, new_ind)))
    return df

def replace_html(html, list_):
    pattern  = r"\[\s*[[A-z]\w{1,}.{1,}\]"
    html = html.split('\n')
    count = 0
    for line in range(len(html)):
        
        if(re.sub(pattern, '[zezinho]', html[line]) != html[line]):
            html[line] = re.sub(pattern, list_[count], html[line])
            count+=1
            if(count>2):
                break
    return '\n'.join(html)

