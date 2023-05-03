import pandas as pd
import csv
import numpy as np

folder = 'C:\\Users\\u1056\\Fracture_Project_simulations\\PULLING\\Classic_numerical_Example\\'
simulation = 'Experiment_data_MY_ANGLES'



data = pd.read_csv(folder + simulation + '.SIF')
print(data)

top = data.iloc[ 1 : 2 ] #top should have higher KI than bottom
top = pd.concat((top, data.iloc[15:27]), axis=0)

bottom = data.iloc[ 2 : 15 ]
# bottom = pd.concat((bottom, data.iloc[23:26]), axis=0)
top = top.reset_index(drop=True)
bottom = bottom.reset_index(drop=True)

print("\ntop:")
print(top)
print("\nbottom:")
print(bottom)

top.to_csv(folder + simulation + '_TOP.SIF')
bottom.to_csv(folder + simulation + '_BOTTOM.SIF')



"""writing the top csv"""
