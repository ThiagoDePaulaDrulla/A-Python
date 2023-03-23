import math
import dists

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
        exploited = {start : 1}; #Explorados
        costs = {}  #Custos do nó atual
        actual_city = ''
        route = []
        i = False
        
        if(dists.get(start,None) and start != goal):
            actual_city = start
            index = 0
            toral_range = 0
            while i == False:
                costs = {} 
                range_city = {}
                
                for city in dists[actual_city]:
                    if(exploited.get(city[0],None) == None):
                         costs[city[0]] = ((city[1] + toral_range) + straight_line_dists_from_bucharest[city[0]])                    
                         range_city[city[0]] = city[1]
                         exploited[city[0]] = 1
                    else:
                        continue
                costs = dict(sorted(costs.items(), key=lambda item: item[1]))
                actual_city = next(iter(costs))
                toral_range += range_city.get(actual_city, 0)
                route.insert(index, actual_city+'( f(n): '+str(costs.get(actual_city, 0))+')')
                if(actual_city == goal):
                   i = True
                   break
                index = index + 1
            print('Caminho --> Pé na tábua!')
            route.insert(0, start)
            print(route)        
        else:
            print('Cidade Inválida ou você já se encontra na cidade Sr')
   

dists = {
    'Bucharest': [
        ('Urzineci',85),
        ('Giurgiu',90),
        ('Pitesti',101),
        ('Fagaras',211)
    ],
    'Giurgiu': [
        ('Bucharest',90)
    ],
    'Urzineci': [
        ('Bucharest',85),
        ('Hirsova',98),
        ('Vaslui',142)
    ],
    'Hirsova': [
        ('Urzineci',98),
        ('Eforie',86)
    ],
    'Eforie': [
        ('Hirsova',86)
    ],
    'Vaslui': [
        ('Urzineci',142),
        ('Iasi',92)
    ],
    'Iasi': [
        ('Vaslui', 92),
        ('Neamt',87)
    ],
    'Neamt': [
        ('Iasi', 87)
    ],
    'Fagaras': [
        ('Bucharest',211),
        ('Sibiu',99)
    ],
    'Pitesti': [
        ('Bucharest',101),
        ('Rimnicu Vilcea',97),
        ('Craiova',138)
    ],
    'Craiova':[
        ('Pitesti',138),
        ('Rimnicu Vilcea',146),
        ('Dobreta',120)
    ],
    'Rimnicu Vilcea':[
        ('Craiova',146),
        ('Pitesti',97),
        ('Sibiu',80)
    ],
    'Sibiu':[
        ('Rimnicu Vilcea',80),
        ('Fagaras',99),
        ('Oradea',151),
        ('Arad',140)
    ],
    'Oradea':[
        ('Sibiu',151),
        ('Zerind',71)
    ],
    'Zerind':[
        ('Oradea',71),
        ('Arad',75)
    ],
    'Arad':[
        ('Zerind',75),
        ('Timisoara',118),
        ('Sibiu',140)
    ],
    'Timisoara':[
        ('Arad',118),
        ('Lugoj',111)
    ],
    'Lugoj':[
        ('Timisoara',111),
        ('Mehadia',70)
    ],
    'Mehadia':[
        ('Lugoj',70),
        ('Dobreta',75)
    ],
    'Dobreta':[
        ('Mehadia',75),
        ('Craiova',120)
    ],
}


straight_line_dists_from_bucharest = {
    'Arad': 366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urzineci':80,
    'Vaslui':199,
    'Zerind':374
}

#Testado com os exemplos do professor Razer (Arad->Bucharest) e também do trabalho (Lugoj->Bucharest)
print('Bem vindo(a) ao GPS que é BOM! Aqui garantimos o BOM Caminho ;)')
start = input('Informe a cidade de origem: ')
a_star(start)
