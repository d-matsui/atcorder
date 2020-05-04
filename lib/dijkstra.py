def dijkstra(n_nodes, edges, start):
    que = deque()
    dist = [INF] * n_nodes
    dist[start] = 0
    que.append([start, 0])
    while len(que) > 0:
        v, v_cost = que.popleft()
        if dist[v] < v_cost:
            continue
        for u, u_cost in edges[v]:
            if v_cost + u_cost < dist[u]:
                dist[u] = v_cost + u_cost
                que.append([u, dist[u]])
    return dist
