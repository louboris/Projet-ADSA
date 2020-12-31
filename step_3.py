import numpy as np

def floyd_warshall(graph):
    """
    Floyd warshall algorithm
    """
    distance = {v:dict.fromkeys(graph, float('inf')) for v in graph}
    suivv = {v:dict.fromkeys(graph, None) for v in graph}

    for e in graph:
        for voi in graph[e]:
            distance[e][voi] = graph[e][voi]
            suivv[e][voi] = voi
 
    for v in graph:
         distance[v][v] = 0
         suivv[v][v] = None
 
    for p in graph: 
        for v in graph:
            for w in graph:
                if distance[v][w] > distance[v][p] + distance[p][w]:
                    distance[v][w] = distance[v][p] + distance[p][w]
                    suivv[v][w] = suivv[v][p]

    return distance

if __name__ == "__main__":
    adsaMap = {
        'Reactor': {'a': 2.5},
        'a': {'Reactor': 2.5, 'Security': 2, 'Lower E.': 3, 'Upper E.': 3},
        'Upper E.': {'a': 3, 'b': 4},
        'Lower E.': {'a': 3, 'c': 5},
        'c': {'Electrical': 2.5, 'Lower E.': 5, 'Storage': 4},
        'Electrical': {'c': 2.5},
        'Storage': {'d': 3, 'f': 3.5, 'c': 4},
        'd': {'Cafetaria': 4, '01': 2.5, 'Storage': 3},
        'Cafetaria' : {'b': 4.5, 'd': 4, 'Weapons': 5.5},
        'b': {'Medbay': 2, 'Upper E.': 4, 'Cafetaria': 4},
        'Weapons': {'Cafetaria': 5.5, 'g': 2},
        'g': {'02': 2, 'e': 1},
        'e': {'Navigations': 2.5, 'Shield': 5, 'g': 2},
        'Shield': {'e': 5, 'f': 2.5},
        'f': {'03': 1.5, 'Shield': 2.5, 'Storage': 3.5},
        'Security': {'a': 2},
        'Medbay': {'b': 2},
        '01': {'d': 2.5},
        '03': {'f': 1.5},
        '02': {'g': 2},
        'Navigations': {'e': 2.5},
        
    }

    adsaMapImpostor =  {
    'Reactor': {'a': 2.5, 'Upper E.': 0, 'Lower E.': 0},
    'a': {'Reactor': 2.5, 'Security': 2, 'Lower E.': 3, 'Upper E.': 3},
    'Upper E.': {'a': 3, 'b': 4, 'Reactor':0},
    'Lower E.': {'a': 3, ' c': 5, 'Reactor': 0},
    'c': {'Electrical': 2.5, 'Lower E.': 5, 'Storage': 4},
    'Electrical': {'c': 2.5, 'Security':0 ,'Medbay':0},
    'Storage': {'d': 3, 'f': 3.5},
    'd': {'Cafetaria': 4, '01': 2.5, 'Storage': 3},
    'Cafetaria' : {'b': 4.5, 'd': 4, 'Weapons': 5.5, 'h': 0, '01': 1},
    'b': {'Medbay': 2, 'Upper E.': 4, 'Cafetaria': 4},
    'Weapons': {'Cafetaria': 5.5, 'g': 2},
    'g': {'02': 2, 'e': 1},
    'e': {'Navigations': 2.5, 'Shield': 5, 'g': 2, 'h': 1.5},
    'Shield': {'e': 5, 'f': 2.5, 'h': 3.5},
    'f': {'03': 1.5, 'Shield': 2.5, 'Storage': 3.5},
    'Security': {'a': 2, 'Medbay':0 , 'Electrical': 0},
    'Medbay': {'b': 2, 'Security': 0, 'Electrical': 0},
    '01': {'d': 2.5, 'h': 0, 'Cafetaria': 0},
    '03': {'f': 1.5},
    '02': {'g': 2},
    'Navigations': {'e': 2.5},
    'h': {'e': 1.5, ' Shield': 3.5, 'Cafetaria': 0, '01': 0 },

    }

    rooms = ['Reactor','Upper E.','Security','Medbay','Electrical','Storage','Cafetaria','Storage','01','02','03','Shield','Weapons','Navigations']


    matrixCrewmate = floyd_warshall(adsaMap)
    matrixImpostor = floyd_warshall(adsaMapImpostor)   

    paths = []
    for a in rooms:
        for b in rooms:
            if [a,b] not in paths and [b,a] not in paths and a != b:
                paths.append([a,b])
    print('%-12s'%'-','%-12s'%'-','%-12s'%'Crewmate','%-12s'%'Impostor','Interval')
    for e in paths:
        lengthCrewmateFW = matrixCrewmate[e[0]][e[1]]
        lengthImpostorFW = matrixImpostor[e[0]][e[1]]
        print('%-12s'%e[0],'%-12s'%e[1],'%-12s'%lengthCrewmateFW,'%-12s'%lengthImpostorFW, lengthImpostorFW - lengthCrewmateFW)



def step3():
    adsaMap = {
        'Reactor': {'a': 2.5},
        'a': {'Reactor': 2.5, 'Security': 2, 'Lower E.': 3, 'Upper E.': 3},
        'Upper E.': {'a': 3, 'b': 4},
        'Lower E.': {'a': 3, 'c': 5},
        'c': {'Electrical': 2.5, 'Lower E.': 5, 'Storage': 4},
        'Electrical': {'c': 2.5},
        'Storage': {'d': 3, 'f': 3.5, 'c': 4},
        'd': {'Cafetaria': 4, '01': 2.5, 'Storage': 3},
        'Cafetaria' : {'b': 4.5, 'd': 4, 'Weapons': 5.5},
        'b': {'Medbay': 2, 'Upper E.': 4, 'Cafetaria': 4},
        'Weapons': {'Cafetaria': 5.5, 'g': 2},
        'g': {'02': 2, 'e': 1},
        'e': {'Navigations': 2.5, 'Shield': 5, 'g': 2},
        'Shield': {'e': 5, 'f': 2.5},
        'f': {'03': 1.5, 'Shield': 2.5, 'Storage': 3.5},
        'Security': {'a': 2},
        'Medbay': {'b': 2},
        '01': {'d': 2.5},
        '03': {'f': 1.5},
        '02': {'g': 2},
        'Navigations': {'e': 2.5},
        
    }

    adsaMapImpostor =  {
    'Reactor': {'a': 2.5, 'Upper E.': 0, 'Lower E.': 0},
    'a': {'Reactor': 2.5, 'Security': 2, 'Lower E.': 3, 'Upper E.': 3},
    'Upper E.': {'a': 3, 'b': 4, 'Reactor':0},
    'Lower E.': {'a': 3, ' c': 5, 'Reactor': 0},
    'c': {'Electrical': 2.5, 'Lower E.': 5, 'Storage': 4},
    'Electrical': {'c': 2.5, 'Security':0 ,'Medbay':0},
    'Storage': {'d': 3, 'f': 3.5},
    'd': {'Cafetaria': 4, '01': 2.5, 'Storage': 3},
    'Cafetaria' : {'b': 4.5, 'd': 4, 'Weapons': 5.5, 'h': 0, '01': 1},
    'b': {'Medbay': 2, 'Upper E.': 4, 'Cafetaria': 4},
    'Weapons': {'Cafetaria': 5.5, 'g': 2},
    'g': {'02': 2, 'e': 1},
    'e': {'Navigations': 2.5, 'Shield': 5, 'g': 2, 'h': 1.5},
    'Shield': {'e': 5, 'f': 2.5, 'h': 3.5},
    'f': {'03': 1.5, 'Shield': 2.5, 'Storage': 3.5},
    'Security': {'a': 2, 'Medbay':0 , 'Electrical': 0},
    'Medbay': {'b': 2, 'Security': 0, 'Electrical': 0},
    '01': {'d': 2.5, 'h': 0, 'Cafetaria': 0},
    '03': {'f': 1.5},
    '02': {'g': 2},
    'Navigations': {'e': 2.5},
    'h': {'e': 1.5, ' Shield': 3.5, 'Cafetaria': 0, '01': 0 },

    }

    rooms = ['Reactor','Upper E.','Security','Medbay','Electrical','Storage','Cafetaria','Storage','01','02','03','Shield','Weapons','Navigations']


    matrixCrewmate = floyd_warshall(adsaMap)
    matrixImpostor = floyd_warshall(adsaMapImpostor)   

    paths = []
    for a in rooms:
        for b in rooms:
            if [a,b] not in paths and [b,a] not in paths and a != b:
                paths.append([a,b])
    print('%-12s'%'-','%-12s'%'-','%-12s'%'Crewmate','%-12s'%'Impostor','Interval')
    for e in paths:
        lengthCrewmateFW = matrixCrewmate[e[0]][e[1]]
        lengthImpostorFW = matrixImpostor[e[0]][e[1]]
        print('%-12s'%e[0],'%-12s'%e[1],'%-12s'%lengthCrewmateFW,'%-12s'%lengthImpostorFW, lengthImpostorFW - lengthCrewmateFW)

