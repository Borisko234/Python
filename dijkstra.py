class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes

        for edge in edgesToVertexes:
            for v in vertexes:
                if v.id == edge.source:
                    v.edges.append(edge)

    def computePath(self, sourceId):

        for v in self.vertexes:
            if v.id == sourceId:
                currentVertex = v
        currentVertex.minDistance = 0

        path = [currentVertex]

        while path:
            sorted = False
            while not sorted:
                sorted = True
                for i in range(len(path)-1):
                    if path[i].minDistance > path[i+1].minDistance:
                        path[i], path[i+1] = path[i+1], path[i]
                        sorted = False
            currentVertex = path.pop(0)

            for edge in currentVertex.edges:
                for v in self.vertexes:
                    if v.id == edge.target:
                        target = v

                        new_path = currentVertex.minDistance + edge.weight

                        if new_path < target.minDistance:
                            target.minDistance = new_path
                            target.previousVertex = currentVertex

                            if target not in path:
                                path.append(target)
                            
       
    def getShortestPathTo(self, targetId):
        
        for v in self.vertexes:
            if v.id == targetId:
                target = v
                break

        path = []
        while target is not None:
            path.insert(0, target)
            target = target.previousVertex
        return path



    def resetDijkstra(self):
        for v in self.vertexes:
            v.minDistance = float('inf')
            v.previousVertex = None

    def getVertexes(self):
        return self.vertexes

