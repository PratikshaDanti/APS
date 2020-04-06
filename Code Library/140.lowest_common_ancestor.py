import queue
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

def creatSparse(max_node, parent):
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent

def LCA(u, v, level, parent):
    if level[u] < level[v]:
        u, v = swap(u, v)
    for i in range(18, -1, -1):
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]
    if u == v:
        return u
    for i in range(18, -1, -1):
        if parent[i][u] != 0 and parent[i][u] != parent[i][v]:
            u, v = parent[i][u], parent[i][v]
    return parent[0][u]

def bfs(level, parent, max_node, graph, root=1):
    level[root] = 0
    q = queue.Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.put(v)
                parent[0][v] = u
    return level, parent

def main():
    max_node = 13
    parent = [[0 for _ in range(max_node + 10)] for _ in range(20)]
    level = [-1 for _ in range(max_node + 10)]
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [6, 7],
        4: [8],
        5: [9, 10],
        6: [11],
        7: [],
        8: [12, 13],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
    }
    level, parent = bfs(level, parent, max_node, graph, 1)
    parent = creatSparse(max_node, parent)
    print("LCA of node 1 and 3 is: ", LCA(1, 3, level, parent))
    print("LCA of node 5 and 6 is: ", LCA(5, 6, level, parent))
    print("LCA of node 7 and 11 is: ", LCA(7, 11, level, parent))
    print("LCA of node 6 and 7 is: ", LCA(6, 7, level, parent))
    print("LCA of node 4 and 12 is: ", LCA(4, 12, level, parent))
    print("LCA of node 8 and 8 is: ", LCA(8, 8, level, parent))

if __name__ == "__main__":
    main()
