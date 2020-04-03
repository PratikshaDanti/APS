def dfs(graph, start):
    explored, stack = set(), [start]
    while stack:
        v = (stack.pop()) 

        if v in explored:
            continue

        explored.add(v)

        for w in graph[v]:
            if w not in explored:
                stack.append(w)
    return explored


G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs(G, "A"))
