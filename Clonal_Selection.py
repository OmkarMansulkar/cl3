import numpy as np

def f(x):
    return x*np.sin(10*np.pi *x)+1


pop=np.random.uniform(-1,2,20)

for _ in range(100):
    scores=f(pop)
    top=pop[scores.argsort()][-10:]
    clones=[x+np.random.normal(0,0.2) for x in top for _ in range(5)]
    pop=np.clip(clones,-1,2)

best_x=pop[np.argmax(f(pop))]
print(f"Best x is: {best_x}, f(x) is: {f(best_x)}")
