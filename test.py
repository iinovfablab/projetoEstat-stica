
from traceback import print_tb
from model.courses_model import CoursesModel
from model.training_model import TrainingModel
from scripts.dataframe_to_image import dataframe_to_image
from scripts.plot_to_image import plot_to_image
from scripts.tools import reverse_key_to_value, read_file_list
import locale
import calendar
import pandas as pd
import os

unicode = "pt_BR.UTF-8"
locale.setlocale(locale.LC_ALL, unicode)

if __name__ == "__main__":
    c = CoursesModel()
    for u in c.courses_name():
        print(u, end='\n')
