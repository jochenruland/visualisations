import pandas as pd

def read_data_file(filename):
    ''' Function to read in data from a .csv file. The file should have a
        categorical value and a quantitative value per line separated by comma.

        Args:
            filname (string): name of file to read from
        Returns:
            None '''
    s = pd.read_csv(filename)
    return s

b_chart = Customcountplot()
d_series = read_data_file('datafile.csv')

plt.show(b_chart)
