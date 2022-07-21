import dataframe_image as dfi
import pandas as pd


def dataframe_to_image(df, file_name):
    dfi.export(df, file_name)
