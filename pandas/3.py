import pandas as pd

states ={'State' :['Gujarat', 'Tamil Nadu', ' Andhra', 'Karnataka', 'Kerala'],
                  'Population': [36, 44, 67,89,34],
                  'Language' :['Gujarati', 'Tamil', 'Telugu', 'Kannada', 'Malayalam'], 'Level': ['A','B','C','D','E']}
india = pd.DataFrame(states)
print(india)
india.index = ['a','n','g','r','y']
print(india)
print(india.iloc[3])

new_farme = pd.DataFrame(states, columns=['State', 'Language', 'Population', 'Per Capita Income'], index =['a','b','c','d','e'])

# print(new_farme.State)

# print(new_farme.iloc[:3])
new_farme['Development'] = new_farme.State == 'Gujarat'
print(new_farme)