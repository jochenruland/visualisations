from ready_to_go_bar_charts import Customplotdata
import matplotlib.pyplot as plt

cpd=Customplotdata()
cpd.read_dataframe_fom_file('fuel-econ.csv')
cpd.print_dtypes()
cpd.customcountplot(x='make', hue='feScore')
plt.show()
