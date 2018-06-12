import romania
import sys

""" This class finds the shortest route between any 2 given unique vertices, i.e: cities in this case, using Breadth First Search """
class find_route:
    def findRoute(self):
        fileInput = sys.argv[1] 
        dest1 = sys.argv[2]     #First Destination
        dest2 = sys.argv[3]     #Second Destination
        totalDistance = 0   #Cumilative Distance
        stack = []

        #Get Graphical representation of unique vertices and thier respective weights
        biDirGraph = romania.romania(0).getDataRomania(fileInput) 

        graph = biDirGraph[0]
        vertices = biDirGraph[1]
        visited = [False] * vertices

        for i in range(vertices):
            if visited[i] == False:
                #Traverse the graph and mark vertices as 'Visited' according to levels
                self.sort(graph, dest1, visited, stack)
            #endif
        #endfor
        dist = [float("Inf")] * vertices    #Total Distance From Destination 1 to all vertices
        dist[graph.keys().index(dest1)] = 0.0
        fromCity = [0] * vertices   #Destination 1 or via vertices
        toCity = [0] * vertices     #Destination 2 or via vertices
        toFroDist = [0] * vertices  #Distance between internal vertices, i.e: city to city till Destination 2

        while stack:
            pos = stack.pop()   #Get each vertex(city) according to levels
            for destination, distance in graph[pos]:
                #Distance between starting or intermediate vertex and adjacent vertex
                cumilativeDistance = float(dist[graph.keys().index(pos)]) + float(distance)

                #Checks if weight of vertex exceeds cumilative path weight, in this case distances between vertices
                if float(dist[graph.keys().index(destination)]) > cumilativeDistance:
                    dist[graph.keys().index(destination)] = cumilativeDistance
                    fromCity[graph.keys().index(destination)] = pos
                    toCity[graph.keys().index(destination)] = destination
                    toFroDist[graph.keys().index(destination)] = float(distance)

                    if destination == dest2:
                        totalDistance = cumilativeDistance
                    #endif
                #endif
            #endfor
        #endwhile
        pos = 0
        returnStr = []
        finalDist = totalDistance

        #Get individual distances between adjacent nodes from Destination 1 to Destination 2
        while totalDistance != 0:
            if toCity[pos] == dest2:
                    returnStr.append(fromCity[pos])
                    returnStr.append(toCity[pos])
                    returnStr.append(str(toFroDist[pos]))
                    totalDistance = dist[pos] - toFroDist[pos]
                    dest2 = fromCity[pos] #Via node
                    pos = 0
            else:
                pos = pos + 1
            #endif
        #endwhile

        #Bottom-Up traversal
        returnStr.reverse()

        #Print the paths
        if finalDist == 0:
            pathStr = "distance: infinity\nroute:\nnone\n"
        else:
            pathStr = "distance: " + str(finalDist) + " km\n" + "route:\n"
            pos = 0
            while pos < len(returnStr):
                pathStr += returnStr[pos + 2] + " to " + returnStr[pos + 1] + ", " + returnStr[pos] + " km\n"
                pos = pos + 3
        #endif
        print pathStr
    #endmethod

    #Traverse the graph and mark vertices as 'Visited' according to levels
    def sort(self, graph, dest1, visited, stack):
        visited[graph.keys().index(dest1)] = True
        if dest1 in graph.keys():
            for d, distance in graph[dest1]:
                if visited[graph.keys().index(d)] == False:
                    self.sort(graph, d, visited, stack)
                #endif
            #endfor
        #endif
        stack.append(dest1)
    #endmethod

#Main method
def main():
    obj = find_route()
    obj.findRoute()
#endmethod

if __name__ == "__main__":
    main()