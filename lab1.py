import matplotlib
matplotlib.use("Agg")   # SAFE backend (no GUI)

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,2,4,4,8,7,4,8,10,9]

plt.plot(x, y)
plt.xlabel("time (s)")
plt.ylabel("temperature (deg C)")
plt.title("Temperature vs Time")

plt.savefig("graph.png")   # saves graph
print("Graph saved as graph.png")
