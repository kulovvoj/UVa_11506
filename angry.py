# Will use Ford-Fulkerson and for that I need to split each vertex into 2, one with outgoing and one with incoming edges.
# Edge between split vertices will be directed from incoming vertex to outgoing vertex and will have value of vertex removal.

def BFS(M, residual, parent):
    visited = [False] * M * 2
    queue = []

    # We add the outgoing starting node to the queue
    queue.append(M)
    visited[M] = True

    while (queue):
        current = queue.pop(0)

        for vertex, cost in enumerate(residual[current]):
            if (visited[vertex] == False and cost > 0):
                if (vertex == M - 1):
                    parent[vertex] = current
                    return True
                queue.append(vertex) 
                visited[vertex] = True
                parent[vertex] = current

    return False

def ford_fulkerson(residual, M):
    parent = [-1] * M * 2
    max_flow = 0
    while (BFS(M, residual, parent)):
        path_flow = 10000000000
        vertex = M - 1
        while (vertex != M):
            path_flow = min(path_flow, residual[parent[vertex]][vertex])
            vertex = parent[vertex]
        
        max_flow += path_flow

        vertex = M - 1
        while (vertex != M):
            residual[parent[vertex]][vertex] -= path_flow
            residual[vertex][parent[vertex]] += path_flow
            vertex = parent[vertex]

    return max_flow

def main():
    M, W = map(int, input().split())
    while (M != 0 or W != 0):
        # Splitting the vertices gives us twice their number
        residual = [[0 for i in range(2 * M)] for j in range(2 * M)]
        # Weight of the split of first and last vertex is virtually infinite
        residual[0][M] = residual[M - 1][2 * M - 1] = 10000000000 

        for i in range(M - 2):
            node, cost = map(int, input().split())
            residual[node - 1][M + node - 1] = cost

        for i in range(W):
            node1, node2, cost = map(int, input().split())
            residual[M + node1 - 1][node2 - 1] = cost
            residual[M + node2 - 1][node1 - 1] = cost

        print(ford_fulkerson(residual, M))
        M, W = map(int, input().split())

main()