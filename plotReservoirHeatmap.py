import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import sys
# import matplotlib as mpl
# from matplotlib.backends.backend_pgf import FigureCanvasPgf
# mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)   # using vector graphics (more suitable for LaTeX figures)


# title = "W_jumps_only"
if len(sys.argv) > 1:   # invoked from outside with params
    title = sys.argv[1]
    # range = float(sys.argv[2])

# data = np.random.rand(4, 6)
data = np.genfromtxt('../python_plots/plot_data/heatmap_data/' + title + '.csv', delimiter=',')
# print(data)

# plt.style.use('seaborn-darkgrid')

# plain matplotlib
# plt.imshow(data, cmap='viridis')
# plt.colorbar()

# seaborn
# heatmap = sb.heatmap(data, linewidths=.5, linecolor='black')
heatmap = sb.heatmap(data, vmin=-0.5, vmax=0.5, cmap='RdBu')
plt.title(title)

# plt.legend()
plotsPath = "../python_plots/plots/heatmaps/"
plt.savefig(plotsPath + title.replace(" ", "_") + ".pdf")
plt.show()
