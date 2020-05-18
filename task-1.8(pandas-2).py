#task-1.8
#Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series
import pandas as pd
loc="https://raw.githubusercontent.com/manas1410/Spectrum-Internship-2020-task-1-/master/diamonds.csv"#stores the location of diamonds.csv
diamonds=pd.read_csv(loc)
print(f"Select a series form below \n {diamonds.columns}")#print the list of series which are present in diamonds.csv
s=input("Enter which series you want to print:")
print(diamonds[s])#print the choosen series
