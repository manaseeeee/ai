from queue import PriorityQueue

GRAPH = {
    'Delhi': {'Jaipur': 280, 'Agra': 210, 'Lucknow': 400},
    'Agra': {'Delhi': 210, 'Gwalior': 120},
    'Gwalior': {'Agra': 120, 'Bhopal': 400},
    'Jaipur': {'Delhi': 280, 'Jodhpur': 330, 'Udaipur': 410},
    'Lucknow': {'Delhi': 400, 'Kanpur': 80},
    'Kanpur': {'Lucknow': 80, 'Allahabad': 190},
    'Allahabad': {'Kanpur': 190, 'Varanasi': 120},
    'Varanasi': {'Allahabad': 120, 'Patna': 250},
    'Patna': {'Varanasi': 250, 'Ranchi': 300, 'Kolkata': 560},
    'Ranchi': {'Patna': 300, 'Jamshedpur': 130},
    'Jamshedpur': {'Ranchi': 130, 'Kolkata': 280},
    'Kolkata': {'Patna': 560, 'Jamshedpur': 280, 'Bhubaneswar': 440},
    'Bhubaneswar': {'Kolkata': 440, 'Cuttack': 30, 'Puri': 60},
    'Puri': {'Bhubaneswar': 60},
    'Cuttack': {'Bhubaneswar': 30},
    'Jodhpur': {'Jaipur': 330, 'Udaipur': 250},
    'Udaipur': {'Jaipur': 410, 'Jodhpur': 250, 'Ahmedabad': 260},
    'Ahmedabad': {'Udaipur': 260, 'Surat': 280},
    'Surat': {'Ahmedabad': 280, 'Mumbai': 280},
    'Mumbai': {'Surat': 280, 'Pune': 150},
    'Pune': {'Mumbai': 150}
}

def bestfirst(source, destination):
    straight_line = {
        'Delhi': 1400, 'Jaipur': 1200, 'Agra': 1300, 'Lucknow': 1100, 'Kanpur': 1050,
        'Allahabad': 900, 'Varanasi': 850, 'Patna': 600, 'Gwalior': 1200, 'Bhopal': 1000,
        'Ranchi': 500, 'Jamshedpur': 300, 'Kolkata': 0, 'Bhubaneswar': 450, 'Puri': 510,
        'Cuttack': 440, 'Jodhpur': 1400, 'Udaipur': 1300, 'Ahmedabad': 1200, 'Surat': 1250,
        'Mumbai': 1600, 'Pune': 1550
    }

    priority_queue = PriorityQueue()
    priority_queue.put((straight_line[source], 0, source, [source]))

    visited = {source: 0}

    while not priority_queue.empty():
        heuristic, cost, vertex, path = priority_queue.get()

        if vertex == destination:
            return heuristic, cost, path

        for next_node, travel_cost in GRAPH.get(vertex, {}).items():
            new_cost = cost + travel_cost
            if next_node not in visited or new_cost < visited[next_node]:
                visited[next_node] = new_cost
                priority_queue.put((straight_line[next_node], new_cost, next_node, path + [next_node]))

    return None

def main():
    print('ENTER SOURCE :', end=' ')
    source = input().strip()
    print('ENTER GOAL :', end=' ')
    goal = input().strip()

    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nBest First Search PATH:')
        result = bestfirst(source, goal)

        if result:
            heuristic, cost, optimal_path = result
            print('PATH COST =', cost)
            print(' -> '.join(optimal_path))
        else:
            print("No path found from {} to {}".format(source, goal))

if __name__ == '__main__':
    main()
