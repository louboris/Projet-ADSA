adsaMap = {
        'Reactor':['Upper E.', 'Lower E.','Security'],
        'Upper E.': ['Lower E.','Reactor','Security','Cafetaria','Medbay'],
        'Lower E.': ['Reactor','Upper E.','Security','Electrical','Storage'],
        'Electrical': ['Lower E.','Storage'],
        'Storage': ['Lower E.','Electrical','Cafetaria','01'],
        'Cafetaria' : ['Medbay','Upper E.','01','Storage','Weapons'],
        'Weapons': ['02','Shield','Navigations','Cafetaria'],
        'Shield': ['Weapons','02','Navigations','Storage','03'],
        'Security': ['Reactor','Upper E.','Lower E.'],
        'Medbay': ['Upper E.', 'Cafetaria'],
        '01': ['Cafetaria', 'Storage'],
        '03': ['Storage', 'Shield'],
        '02': ['Weapons','Navigations','Shield'],
        'Navigations': ['Weapons','02','Shield']
    }

def conv(dic):
    output= {}
    for e in dic:
        for i in dic[e]:
            try:
                output[e].append(i)
            except:
                output[e] = [i]
    return output


def hamilton2(graph, path, nextV):
    """
    This algorithm return the hamilton path for a given graph. 
    Input: graph: the given graph
    path: The path of the hamiltonian path
    nextV: the next node that going to be visited
    """
    #print(path)
    if(len(graph) == len(path) + 1 and nextV not in path):  
        return [nextV]

    for e in graph[nextV]:
        if(e not in path):
            
            a = hamilton2(graph, path + [nextV], e)
            if(a != None):
                return [nextV] + a




path = hamilton2(adsaMap,[],"Electrical")

if __name__ == "__main__":
    print("Visite the rooms in this order: ")
    for e in path:
        print(e)

def step4():
    print("Visite the rooms in this order: ")
    for e in path:
        print(e)





