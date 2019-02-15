from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it


def geraLista(lista):
    newlista = []
    for i in range(lista):
        while len(newlista) != lista:
            n = randint(1,1*lista)
            if n not in newlista: newlista.append(n)
    return newlista

def desenhaGrafico(x,y,z,k,xl = "Elementos", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso Medio")
    ax.plot(x,z, label = "Melhor Caso")
    plt.plot(x,k, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    fig.savefig('SelectSort.png')

def SelectionSort(lista):
    index=0
    tam_lista=len(lista)
    while index<tam_lista-1:
        valorMenor = lista[index]
        indexmenor = index
        for i in range(index+1,tam_lista):
            if valorMenor>lista[i]:
                valorMenor=lista[i]
                indexmenor=i
                
        temp = lista[index]
        lista[index]=valorMenor
        lista[indexmenor]=temp
                
        index=index+1

CasoMedio=[]
MelhorCaso=[]
PiorCaso=[]


lista=[10000,20000,30000,40000,50000]

for i in lista:
    lista_gerada=geraLista(i)
    lista_ordenada_cres = sorted(lista_gerada)
    lista_ordenada_dec = sorted(lista_gerada,reverse=True)

    CasoMedio.append(timeit("SelectionSort({})".format(lista_gerada),setup="from __main__ import SelectionSort",number=1))
    MelhorCaso.append(timeit("SelectionSort({})".format(lista_ordenada_cres),setup="from __main__ import SelectionSort",number=1))
    PiorCaso.append(timeit("SelectionSort({})".format(lista_ordenada_dec),setup="from __main__ import SelectionSort",number=1))

#PARTE 1
desenhaGrafico(lista,CasoMedio,MelhorCaso,PiorCaso)


#PARTE2
listapermuta = list(it.permutations([1,2,3,4,5,6],6)) 

novalistapermuta=[]

for i in listapermuta:
  c = list(i)
  novalistapermuta.append(timeit("SelectionSort({})".format(c),setup="from __main__ import SelectionSort",number=1))

menortempo = min(novalistapermuta)
menortempoindex = novalistapermuta.index(menortempo)
print(listapermuta[menortempoindex])