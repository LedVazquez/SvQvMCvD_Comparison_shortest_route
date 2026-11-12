#Main script for comparisons

import numpy as np

from methods import Dijkstra as D
from methods import Q_learning as Q


def get(name):
    content=[]
    with open("tests/"+name+".txt") as f:
        # for line in f:
        content=f.readlines()

    # print(content)
    data=[[] for i in range(int(content[0]))]
    for row in content[1:]:
        aux_row=[int(i) for i in row.split()]
        
        data[aux_row[0]].append(tuple((aux_row[1],aux_row[2])))
        data[aux_row[1]].append(tuple((aux_row[0],aux_row[2])))

    return data

seed=42

Q_Learn_data={
    "episodios" : 20000,
    "alpha" : .1,
    "gamma" : 0.95,
    "epsilon_inicial" : 1.5,
    "epsilon_minimo" : 0.05,
    "decaimiento_epsilon" : 0.9995,
    "maximo_pasos":200
}

SARSA_data={
    "alpha":0.10,
    "gamma":0.95,
    "epsilon":0.10,
    "episodios":1000
}

graph=get(f"test_{input("Ingrese N° caso de prueba: ")}")

print(D.start(graph, 0))

