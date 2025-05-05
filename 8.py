import random

server=[0,0,0,0]
index=0

def choose_server(algo):
    global index
    if algo=="round_robin":
        s=index
        index=(index+1)%len(server)
    elif algo=="least_connections":
        s=server.index(min(server))
    elif algo=="random":
        s=random.randint(0,len(server)-1)
    else:
        raise ValueError("Invalid Algorithm Name")
    server[s]+=1
    return s

alg=input("Whih load balancing algorithm do you want to move forward with (round_robin,least_connections,random):")
for _ in range(20):
    sid=choose_server(alg)
    print(f"Server {sid} was chosen")
    
print("Final Serve load")
for i,load in enumerate(server):
    print(f"Server {i} Load: {load}")