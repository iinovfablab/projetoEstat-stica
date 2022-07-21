import os
import numpy as np
import math

def reverse_key_to_value(d:list) -> dict:
    return dict(map(lambda x: x[::-1], d))


def read_file_list(level, path=False, dirname="files"):
    current_path = "\\".join(os.path.abspath(__file__).split('\\')[:-level])
    path_file = os.path.join(current_path, dirname)
    if not path:
        func_filt = lambda x: x.endswith(".xlsx")
        files = list(filter(func_filt, os.listdir(os.path.abspath(path_file))))
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
        j=np.insert(j, max_, 0)
    j = np.append(j, np.zeros((1,(range_at-y))))
  
    return j


def range_variation(df):
    f = lambda x: x>0
    d = []
    columns = df.columns[1:]
    for c in range(len(df.columns[1:])):
        d.append(len(list(filter(f,df.iloc[:,c+1]))))

    return d

def reduction_col(df):
    for col in df.columns:
        if(len(col)>10):
            return True
    return False
    