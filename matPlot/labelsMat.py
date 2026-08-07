import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([500, 470, 430, 520, 600, 750 ])
y2 = np.array([300, 170, 130, 520, 700, 950 ])
y3 = np.array([300, 400, 500, 600, 700, 1000 ])

plt.title("Student Strength", fontsize = 20,
                family = "Arial", fontweight = "bold", color = "blue")

plt.xlabel("Year", fontsize = 15,
        family = "Arial", fontweight = "bold", color = "green" )

plt.ylabel("Students", fontsize = 15,
        family = "Arial", fontweight = "bold", color = "green" )

lineStyle = dict(marker = ".", 
                markersize = 20, 
                markerfacecolor = "#3de609",
                markeredgecolor = "000000", 
                linestyle = "solid", 
                linewidth = 3)

plt.tick_params(axis="both", colors= "#5e2b06")

plt.plot(x, y, **lineStyle, color = "#7a0b0b")
plt.plot(x,y2, **lineStyle, color = "#0b7a69")
plt.plot(x,y3, **lineStyle, color = "#9015e8")

plt.xticks(x)

plt.show()

