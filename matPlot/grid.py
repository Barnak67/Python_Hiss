import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.grid(axis = "both", linewidth = 2, 
        color = "green",
        linestyle = "dotted")

plt.plot(x,y, color = "black")

plt.show()