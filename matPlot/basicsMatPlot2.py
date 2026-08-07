import matplotlib.pyplot as plt
import numpy as np

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([500, 470, 430, 520, 600, 750 ])
y2 = np.array([300, 170, 130, 520, 700, 950 ])

lineStyle = dict(marker = ".", 
                markersize = 20, 
                markerfacecolor = "#3de609",
                markeredgecolor = "000000", 
                linestyle = "solid", 
                linewidth = 3, 
                color = "#7a0b0b")

plt.plot(x, y, **lineStyle)
plt.plot(x,y2, **lineStyle)

plt.show()

