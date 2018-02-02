#dictionary used to hold the graph with distances between nodes
#Code snippet extracted from Python 'collections' module
#Since 'defaultdict' module only works on Python version 2.5x and higher
def defaultdict(default_type):
    class DefaultDict(dict):
        def __getitem__(self, key):
            if key not in self:
                dict.__setitem__(self, key, default_type())
            return dict.__getitem__(self, key)
    return DefaultDict()
#endmethod

class romania:
    """description of class romania: 
    This class reads the input.txt file that holds the various bi-directional distances between various nodes ont the graph which is the map of the contry Romania where each node is a city."""
    #Creates new dictionary for graph
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
    #endmethod

    #Read each line from given file containing node names and weights and induce into a graph
    def getDataRomania(self, fileInput):
        file1 = open(fileInput, "r")   #Read file
        cityList = []
        for data in file1.read().split():
            if(data == "END"):
                break
            #Get list of all unique nodes
            if data not in cityList:
                if data.isdigit() == False:
                    cityList.append(data)
                #endif
            #endif
        #endfor
        file1 = open(fileInput, "r")   #Read file
        romaniaGraph = romania(len(cityList))   #Number of nodes in graph
        cityList = []
        for data in file1.read().split():
            if(data == "END"):
                break
            cityList.append(data)
            if len(cityList) == 3:
                city1 = cityList[0]
                city2 = cityList[1]
                distance = cityList[2]
                #Bidirectional graph
                romaniaGraph.addEdges(city1, city2, distance)
                romaniaGraph.addEdges(city2, city1, distance)
                cityList = []
            #endif
        #endfor
        return romaniaGraph.graph, romaniaGraph.vertices
    #endmethod

    # Graph with the edges representing unique nodes and distances between each node
    def addEdges(self, fromloc, toloc, distance):
        self.graph[fromloc].append((toloc, distance))
    #endmethod





