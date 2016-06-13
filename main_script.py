class TopologicalSort:
    def __init__(self, graph):
        self.temp_marked = set()
        self.permanent_marked = set()
        self.result = []
        self.graph = graph
        self.unmarked = list(self.graph.keys())

    def sort(self):
        while len(self.unmarked) > 0:
            unmarked_node = self.unmarked.pop()
            self.visit(unmarked_node)
        return self.result

    def visit(self, node):
        if node in self.temp_marked:
            raise ValueError('Not a DAG graph')
        if node not in self.permanent_marked:
            self.temp_marked.add(node)
            for m in graph[node]:
                self.visit(m)
            self.permanent_marked.add(node)
            self.temp_marked.remove(node)
            self.result.insert(0, node)


if __name__ == "__main__":
    graph = dict()
    with open('C:/cygwin64/home/ipatrikeev/input.txt') as f:
        n = int(f.readline())
        for i in range(n):
            a, b = f.readline().split()
            if a in graph:
                graph[a].add(b)
            else:
                graph[a] = set()
                graph[a].add(b)
            if b not in graph:
                graph[b] = set()

    tp_sort = TopologicalSort(graph)
    print(' '.join(tp_sort.sort()))
