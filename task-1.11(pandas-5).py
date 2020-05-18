#task-1.11
#Write a Pandas program to count the duplicate rows of diamonds DataFrame.
import pandas as pd
loc="https://raw.githubusercontent.com/manas1410/Spectrum-Internship-2020-task-1-/master/diamonds.csv"#stores the path of diamonds.csv
diamonds=pd.read_csv(loc)
l=list(diamonds.columns)
l.remove('Unnamed: 0')
print("\nDuplicate rows of diamonds DataFrame:")
#Pandas duplicated() method helps in analyzing duplicate values only
#duplicated().sum() finds how many duplicate values are present
print(diamonds.duplicated(subset=l,keep='first').sum())

