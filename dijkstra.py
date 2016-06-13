from graph_generator import LCGenerator, GraphGenerator


def dist_between(graph, a, b):
    distances = graph[a]
    for d in distances:
        if d[0] == b:
            return d[1]
    return -1


def get_min(dist, vert):
    min = None
    for v in vert:
        if min is None and v in dist:
            min = v
        else:
            if v in dist and dist[v] < dist[min]:
                min = v
    return min


def dijkstra_search(graph, start):
    dist = {start: 0}
    process_queue = set(graph.keys())
    while len(process_queue) > 0:
        min = get_min(dist, process_queue)
        process_queue.remove(min)
        for neighbour in graph[min]:
            if neighbour[0] in process_queue:
                alt = dist[min] + dist_between(graph, min, neighbour[0])
                if neighbour[0] not in dist or dist[neighbour[0]] > alt:
                    dist[neighbour[0]] = alt

    return dist


if __name__ == "__main__":
    with open('C:/cygwin64/home/ipatrikeev/input.txt') as f:
        node_number, seed, start_value = [int(x) for x in f.readline().split()]
        generator = LCGenerator(seed)
        graph_generator = GraphGenerator(generator, node_number)

        graph = graph_generator.build()

        print(' '.join(str(x) for x in dijkstra_search(graph, start_value).values()))
