class LCGenerator:
    def __init__(self, initial_value, a=445, c=700001, m=2097152):
        super().__init__()
        self.a = a
        self.c = c
        self.m = m
        self.current = initial_value

    def next(self):
        result = (self.a * self.current + self.c) % self.m
        self.current = result
        return result


class GraphGenerator:
    def __init__(self, generator, node_number):
        self.node_number = node_number
        self.random_generator = generator
        self.graph = dict()

    def get_next_number(self):
        return self.random_generator.next() % self.node_number + 1

    def weight_of(self, a, b):
        if a not in self.graph or b not in self.graph:
            return -1
        for edge in self.graph[a]:
            if edge[0] == b:
                return edge[1]
        return -1

    def build(self):
        for i in range(1, self.node_number + 1):
            v1 = self.get_next_number()
            d1 = self.get_next_number()
            v2 = self.get_next_number()
            d2 = self.get_next_number()

            if i != v1 and self.weight_of(i, v1) == -1:
                if i in self.graph:
                    self.graph[i].append((v1, d1))
                else:
                    self.graph[i] = [(v1, d1)]
                if v1 in self.graph:
                    self.graph[v1].append((i, d1))
                else:
                    self.graph[v1] = [(i, d1)]

            if i != v2 and self.weight_of(i, v2) == -1:
                if i in self.graph:
                    self.graph[i].append((v2, d2))
                else:
                    self.graph[i] = [(v2, d2)]
                if v2 in self.graph:
                    self.graph[v2].append((i, d2))
                else:
                    self.graph[v2] = [(i, d2)]

        return self.graph


if __name__ == "__main__":
    with open('C:/cygwin64/home/ipatrikeev/input.txt') as f:
        node_number, start_value = [int(x) for x in f.readline().split()]
        generator = LCGenerator(start_value)
        graph_generator = GraphGenerator(generator, node_number)

        graph = graph_generator.build()

        for vertex in graph.keys():
            weight = 0
            for edge in graph[vertex]:
                weight += edge[1]
            print(weight, end=' ')
