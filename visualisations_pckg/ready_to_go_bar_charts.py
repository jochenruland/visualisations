import seaborn as sb
import matplotlib as plt
import pandas as pd

class Customcountplot(sb):
    """A countplot with axis lables and title"""
    def __init__(self, *args, x_lab='category', y_lab='counts', tit='barchart for qualitative data', **kwargs):
        super().__init__(*args, **kwargs)

        self.x_lab = x_lab
        self.y_lab = y_lab
        self.tit = tit

        self.countplot(data)
        plt.xlabel(self.x_lab)
        plt.ylabel(self.y_lab)
        plt.title(self.tit)
