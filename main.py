

from importlib.resources import path
from model.courses_model import CoursesModel
from model.reserve_model import ReserveModel
from model.training_model import TrainingModel
from scripts.dataframe_to_image import dataframe_to_image
from scripts.plot_to_image import plot_to_dataframe
from scripts.tools import *
from scripts.abcdef import fedcba
import locale
import calendar
import pandas as pd
import datetime
import argparse
import matplotlib.pyplot as plt
import sys


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

unicode = "pt_BR.UTF-8"
locale.setlocale(locale.LC_ALL, unicode)

parser = argparse.ArgumentParser()

parser.add_argument("--month", type=int,
                    help="Gera uma analise com o mês passado por argumento", required=False)

parser.add_argument("--year", type=int, default=datetime.datetime.now().year,
                    help="Gera uma analise com o ano passado por argumento, como padrão esta 2022", required=False)

month_selected = parser.parse_args().month

cc = read_file_list(2, path=True, dirname="files\\")


class_div = ["finder", "zmorph", "lase", "pcb"]

# fedcba("config.json")

if __name__ == "__main__":

    c = CoursesModel().courses_name()
    courses = {}
    courses['x'] = dict(reverse_key_to_value(c))

    # ====================================================================
    pdc = pd.DataFrame.from_dict(courses)
    pdc.to_excel(read_file_list(2, path=True)+"\\alunos.xlsx")
    # ====================================================================

    r = datetime.datetime.now()
    t = TrainingModel()
    m = ReserveModel()
    abe = dict(t.all_courses())

    dates = {}
    data = {}
    mach = {}
    year_ran = {}
    machines = dict(m.all_machines())

    def f(x): return round(x/2)

    #pd.set_option('display.max_colwidth', 10)
    #pd.set_option('display.max_row', 23)
    #pd.set_option('display.expand_frame_repr', False)

    # pd.set_option('display.max_colwidth', None)

    paramter = {
        "figsize": (29, 10),
        "autolayout": True,
        "title": '',
        "files": read_file_list(2, path=True, dirname="images")
    }

    _config = {
        "ylabel": "N° de Treinamentos Realizados",
        "title": '',
        "figsize": (29, 10),
        "width": 1,
        "use_index": False,
        "align": "edge",
        "color": [],
        "rot": 60

    }

    if (parser.parse_args().month):
        if (month_selected == 12):
            dates["dezembro"] = [
                f"{parser.parse_args().year}-12-01 08:00:00", f"{parser.parse_args().year}-12-20 22:00:00"]
        else:

            dates[calendar.month_name[month_selected]] = [
                f'{parser.parse_args().year}-{month_selected}-01 08:00:00', f'{parser.parse_args().year}-{month_selected+1}-01 08:00:00']

        for b in [1, 23, 24, 25]:
            for k, v in zip(dates.keys(), dates.values()):
                data[k] = dict(reverse_key_to_value(t.find_by_training(*v, b)))

            df = pd.DataFrame.from_dict(data)
            # ===================================
            df = one_more_time(df, pdc)
            df.to_excel(cc+f'{abe[b]}.xlsx')

        for o in range(parser.parse_args().year-2018):
            yy = 2019+o
            if (yy == parser.parse_args().year):
                year_ran[str(yy)] = dict(reverse_key_to_value(
                    t.find_all(f'{yy}-01-01 08:00:00', f'{yy:02d}-12-20 22:00:00')))
            else:
                year_ran[str(yy)] = dict(reverse_key_to_value(
                    t.find_all(f'{yy}-01-01 08:00:00', f'{yy}-12-20 22:00:00')))

        for n, i in zip(machines.keys(), machines.values()):
            mach[i] = reverse_key_to_value(m.find_by_machine(
                n, f'{parser.parse_args().year}-{month_selected}-01 08:00:00', f'{parser.parse_args().year}-{month_selected}-30 22:00:00'))
        m._clsose()
        dfm = pd.DataFrame.from_dict(mach)
        # ===================================
        dfm = one_more_time(dfm, pdc)
        dfm = dfm.fillna(0)
        dfm = dfm.apply(lambda x: round(x/2))
        dfm = dfm.fillna('')
        dfm.to_excel(cc+"Horas Máquina.xlsx")

        dfh = pd.DataFrame.from_dict(year_ran)
        dfh = dfh.fillna(0)
        dfh = one_more_time(dfh, pdc)
        dfh.to_excel(cc+f'Relação Anual de Treinamentos.xlsx')

    else:
        for i in range(1, 13):
            dates[calendar.month_name[i]] = [
                f'{parser.parse_args().year}-{i}-02 08:00:00', f'{parser.parse_args().year}-{i+1}-01 08:00:00']
        if (i == 12):
            dates["dezembro"] = [
                f'{parser.parse_args().year}-12-01 08:00:00', f'{parser.parse_args().year}-12-20 22:00:00']
        for b in [1, 23, 24, 25]:
            for k, v in zip(dates.keys(), dates.values()):
                data[k] = dict(reverse_key_to_value(t.find_by_training(*v, b)))
            df = pd.DataFrame.from_dict(data)
            # ===================================
            df = one_more_time(df, pdc)
            df.to_excel(cc+f'{abe[b]}.xlsx')
        for o in range((parser.parse_args().year)-2018):
            yy = 2019+o
            if (yy == parser.parse_args().year):
                year_ran[str(yy)] = dict(reverse_key_to_value(
                    t.find_all(f'{yy}-01-01 08:00:00', f'{yy:02d}-12-26 22:00:00')))
            else:
                year_ran[str(yy)] = dict(reverse_key_to_value(
                    t.find_all(f'{yy}-01-01 08:00:00', f'{yy}-12-26 22:00:00')))
        for n, i in zip(machines.keys(), machines.values()):
            mach[i] = reverse_key_to_value(m.find_by_machine(
                n, f"{parser.parse_args().year}-02-01 00:00:00"))
        m._clsose()
        dfm = pd.DataFrame.from_dict(mach)

        # ===================================
        dfm = one_more_time(dfm, pdc)
        dfm = dfm.fillna(0)
        dfm = dfm.apply(lambda x: round(x/2))
        dfm = dfm.fillna('')

        ind = []

        for index in range(dfm.shape[0]):
            if(sum(dfm.iloc[index,:]) == 0):
                ind.append(index)

        dfk = dfm.iloc[ind]
        print(dfk.index.values)
        dfm = dfm.drop(index=dfk.index.values)

        dfk.to_excel(cc+"Horas Máquina_NFC.xlsx")
        dfm.to_excel(cc+"Horas Máquina.xlsx")

        dfh = pd.DataFrame.from_dict(year_ran)
        dfh = dfh.fillna(0)
        dfh = one_more_time(dfh, pdc)

       
        dfh.to_excel(cc+f'Relação Anual de Treinamentos.xlsx')

        
        

    t._clsose()
    for file in read_file_list(2):

        if (file == "Horas Máquina.xlsx"):
            # "\\".join([read_file_list(2, path=True), file])
            path = read_file_list(2, path=True)+"\\"+file
            dfo = pd.read_excel(path)

            dfo.columns = dfo.columns.str.replace("Unnamed: 0", "Cursos")
            plt.cla()

            rename_rank(dfo, file, month_selected, parser.parse_args().year, 5)

            dff = dfo.sum(numeric_only=True)
            dff['Cursos'] = "Total/Treinamentos"
            dfo = dfo._append(dff.T, ignore_index=True)
            dfo.fillna(0, inplace=True)
            dfo[dfo.columns[1:]] = dfo.iloc[:, 1:].astype(int)
            dfo.columns = ['Cursos', '3D FINDER - 2',
                            'Prototipadora de circuitos impressos',
                            'Parafusadeira Furadeira', 'Furadeira de Bancada',
                            'Scanner 3D', 'Lixadeira portátil', 'Serra tico-tico',
                            'Maquina de costura', 'Estação de solda e retrabalho',
                            'Micro Retífica', '3D FLEXPRINTER',
                            '3D FINDER - 3', '3D ZMorph',
                            'Gravadora de Matrize a vácuo', 'Plotter de recorte',
                            '3D - Guider IIs', '3D FINDER - 1',
                            '3D - Guider IIs -', 'Cortadora/Gravadora a Laser']

            if (reduction_col(dfo)):
                dfo = dfo.style.set_table_styles(
                    [dict(selector="th.col_heading",
                          props=[("writing-mode", "vertical-rl"),
                                    ("font-size", "9px"),
                                 ('transform', 'rotateZ(180deg)'),
                                 ('height', '8%'),
                                 ('width', '90%'),
                                 ('vertical-align', 'left')]),
                    dict(selector="td",
                          props=[("font-size", "8px"),
                                 #('height', '30%'),
                                 ('width', '1200px'),
                                 ]),],
                ) 
            dfo = dfo.apply(hcol, axis=1)
            dataframe_to_image(dfo, read_file_list(
                2, path=True, dirname="images")+'\\'+file[:-5]+"_table"+".png")
            dfo = dfo.data
            paramter['title'] = file[:-5]
            _config['title'] = paramter['title']

            if month_selected:
                plot_to_dataframe(dfo, read_file_list(
                    2, path=True, dirname="images"), *[calendar.month_name[month_selected], parser.parse_args().year], **_config)
            else:
                plot_to_dataframe(dfo, read_file_list(
                    2, path=True, dirname="images"), *[parser.parse_args().year], **_config)

        else:
            path = (read_file_list(2, path=True)+"\\"+file)
            df = pd.read_excel(path)
            df.columns = df.columns.str.replace("Unnamed: 0", "Cursos")
            dx = df.sum(numeric_only=True)
            dx['Cursos'] = "Total/Treinamentos"
            if file.startswith("Relação"):
                dx['Cursos'] = "Total/Treinamentos Anuais"
            df = df._append(dx.T, ignore_index=True)
            df.fillna(0, inplace=True)

            df[df.columns[1:]] = df.iloc[:, 1:].astype(int)
            df = df.style.set_table_styles(
                [dict(selector="th.col_heading",
                      props=[
                          ("writing-mode", "vertical-rl"),
                          ('transform', 'rotateZ(180deg)'),
                          ('heigth', '50%'),
                          ('width', '100%'),
                          ('vertical-align', 'left')]),
                ],
                overwrite=False
            )
            df = df.apply(hcol, axis=1)
        
            dataframe_to_image(df, read_file_list(
                2, path=True, dirname="images")+'\\'+file[:-5]+"_table"+".png")
            df = df.data
            paramter['title'] = file[:-5]
            _config['title'] = paramter['title']
            if month_selected:
                plot_to_dataframe(df, read_file_list(
                    2, path=True, dirname="images"), *[calendar.month_name[month_selected], parser.parse_args().year], **_config)
            else:
                plot_to_dataframe(df, read_file_list(
                    2, path=True, dirname="images"), *[parser.parse_args().year], **_config)
