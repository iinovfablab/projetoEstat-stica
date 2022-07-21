

from importlib.resources import path

from traitlets import observe
from model.courses_model import CoursesModel
from model.reserve_model import ReserveModel
from model.training_model import TrainingModel
from scripts.dataframe_to_image import dataframe_to_image
from scripts.plot_to_image import plot_to_dataframe, plot_to_image
from scripts.tools import reduction_col, reverse_key_to_value, read_file_list
import locale
import calendar
import pandas as pd
import os
import datetime

unicode = "pt_BR.UTF-8"
locale.setlocale(locale.LC_ALL, unicode)


def hcol(x):
    s = x['Cursos']
    if s == 'Total':
        css = 'background-color: #ACCA'
    else:
        css = 'background-color: white'
    return [css]*len(x)


if __name__ == "__main__":

    r = datetime.datetime.now()
    t = TrainingModel()
    m = ReserveModel()
    abe = dict(t.all_courses())
    dates = {}
    data = {}
    mach = {}
    year_ran = {}
    machines = dict(m.all_machines())
    cc = read_file_list(2, path=True, dirname="files\\")
    def f(x): return round(x/2)

    pd.set_option('display.max_colwidth', 6)

    paramter = {
        "figsize": (25, 9),
        "autolayout": True,
        "title": '',
        "files": read_file_list(2, path=True, dirname="images")
    }

    _config = {
        "ylabel": "N° de Treinamentos Realizados",
        "title": '',
        "figsize": (25, 9),
        "width": 1,
        "use_index": False,
        "align": "edge",
        "color": [],
        "rot": 60

    }

    for n, i in zip(machines.keys(), machines.values()):
        mach[i] = reverse_key_to_value(m.find_by_machine(n))

    m._clsose()
    dfm = pd.DataFrame.from_dict(mach)
    dfm = dfm.fillna(0)
    dfm[dfm.columns[1:]] = dfm[dfm.columns[1:]].apply(f)
    dfm.loc['Total'] = dfm.sum(numeric_only=True)
    dfm = dfm.fillna('')

    dfm.to_excel(cc+"Horas maquina.xlsx")

    for i in range(1, r.month):
        dates[calendar.month_name[i]] = [
            f'{r.year}-{i}-01 00:00:00', f'{r.year}-{i+1}-01 00:00:00']
    if(r.month == 12):
        dates["dezembro"] = [
            "{r.year}-12-01 00:00:00", "{r.year}-12-31 00:00:00"]

    for b in [1, 23, 24, 25]:
        for k, v in zip(dates.keys(), dates.values()):
            data[k] = dict(reverse_key_to_value(t.find_by_training(*v, b)))
        df = pd.DataFrame.from_dict(data)
        df = df.fillna(0)
        dx = df.sum(numeric_only=True)
        dx.name = "Total"
        df = df.append(dx.T)
        df.to_excel(cc+f'{abe[b]}.xlsx')

    for o in range(r.year-2018):
        yy = 2019+o
        if(yy==r.year):
            year_ran[str(yy)] = dict(reverse_key_to_value(
            t.find_all(f'{yy}-01-01 08:00:00', f'{yy:02d}-{r.month:02d}-{r.day} 22:00:00')))
        else:
            year_ran[str(yy)] = dict(reverse_key_to_value(
                t.find_all(f'{yy}-01-01 08:00:00', f'{yy}-12-26 22:00:00')))
    dfh = pd.DataFrame.from_dict(year_ran)
    dfh = dfh.fillna(0)
    dxh = dfh.sum(numeric_only=True)
    dxh.name = "Total"
    dfh = dfh.append(dxh.T)
    dfh.to_excel(cc+f'Variação Anual.xlsx')

    t._clsose()
    for file in read_file_list(2):

        path = (read_file_list(2, path=True)+"\\"+file)
        df = pd.read_excel(path)
        df.columns = df.columns.str.replace("Unnamed: 0", "Cursos")

        df = df.style.apply(hcol, axis=1)
        if(reduction_col(df)):
            df = df.set_table_styles(
                [dict(selector="th.col_heading",
                      props=[("writing-mode", "vertical-rl"),

                             ('transform', 'rotateZ(180deg)'),
                             ('height', '290px'),
                             ('vertical-align', 'left')])],
            )

        dataframe_to_image(df, read_file_list(
            2, path=True, dirname="images")+'\\'+file[:-5]+"_table"+".png")
        df = df.data
        _config['title'] = paramter['title'] = file[:-5]
        plot_to_dataframe(df, read_file_list(
            2, path=True, dirname="images"), **_config)
