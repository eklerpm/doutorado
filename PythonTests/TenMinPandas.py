import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



######## Object Creation ########
# series
s = pd.Series([1,3,5,np.nan,6,8])

print(s)

# dias 
dates = pd.date_range('20130101', periods=6)
print(dates)


# cria uma tabela 6, 4 com índice dates e cabeçalho
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({ 'A' : 1.,
                        'B' : pd.Timestamp('20130102'),
                       'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                      'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                        'F' : 'foo' })

print("Creating a DataFrame by passing a dict of objects that can be converted to series-like.")
print(df2)
print("The columns of the resulting DataFrame have different dtypes.")
print(df2.dtypes)


print("##Viewing Data ##")

print("Here is how to view the top and bottom rows of the frame:")
print(df.head())

print(df.tail(3))


print("Display the index, columns, and the underlying NumPy data:")
print(df.index)
print(df.columns)
print(df.values)

print("describe")
print(df.describe())


print("Transposing your data:")
print(df.T)

print("Sorting by an axis:")
print(df.sort_index(axis=1, ascending=False))


print("Sorting by values:")
print(df.sort_values(by='B'))

######### Selection #########

print("Getting")
print("Selecting a single column, which yields a Series, equivalent to df.A:")
print(df['A'])


print("Selecting via [], which slices the rows.")
print(df[0:3])

print(df['20130102':'20130104'])


######### Selection by Label #########

print("For getting a cross section using a label:")
print(df.loc[dates[0]])

print("Selecting on a multi-axis by label:")
print(df.loc[:,['A','B']])

print("Showing label slicing, both endpoints are included:")
print(df.loc['20130102':'20130104',['A','B']])


print("Reduction in the dimensions of the returned object:")
print(df.loc['20130102',['A','B']])


print("For getting a scalar value:")
print(df.loc[dates[0],'A'])


print("For getting fast access to a scalar (equivalent to the prior method):")
print(df.at[dates[0],'A'])


######### Selection by Position #########

print("Select via the position of the passed integers:")
print(df)
print(df.iloc[3])

# linhas no intervvalo 3 ate 5
# coluna no intervalo 0 até 2
print("By integer slices, acting similar to numpy/python:")
print(df.iloc[3:5,0:2])


# recupera as linhas 1,2,4  e coluna 0 e 2
print("By lists of integer position locations, similar to the numpy/python style:")
print(df)
print(df.iloc[[1,2,4],[0,2]])

print("For slicing rows explicitly:")
print(df.iloc[1:3,:])

print("\nFor slicing columns explicitly:")
print(df.iloc[:,1:3])


print("For getting a value explicitly:")
print(df.iloc[1,1])

print("For getting fast access to a scalar (equivalent to the prior method):")
print(df.iat[1,1])

####### Boolean Indexing #######
print("Using a single column’s values to select data.")
print(df[df.A > 0])

print("Selecting values from a DataFrame where a boolean condition is met.")
print(df[df > 0])

print("Using the isin() method for filtering:")
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

print(df2)


print(df2[df2['E'].isin(['two','four'])])

###### Setting ######
print("Setting a new column automatically aligns the data by the indexes.")
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(s1)
df['F'] = s1

print(df)

print("Setting values by label:")
df.at[dates[0],'A'] = 0
print(df)

print("Setting values by position:")
df.iat[0,1] = 0
print(df)


print("Setting by assigning with a NumPy array:")
df.loc[:,'D'] = np.array([5] * len(df))
print(df)


print("The result of the prior setting operations.")
print(df)

print("A where operation with setting.")
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)


######## Missing Data ########

print("Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.")
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)

df1.loc[dates[0]:dates[1],'E'] = 2
print(df1)

print("To drop any rows that have missing data.")
df1.dropna(how='any')

print(df1)


print("Filling missing data.")
print(df1.fillna(value=10))


print("To get the boolean mask where values are nan.")
print(pd.isna(df1))


######## Operations ########

#### Stats ####
print("Performing a descriptive statistic:")
print(df)
print(df.mean())
print(df.mean(1))


s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print(s)

print(df.sub(s, axis='index'))


####### Histogramming  #######
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)

print(s.value_counts())

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

print(s.str.lower())

######## Merge ########

#### Concat ####
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

pieces = [df[:3], df[3:7], df[7:]]
print(pieces)
pd.concat(pieces)

print("foi trem")
print(pd.concat(pieces))

#### Join ####
print("SQL style merges. See the Database style joining section.")

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(left)
print(right)
print(pd.merge(left, right, on='key'))

print("Another example that can be given is:")
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
print(left)

right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(right)

print(pd.merge(left, right, on='key'))

####### Append #######
print("Append rows to a dataframe. See the Appending section.")
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])

print(df)

s = df.iloc[3]
print(df.append(s, ignore_index=True))

###### Grouping ######
#By “group by” we are referring to a process involving one or more of the following steps:

#Splitting the data into groups based on some criteria
#Applying a function to each group independently
#Combining the results into a data structure


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
	'foo', 'bar', 'foo', 'foo'],
	'B' : ['one', 'one', 'two', 'three',
	'two', 'two', 'one', 'three'],
	'C' : np.random.randn(8),
	'D' : np.random.randn(8)})

print(df)

print("Grouping and then applying the sum() function to the resulting groups.")
print(df.groupby('A').sum())

print("Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.")
print(df.groupby(['A','B']).sum())


######### Reshaping #########

### Stack ###
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
'foo', 'foo', 'qux', 'qux'],
['one', 'two', 'one', 'two',
'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df2 = df[:4]

print(df2)
