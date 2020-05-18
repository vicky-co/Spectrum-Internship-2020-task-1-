#task-1.7
#Write a Pandas program to read a csv file from a specified source and print the first 5 rows
import pandas as pd #pandas imported
diamonds=pd.read_csv("https://raw.githubusercontent.com/manas1410/Spectrum-Internship-2020-task-1-/master/diamonds.csv",nrows=5) #stores the first 5 rows of diamonds.csv
print("The first 5 rows:")
print(diamonds) #print the first five rows