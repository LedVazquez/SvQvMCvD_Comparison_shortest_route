#Script for Dijkstra

import numpy as np
import sys 

import time

class global_counter:
    def __init__(self):
        self.p=0

    def pasito(self):
        self.p+=1

    def show(self):
        return self.p

class min_plist:

    def __init__(self):
        counter.pasito()
        self.list=[]

    def push(self, item):
        counter.pasito()
        self.list.append(item)

    def pop(self):
        counter.pasito()
        min=0
        for e in range(1,len(self.list)):
            if self.list[e][1]<self.list[min][1]:
                counter.pasito()
                min=e
                counter.pasito()

        return self.list.pop(min)

    def is_empty(self):
        counter.pasito()
        return len(self.list)==0

def graph_to_string(graph):
    res=""
    for node in graph:
        nhood=""
        for vecino in node:
            nhood+=f"vecino {(vecino[0])} - peso {vecino[1]}, "

        res+=f"\tNodo {graph.index(node)}: {nhood[:-2]}\n"

    return res

def dis_to_string(distancias, src):
    res="\n"
    for i in range(len(distancias)):
        res+=f"{src} - {i} = {  "no-conexo" if distancias[i]==sys.maxsize else distancias[i]}\n"

    return res

def print_rutas(rutas, src):
    res=""
    for ruta in rutas:
        res+=str(f"{src} - {rutas.index(ruta)} = {ruta}\n")
    return res

def get_rutas(previous, src):
    routes=[[]]*len(previous)
    n=src
    for i in range(len(previous)):
        aux=[]
        cur=n
        while True:
            # print(cur)
            aux.append(cur)
            if cur==src:
                break
            cur=previous[cur]

        if -1 in aux:
            routes[n]="no conexo"
        else:
            routes[n]=aux[::-1]
        n+=1
        if n>=len(previous):
            n=0
    return routes

def dijkstra(graph, src):
    pqueue=min_plist()
    counter.pasito()
    previos=[-1]*len(graph)
    procesados=[]

    dist=[sys.maxsize]*len(graph)
    counter.pasito()
    counter.pasito()

    # print("Distancias: ",dist, f"\n{line}\n")
    
    dist[src]=0
    counter.pasito()

    previos[src]=src
    counter.pasito()

    pqueue.push(tuple((src, 0)))
    counter.pasito()

    while not pqueue.is_empty():
        #nodo, distancia

        counter.pasito()
        n, d=pqueue.pop()
        procesados.append(n)

        counter.pasito()
        if d>dist[n]:
            continue

        #vecino, peso
        for v, p in graph[n]:

            if v in procesados:
                continue
            counter.pasito()
            if dist[n]+p <dist[v]:
                counter.pasito()
                dist[v]=dist[n]+p
                counter.pasito()
                pqueue.push(tuple((v, dist[v])))

                counter.pasito()
                previos[v]=n

            # print(f"nodo: {v}, distancias: {dist}")

    return dist, previos

def start(graph, src):

    start=time.time()

    distancias, previos=dijkstra(graph, src)

    end=time.time()

    # dist_steps=f"\n{line}\nDistancias: {}\nPasos: {counter.show()}"

    rutas=print_rutas(get_rutas(previos, src), src)

    return end-start, dis_to_string(distancias, src), rutas, counter.show()

line="-------------"
counter=global_counter()


