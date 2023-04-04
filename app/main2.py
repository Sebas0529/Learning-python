import utils 
import charts
import read_csv


data = read_csv.read('C:/Users/sebas/OneDrive/Programacion/Curso de python_Comprehensions, funciones y manejo de errores/app/world_population.csv')
options = set([n['Continent'] for n in data])
print(options)
continent = str(input('de que continente quieres que se muestre la estadistica mundial ==> '))
data = list(filter(lambda n : n['Continent']==continent,data))
label, values = utils.select_column('World Population Percentage',data)

charts.generate_pie_chart(label,values)

print(set([1,2,3,4,5,5,5,6,7]))