from graph_breadth_first import Graph

def graph_business_trip(graph, arr):
    trip_total = 0
    incrementer = 2
    can_connect = False

    if graph.size() < 2:
        cant_connect = [can_connect, '$0']
        return cant_connect
    elif len(arr) < 2:
        cant_connect = [can_connect, '$0']
        return cant_connect
    departure = arr[0]
    arrival = arr[1]

    while arrival is not None:
        can_connect = False
        connections = graph.get_neighbors(departure)
        if len(connections) > 0:
            for city in range(len(connections)):
                if connections[city].end_vert.value == arrival:
                    can_connect = True
                    trip_total += connections[city].weight
                    departure = arrival
                elif city == len(connections) - 1 and can_connect == False:
                    cant_connect = [can_connect, '$0']
                    return cant_connect
            try:
                arrival = arr[incrementer]
                incrementer = incrementer + 1
            except:
                arrival = None

        else:
            cant_connect = [can_connect, '$0']
            return cant_connect
    total = [can_connect, f'${trip_total}']
    return total
