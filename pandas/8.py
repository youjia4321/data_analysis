from pandas import DataFrame
states ={'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
                  'Population': [36, 44, 67,89,34],
                  'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam']}
india = DataFrame(states, columns =['State', 'Population', 'Language'])
print(india)
print(india[india['Population']>50])
print(india.loc[[1,3], ['State','Population']])
s = india.reindex(index=[list('abcde')])
print(s)
print(s.loc[['a','b'], ['State','Population']])