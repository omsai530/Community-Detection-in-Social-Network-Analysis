import time
st=time.time()
'''graph={'a':{'b':3,'d':7,'c':4},
       'b':{'c':1,'f':5,'a':3},
       'c':{'f':6,'d':2,'a':4,'b':1},
       'd':{'e':3,'g':6,'a':7,'c':2},
       'e':{'g':3,'h':4,'d':3,'f':1},
       'f':{'e':1,'h':8,'c':6,'b':5},
       'g':{'h':2,'d':6,'e':3},
       'h':{'f':8,'e':4,'g':3}
       }
'''
graph={'a':{'b':10,'d':9,'e':2},
       'b':{'f':10,'a':10},
       'd':{'f':3,'a':13},
       'e':{'f':100,'a':2},
       'f':{'b':10,'d':11,'e':100}
      }
unseen_nodes=graph
shortdis_node={}
inf=999999
path_lst=[]
track={}

def dijkstra(graph,start,goal):
   
   for node in unseen_nodes:
      shortdis_node[node]=inf
   shortdis_node[start]=0
   print(shortdis_node)

   while unseen_nodes:
      
      pointer=None
      for node in unseen_nodes:
         if pointer is None:
            pointer=node
         elif shortdis_node[node]<shortdis_node[pointer]:
            pointer=node
      print(pointer)
         
      for child,wei in graph[pointer].items():
         if wei+shortdis_node[pointer]<shortdis_node[child]:
            shortdis_node[child]=wei+shortdis_node[pointer]
            track[child]=pointer
            
      unseen_nodes.pop(pointer)
      
   currnode=goal
   while currnode!=start:
      
      try:
         path_lst.insert(0,currnode)
         currnode=track[currnode]
         
      except KeyError:
         print("path not Found")
         break
      
   path_lst.insert(0,start)
   if shortdis_node[goal]!=inf:
      print("Shortest Distensce ",start,"Between",goal,"is",shortdis_node[goal])
      print("Shortest Path is :",path_lst)
   
dijkstra(graph,'a','f')

et=time.time()
print(et-st)
