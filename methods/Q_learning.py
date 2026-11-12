#Script for Q learning

import numpy as np
from copy import copy

class Qlearner:


    def __init__(self, data):
        self.episodios=data["episodios"]
        self.alpha=data["alpha"]
        self.gamma=data["gamma"]
        self.epsilon_inicial=data["epsilon_inicial"]
        self.epsilon_minimo=data["epsilon_minimo"]
        self.decaimiento_epsilon=data["decaimiento_epsilon"]
        self.maximo_pasos=data["maximo_pasos"]

    def learn(self, entorno, semilla=None):

        try:

            self.tablaQ=np.zeros((entorno.states, entorno.actions))

            np.random.seed(semilla)

            epsilon=self.epsilon_inicial
            self.historial_recompensas=[]

            for episodio in range(self.episodios):
                estado=copy(entorno.reset())
                terminado= False
                recompensa_total=0
                pasos=0
                explorador=0

                while (not terminado) and pasos<self.maximo_pasos:
                    if np.random.random()<epsilon:
                        accion=np.random.randint(0,entorno.action_space.n)
                    else:
                        accion=np.argmax(self.tablaQ[estado])

                    (
                        estado_siguiente,
                        recompensa,
                        terminado,
                    ) = entorno.step(accion)

                    if terminado:
                        objetivo_temporal=recompensa
                    else:
                        mejor_valor_futuro= np.max(self.tablaQ[estado_siguiente])
                        objetivo_temporal=recompensa+self.gamma*mejor_valor_futuro

                    error_temporal=objetivo_temporal-self.tablaQ[estado][accion]
                    
                    self.tablaQ[estado][accion]+=self.alpha*error_temporal

                    recompensa_total+=recompensa

                    estado=estado_siguiente
                    pasos+=1

                self.historial_recompensas.append(recompensa_total)
                epsilon=max(self.epsilon_minimo, epsilon*self.decaimiento_epsilon)

            return("Aprendizaje completado! -Q")
        except Exception as e:
            return e
        

    def get_tablaQ(self):
        return self.tablaQ

    def get_historial_recompensas(self):
        return self.historial_recompensas

    def redefine_parameters(self, data, seed):
        self.episodios=data["episodios"]
        self.alpha=data["alpha"]
        self.gamma=data["gamma"]
        self.epsilon_inicial=data["epsilon_inicial"]
        self.epsilon_minimo=data["epsilon_minimo"]
        self.decaimiento_epsilon=data["decaimiento_epsilon"]
        self.maximo_pasos=data["maximo_pasos"]

