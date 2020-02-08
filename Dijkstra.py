graaf = {
    'a': {'b': 4, 'c': 3, 'e': 8},
    'b': {'a': 4, 'c': 6, 'd': 5},
    'c': {'a': 3, 'b': 6, 'd': 11, 'e': 8},
    'd': {'b': 5, 'c': 11, 'e': 2, 'g': 10, 'f': 2},
    'e': {'c': 8, 'd': 2, 'g': 5},
    'g': {'d': 10, 'e': 5, 'f': 3},
    'f': {'d': 2, 'g': 3}
    }

def dijkstra(graaf, start, eind):
    onbezochte_knopen = graaf
    kortste_afstand = {}
    voorganger = {}
    oneindig = 9999999
    route = []
    
    for knoop in onbezochte_knopen:
        kortste_afstand[knoop] = oneindig
    kortste_afstand[start] = 0

    while onbezochte_knopen:
        min_knoop = None
        
        for knoop in onbezochte_knopen:
            
            if min_knoop is None:
                min_knoop = knoop
                
            elif kortste_afstand[knoop] < kortste_afstand[min_knoop]:
                min_knoop = knoop

        for buurknoop, gewicht in graaf[min_knoop].items():
            
            if gewicht + kortste_afstand[min_knoop] < kortste_afstand[buurknoop]:
                kortste_afstand[buurknoop] = gewicht + kortste_afstand[min_knoop]
                voorganger[buurknoop] = min_knoop
                
        onbezochte_knopen.pop(min_knoop)

    huidige_knoop = eind
    
    while huidige_knoop != start:
        
        try:
            route.insert(0,huidige_knoop)
            huidige_knoop = voorganger[huidige_knoop]
            
        except KeyError:
            print('Route is niet mogelijk.')
            break
        
    route.insert(0,start)
    if kortste_afstand[eind] != oneindig:
        print('De kortste afstand is ' + str(kortste_afstand[eind]))
        print('De route is ' + str(route))
        
dijkstra(graaf, 'a', 'f')
