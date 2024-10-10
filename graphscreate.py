import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2020, 2022, 2024, 2025])
grades = np.array([55.5 , 83, 65, 72])

#show data in graph ->  line (x,y) ,pie(x), bar(x,y) , scatters(x,y)

plt.plot(years, grades)
plt.show()