import pandas as pd
import numpy as np


# df = pd.DataFrame({'Name': [f'Person_{i}' for i in range(1, 101)]})
# df['Age'] = np.random.randint(18, 66, size=len(df))
# print(df.head())
# df.to_csv('people_data.csv', index=False)


# lis = [1,2,3,4,5,6,7,8,9,10]
# print(pd.DataFrame(lis))
# print(lis[0:5])

dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
# print(pd.DataFrame(dict))
print(dict['Name'][0:2])
print(dict['Age'][0:2])
print(dict['City'][0:2])
df = pd.DataFrame(dict)

print(df[['Name', 'City']])

people = pd.read_csv('people-100.csv')
product = pd.read_csv('products-1000.csv')
# print("DataFrame shape:", people.shape)
# print(people.head(5))
# print(people.tail(5))


print("Describe people DataFrame:\n", people.describe())
print(people.info())
print(product.iloc[0:5, 0:5])
print(people.iloc[0:5, 0:2])

print(product.loc[product['name'] == 'Product 1'])

print(people.columns.tolist())
print(product.dtypes)
print(people.info())

# Drop will remove Column
print(df.drop(columns=['Age']))
# df.drop(columns=['Age'], inplace=True)
# print(df)

print(product.sum(numeric_only=True))
print(people.sum(numeric_only=True))


print(df.sort_values(by='Age').head(5))

numeric = people.select_dtypes(include=[np.number])
print(numeric.mean().to_dict())
# mysum = people.sum(numeric_only=True)
# print(mysum.head(5))


#Create a new column name as age
# df['Age'] = np.random.randint(18, 66, size=len(df))

# print(product['Age'].value_counts().to_dict())


mydropna = people.dropna()
print(mydropna.head(5))

df_filled = df.fillna(0)
print(df_filled.head(5))




data = {
    'Team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Player': ['Ali', 'Ahmed', 'Bilal', 'Zain', 'Hamza', 'Umer'],
    'Points': [85, 90, 78, 88, 92, 75]
}
df = pd.DataFrame(data)
print(df.groupby('Team')['Points'].mean().head(2))


# Convert the 'Sex' column to string type and print its data type
ww1 = people['Sex'].astype(str)
print(ww1.dtype)
q1= product["ean"].astype(int)
print(q1.dtype)
# df["column_name"] = df["column_name"].astype("int32")


# unique name is poped from name columb
mypeople = people['Sex'].unique()[:5]
print(mypeople)
# use for howmany names are unique
print(people['Sex'].nunique())
# print(people.sample(n=2))

ww2 = people.isnull().sum().to_dict()
print(ww2)

mydf = pd.DataFrame({"A": [1, 22, 30, 10]})   #VAr calculate the average of list of set of elements
mycalc = mydf.var().to_dict()
print("31.var():", mydf.var().to_dict())
if mycalc['A']<12:
    print("Control Average...")
else:
    print("Average Outline...")
print("32.median():", mydf.median().to_dict())
print("34.abs():", mydf.abs().head(1).to_dict())    #Convert all -ve numbers to +ve
print("35.round():", mydf.round(2).head(1).to_dict())
print("39.duplicated():", people.duplicated().sum())