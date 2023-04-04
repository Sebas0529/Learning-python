import utils 
import charts
import read_csv
label =[]
values =[]
data = read_csv.read('C:/Users/sebas/OneDrive/Programacion/Curso de python_Comprehensions, funciones y manejo de errores/app/world_population.csv')
country = str(input('ingresa el pais que quieres analizar ==> ')).capitalize()
inf_country = utils.population_by_country(data, country)
try:
    if len(inf_country[0])> 0:
        label, values = utils.get_population(inf_country[0])
        charts.generate_bar_chart(label,values)
except IndexError:
    print('Ingreso un pais que no esta en la lista vuelva a intentar')
