#task-1.10
#Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame.
import pandas as pd
loc="https://raw.githubusercontent.com/manas1410/Spectrum-Internship-2020-task-1-/master/diamonds.csv"#stores the path of diamonds.csv
diamonds=pd.read_csv(loc)
print("Number of rows and columns:")
print(diamonds.shape)#The shape attribute of pandas. DataFrame stores the number of rows and columns as a tuple (number of rows, number of columns)
print("After droping those rows where values are missing:")
#Pandas DataFrame dropna() function is used to remove rows and columns with Null/NaN values.
print(diamonds.dropna(how='any').shape)
