import csv
import copy

'''
Creación de un programa de inventario de vehíclos
Definición del diccionario
'''

miVehiculo = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

for key, value in miVehiculo.items():
    print("{} : {}".format(key, value))


miInventarioList = []

'''
Copia el archivo CSV en Memoria
'''

with open('flota_vehiculos.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            print(
                f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(miVehiculo)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            miInventarioList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

currentVehicle = copy.deepcopy(miVehiculo)

'''
Impresión del inventario de vehículos
'''

for miCoche in miInventarioList:
    for key, value in miCoche.items():
        print("{} : {}".format(key, value))
        print("-----")
