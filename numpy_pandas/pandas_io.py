from pandas import read_csv, read_excel, read_html, read_sql
from sqlalchemy import create_engine

df = read_csv('example')

# specify index false to not save the index as unnamed column
# df.to_csv('my_example', index=False)

# pandas can read/write excel files but cannot read formulas, images or macros.
# This can cause pandas to crash

# pip install xlrd required here
df = read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')

print(df)

# pip install openpyxl required here
# df.to_excel('Excel_Sample.xlsx', sheet_name='Sheet1', index=False)


# lxml required here
data = read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

print(data[0])
engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = read_sql('my_table', con=engine)

print(sqldf)
