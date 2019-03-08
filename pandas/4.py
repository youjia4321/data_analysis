import pandas as pd
from pandas import DataFrame

new_data ={'Modi': {2010: 72, 2012: 78, 2014 : 98},'Rahul': {2010: 55, 2012: 34, 2014: 22}}
elections = DataFrame(new_data) 
# print(elections)
# print(elections.Modi)
elections.index.name = 'year'
elections.columns.name = 'politicians'
print(elections)
print(elections.values)