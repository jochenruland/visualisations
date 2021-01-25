import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sb
import numpy as np
import pandas as pd

class Customplotdata():
    """ Creates a Customplotdata object which stores information how to format different matplotlib.pyplot and seaborn plots.
        The matplotlib.pyplot functions which can be called as methods of the Customplotdata object work in their original way
        only adding the formatting information stored in the object"""
    def __init__(self, x_label='category', y_label='counts', p_title='countplot', cat_order_list=None, p_figsize=[5,5], p_legend=False):
        self.x_label=x_label
        self.y_label=y_label
        self.p_title=p_title
        self.p_figsize=p_figsize
        self.p_legend=p_legend

        if cat_order_list is not None:
            self.ordered_cat = pd.api.types.CategoricalDtype(ordered=True, categories=cat_order_list)



    def read_dataframe_fom_file(self, filename):
        ''' Function to read in data from a .csv file. The data is stored in the
            p_df attribute of the object.

            Args:
                filname (string): name of file to read from
                Returns:
                None '''
        self.p_df = pd.read_csv(filename)

    def print_dtypes(self):
        print(self.p_df.dtypes)

    def customcountplot(self, x):
        fig=plt.figure(figsize=self.p_figsize)
        fig.suptitle(self.p_title, fontsize=16)
        base_color = sb.color_palette()[1]
        sb.countplot(data=self.p_df, x=x, color=base_color)

cpd=Customplotdata()
cpd.read_dataframe_fom_file('pokemon.csv')
#test_cpd.print_dtypes()
cpd.customcountplot('type_2')
plt.show()
