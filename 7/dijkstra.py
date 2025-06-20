path = {"start" : {"A" : 6, "B" : 2}}
print(path["start"].keys())

path["A"] = {}
path["A"]["end"] = 1

path["B"] = {}
path["B"]["A"] = 3
path["B"]["end"] = 5

path["end"] = {}

inf = float("inf")
costs = {}
costs["A"] = 6
costs["B"] = 2
costs["end"] = inf

fathers = {"A": "start", "B" : "start", "end" : None}
process = []

def find_lowest_cost(cost):
    custo_mais_baixo = inf
    nodo_custo_mais_baixo = None
    for nodo in costs:
        custo = costs[nodo]
        if custo < custo_mais_baixo and nodo not in process:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

def find_best_path():
    node = find_lowest_cost(costs)
    while node is not None:
        custo = costs[node]
        vizinhos = path[node]
        for n in vizinhos.keys():
            new_custo = custo + vizinhos[n]
            if costs[n] > new_custo:
                costs[n] = new_custo
                fathers[n] = node
        process.append(node)
        node = find_lowest_cost(costs)
        

print(find_best_path)