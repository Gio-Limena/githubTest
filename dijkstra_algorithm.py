import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    previous = {}
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path = []
    current = end
    while current in previous:
        path.insert(0, current)
        current = previous[current]
    path.insert(0, start)
    
    return distances[end], path

graph = {}
with open("map.txt", "r") as file:
    for line in file:
        start, end, weight = line.split()
        weight = int(weight)
        
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        
        graph[start][end] = weight
        graph[end][start] = weight

start_node = 'WE'
end_node = 'W-304'
distance, path = dijkstra(graph, start_node, end_node)

print(f"Distance from {start_node} to {end_node}: {distance} Seconds")
print("To get to your final destination, You should take the Path:", "->".join(path))

