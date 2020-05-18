#task-1.9
#Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.
import pandas as pd
loc="https://raw.githubusercontent.com/manas1410/Spectrum-Internship-2020-task-1-/master/diamonds.csv"#stores the path of diamonds.csv
diamonds=pd.read_csv(loc)
print("\nCount, minimum, maximum  price for each cut of diamonds DataFrame:")
print(diamonds.groupby('cut').price.agg(['count', 'min', 'max']))#print the count, minimum, maximum price for each cut of diamonds DataFrame.
