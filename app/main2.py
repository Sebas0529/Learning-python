import utils 
import charts
import read_csv
import pandas as pd





df = pd.read_csv('world_population.csv')

options = set(df['Continent'].values)
print(options)
continent = str(input('de que continente quieres que se muestre la estadistica mundial ==> '))


df = df[df['Continent'] == continent]

countries = list(set(df['Country/Territory'].values))
porcentage = df['World Population Percentage']

charts.generate_pie_chart(continent, countries,porcentage)

print(countries)
print(type(countries))
print(porcentage)


'''
data = list(filter(lambda n : n['Continent'].lower() == continent.lower(), data))
values = list(map(lambda i : i['World Population Percentage'],data))
label = list(map(lambda i : i['Country/Territory'],data))
'''
