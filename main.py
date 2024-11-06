from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    path_info = {node: (float('inf'), float('inf')) for node in graph}
    path_info[source] = (0, 0)  
    min_heap = [(0, 0, source)]  
    while min_heap:
        current_weight, current_edges, current_node = heappop(min_heap)
        if (current_weight, current_edges) > path_info[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            updated_weight = current_weight + weight
            updated_edges = current_edges + 1
            if (updated_weight < path_info[neighbor][0]) or \
               (updated_weight == path_info[neighbor][0] and updated_edges < path_info[neighbor][1]):
                path_info[neighbor] = (updated_weight, updated_edges)
                heappush(min_heap, (updated_weight, updated_edges, neighbor))
    return path_info
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent_map = {source: None}  
    to_visit = deque([source])   
    while to_visit:
        current = to_visit.popleft()
        for neighbor in graph[current]:
            if neighbor not in parent_map:
                parent_map[neighbor] = current
                to_visit.append(neighbor)

    return parent_map

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination

    while parents[current] is not None:
        path.append(parents[current])
        current = parents[current]

    return ''.join(path[::-1]) 

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'


test_shortest_shortest_path()
test_bfs_path()
test_get_path()
