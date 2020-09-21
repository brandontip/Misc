

import math


def dijkstra(graph, start, goal):
    shortest_distance = {} # current cost to reach that node
    predecessor = {}  # helps keeps track of paths
    infinity =  math.inf

    # initialize distances
    unseen_vertices = graph.copy()
    for vertex in unseen_vertices:
            shortest_distance[vertex] = infinity
    shortest_distance[start] = 0  

    # core loop
    while unseen_vertices:
        # find next vertex to process
        min_distance_vertex = None
        for vertex in unseen_vertices:
            if min_distance_vertex is None:
                min_distance_vertex = vertex
            elif shortest_distance[vertex] < shortest_distance[min_distance_vertex]:
                min_distance_vertex = vertex
                
        # add paths to descendants, if short than existing       
        path_options = graph[min_distance_vertex].items()
        for descendant, weight in path_options:
            if weight + shortest_distance[min_distance_vertex] < shortest_distance[descendant]:
                shortest_distance[descendant] = weight + shortest_distance[min_distance_vertex]
                predecessor[descendant] = min_distance_vertex
                
        # done processing this vertex
        unseen_vertices.pop(min_distance_vertex)    
    

    # return results
    if shortest_distance[goal] != infinity:                 
        current_vertex = goal
        optimal_path = [] 
        while current_vertex != start:
            optimal_path.insert(0, current_vertex)
            current_vertex = predecessor[current_vertex]
        optimal_path.insert(0, start)    
        print("Shortest distance:" + str(shortest_distance[goal]))
        print("An optimal path:"+str(optimal_path))
    else:
        print("No path exists between vertices '"+start+"' and '"+goal+"'")
        
graph = {    
    'a': {'b':3,  'd':7},
    'b': {'a':3, 'c':4, 'd':7},
    'c': {'b':4, 'd':7},
    'd': {'a':7, 'b':7, 'c':7},   
    'e':{}    
    }
        
dijkstra(graph, 'a', 'c')

