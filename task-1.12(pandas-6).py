#task-1.12
#Write a Pandas program to get sample 75% of the diamonds DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame
import pandas as pd
loc="D:/college/Internship(Spectrum)/2/diamonds.csv"
diamonds=pd.read_csv(loc)
print("\nSample 75% of diamonds DataFrame's rows without replacement:")
result = diamonds.sample(frac=0.75, random_state=99)
print(result)
print("\nRemaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(result.index), :])
