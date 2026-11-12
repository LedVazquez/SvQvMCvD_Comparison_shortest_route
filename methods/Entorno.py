# Script for the entorno

class entorno:

    def __init__(self, graph, src):
        self.graph=graph
        self.states=len(graph)
        self.actions=len(graph)
        self.estado_inicial=src

    def reset(self):
        self.estado=self.estado_inicial 
        return self.estado