import pandas as pd

## Here we can set how many rows of data we want to see otherwise be content with 10!
pd.set_option('display.max_rows', 100)

## Read the entire CSV file into a pandas DataFrame
df = pd.read_csv("FIFA21-player-list.csv")

## Display the length of the dataframe
print("Nr. rows", len(df))

## Display the number of rows and column
print("Shape (rows, cols)", df.shape)

## Select a number of columns - all rows

df1 = df[['short_name', 'age', 'value_eur', 'wage_eur' ]]
#df1.sort_values(by=['age'], inplace=True, ascending=False)

print(df1) 

df1 = df[['short_name', 'age', 'nationality', 'league_name']]
## Irish Players, Can you work out the error?
irishPlayers = df1[df1['nationality'] == 'Republic of Ireland']
print(irishPlayers)

## Premier League Players over 30, Can you work out the error?
premPlayersOver30 = df1[(df1['league_name'] == 'English Premier League') & (df1['age'] > 30)]
print(premPlayersOver30)

##When using loc the part before the comma is the rows you want, and the part after the comma are the columns you want to select.
playersOver30 = df1.loc[(df1['age'] > 30), ['short_name', 'age']]
print(playersOver30)

## Nationality Counts
nationalityCounts = df1['nationality'].value_counts()
print (nationalityCounts)

## OK now some data analysis
df1 = df[['short_name', 'age', 'wage_eur' ]]
## What is the average player age?
print("Average player age:", df1['age'].mean())


## What are the youngest and oldest ages
print("Youngest:", df1['age'].min())
print("Oldest:", df1['age'].max())

## What is the median age and wage of a player? Can you work out the error?
#print("Median age/wage:\n", df1[['age', 'wage_eur']].median())

# Player wage grouped by age? Get the ages, Get the Wages and average them!
print(df1.groupby('age')['wage_eur'].mean())

## Normally put this up at the top of your script
import matplotlib.pyplot as plt

## Graph Player wage grouped by age
df = df1.groupby('age')['wage_eur'].mean()
print(df)
plt.plot(df)
plt.show()





#print(df)

#print(df.to_string())

#print(df.head())

#print(df.head(10))

#print(df.tail())

#print(df.loc[0])

#print(df.info())




