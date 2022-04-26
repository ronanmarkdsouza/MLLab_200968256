import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
sb.set_theme()

wine = pd.read_csv('wine.csv')
wine.head()

fig, axes = plt.subplots(2,7, figsize=(20,5))
fig.suptitle("Visualizing all the numerical variables")
sb.scatterplot(ax=axes[0,1], data=wine.Alcohol)
plt.subplot_tool()