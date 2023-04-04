import csv

def read(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader)
        lista = []
        for row in reader:
            d = {header[i] : row[i] for i in range(len(header))}
            lista.append(d)
    return lista


if __name__ == '__main__':
    read('C:/Users/sebas/OneDrive/Programacion/Curso de python_Comprehensions, funciones y manejo de errores/app/world_population.csv')
