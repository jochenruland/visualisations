import seaborn as sb
import matplotlib as plt
import pandas as pd

class Customcountplot(sb.countplot):
    """A countplot with axis lables and title"""
    def __init__(self, *args, x_lab='category', y_lab='counts', tit='barchart for qualitative data', **kwargs):
        super().__init__(*args, **kwargs)

        self.x_lab = x_lab
        self.y_lab = y_lab
        self.tit = tit

        plt.xlabel(self.x_lab)
        plt.ylabel(self.y_lab)
        plt.title(self.tit)






    #def __init__(self, x, y, hue=None, data=None, order=None, hue_order=None,
    #             orient="h", color=sb.color_palette()[1], palette=None, saturation=0.75, dodge=True, ax=None, **kwargs,
    #             x_lab='category', y_lab='counts', tit='barchart for qualitative data'):
    #    super().__init__(self, x, y, hue, data, order, hue_order, orient, color, palette,
    #                    saturation, dodge, ax)
        ''' you can either setup the Custom class __init__ function with all arguments
            necessary for the __init__ of the parent class and pass those values to
            the parent class OR you only pass less arguments to the __init__ of the parent class but
            then you will have to use the default values of the parent class '''
                        #(self, *, x, y, hue, data, order,
                        #hue_order, orient, color, palette,
                        #saturation, dodge, ax, **kwargs)

    #    self.data = pd.series()
