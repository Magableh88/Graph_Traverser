#Mohammad Makableh
#202130654
from graph import Graph

def find_high_degree(graph, vertex):
   """
   Traverses the graph starting from vertex to look for high degree nodes.

   graph is an object of the Graph class.
   vertex is a vertex in the graph, and an object of the Vertex class.

   See algorithm find_high_degree() in the assignment instructions.

   Returns the vertex with the highest degree that was found during the
   traversal.
   """

   #keeps track of visited vertices and sets initial vertex as max
   visited = set()
   max_vertex = vertex

   while True:
       #list to keep track of neighboring vertices and which ones are visited
       neighbors = [n for n in graph.incident_edges(vertex)]
       unvisited = [edge.opposite(vertex) for edge in neighbors if edge.opposite(vertex) not in visited]

       # Exit the loop if no unvisited neighbors are found
       if not unvisited:
           break

       # finds the highest degree neighbor
       highest_degree = max(unvisited, key=lambda v: graph.degree(v))

       #updates the vertex with the max degree
       if graph.degree(max_vertex) < graph.degree(highest_degree) :
           max_vertex = highest_degree

       #marks the vertex visited
       visited.add(vertex)
       #traverse to next vertex
       vertex = highest_degree
   #return the vertex when found
   return max_vertex



# example usage
G = Graph()

a = G.insert_vertex('a')
b = G.insert_vertex('b')
c = G.insert_vertex('c')
d = G.insert_vertex('d')

G.insert_edge(a, b)
G.insert_edge(b, c)
G.insert_edge(c, a)
G.insert_edge(c, d)

# search G starting from a
vertex = find_high_degree(G, a)  # should return vertex c
print(vertex._element)
