def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            if n in graph:
                cur_graph = graph[n]
                for p in path:
                    if p in cur_graph:
                        cur_graph.remove(p)
                for m in graph[n]:
                    queue.append((m, path + [m]))
    return result


depar = 'SEOUL'
hub = 'DAEGU'
dest = 'YEOSU'
# roads = [['SEOUL', "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "ULSAN"],
#          ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]

roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]


_graph = dict()
for a, b in roads:
    if a in _graph:
        _graph[a].append(b)
    else:
        _graph[a] = [b]
start_hub = len(bfs_paths(_graph, depar, hub))
hub_dest = len(bfs_paths(_graph, hub, dest))
print(start_hub * hub_dest)
