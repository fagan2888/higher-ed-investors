###################################
# Import modules
###################################

import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

###################################
# Loda data
###################################

df = pd.read_csv('dataset.csv')

###################################
# Inspec data
###################################

def df_shape():
	df.shape
	df.describe()

def df_scatter():
	scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal='kde')
	plt.show()
	plt.savefig('df_scatter_matrix.png')
	
def inspect_vars():
	
	df['X1'].plot()

	df.plot(x='X1', y='X2', kind='scatter')
	plt.show()

	plt.savefig('x1vsx2_scatter.png')

df_shape()
df_scatter()
df_inspect_vars()