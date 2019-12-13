# An Iterative Python program to do DFS traversal from  
# a given source vertex. DFS(int s) traverses vertices  
# reachable from s.  
  
# This class represents a directed graph using adjacency  
# list representation  
class Graph:  
    def __init__(self,V): # Constructor  
        self.V = V        # No. of vertices  
        self.adj  = {}
  
    def addEdge(self,v, w):     # to add an edge to graph 
        if v not in self.adj.keys():
            self.adj[v] = [w]
        else:
            self.adj[v].append(w)    # Add w to v’s list.  
  
  
    # prints all not yet visited vertices reachable from s  
    def DFS(self,s):            # prints all vertices in DFS manner from a given source. 
        print("ADJJJJ: ", self.adj)
        # Initially mark all verices as not visited  
        visited = self.adj.fromkeys(self.adj, False)  
        print("VISITED: ", visited)
  
        # Create a stack for DFS  
        stack = [] 
  
        # Push the current source node.  
        stack.append(s)  
  
        while (len(stack)):  
            # Pop a vertex from stack and print it  
            s = stack[-1]  
            stack.pop() 
            
            # Stack may contain same vertex twice. So  
            # we need to print the popped item only  
            # if it is not visited.  
            if (not visited[s]):  
                print(s,end=' ') 
                visited[s] = True 
  
            # Get all adjacent vertices of the popped vertex s  
            # If a adjacent has not been visited, then push it  
            # to the stack.  
            for node in self.adj[s]:
                print("NODEEE: ", node)
                if node == []:
                    break
                if (not visited[node]):  
                    stack.append(node)  
            print("VISITED: ", visited)
  
  
  
# Driver program to test methods of graph class  
  
g = Graph(6); # Total 5 vertices in graph  
g.addEdge(1, 3);  
g.addEdge(1, 2);  
g.addEdge(1, 4);  
g.addEdge(3, 5);  
g.addEdge(3, 6);
g.addEdge(2, []);
g.addEdge(4, []);
g.addEdge(5, []);
g.addEdge(6, []);

  
print("Following is Depth First Traversal")  
g.DFS(1)