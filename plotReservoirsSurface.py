import os
import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import sys
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)   # using a vector graphics extension (more suitable for LaTeX figures)
plt.rcParams.update({
    "text.usetex": True,  # LaTeX style of text (math with $$) formatting,
    "pgf.rcfonts": False,
    "pgf.texsystem": "pdflatex",
})


def getPlottingData(file_name, column_index):
    axis = []
    with open('../python_plots/plot_data/surface_data/' + file_name + ".csv") as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            try:
                axis.append(float(row[column_index]))
            except ValueError:  # skip invalid lines
                continue
    return axis


input_file_name = "Mackey-Glass Time Series using Cyclic with Jumps topology"  # test
output_image_name = "testReservoirSurface"
x_label = "$N_{\\mathrm{x}}$"
y_label = "$\\rho$"
z_label = "$\\overline{MSE}$"
title = "Reservoir Surface Plot Test"
plot_type = "-"

# print("args num.: " + len(sys.argv).__str__())
# print(sys.argv)
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
    output_image_name = sys.argv[2]  # same as title
    title = sys.argv[2]
if len(sys.argv) > 3:
    x_label = sys.argv[4]
    y_label = sys.argv[5]
    z_label = sys.argv[6]
    plot_type = sys.argv[7]

x = []
y = []

plt.xlabel(x_label)
plt.ylabel(y_label)

x = getPlottingData(input_file_name, 0)
y = getPlottingData(input_file_name, 1)
z = getPlottingData(input_file_name, 2)
z_off = getPlottingData(input_file_name, 3)

fig = plt.figure(1)
ax = fig.gca(projection='3d')

# x, y, z = np.meshgrid(x, y, z)
# x = np.reshape(x, (10,50))
# y = np.reshape(y, (10,50))
# z = np.reshape(z, (10,50))
# z = np.outer(z,z)
# x = np.array(x)
# y = np.array(y)
# z = np.array(z)
# x = x.flatten()
# y = y.flatten()
# z = z.flatten()
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)
ax.set_zlabel(z_label)
ax.set_title(title)
# ax.plot_surface(x, y, z, cmap=cm.coolwarm)
# ax.plot_trisurf(x, y, z, cmap=cm.coolwarm)
# ax.scatter(x, y, z, cmap=cm.jet)
ax.scatter(x, y, z, c=z)

# plt.legend()
plotsPath = "../python_plots/plots/surfaces/"
fig.savefig(plotsPath + output_image_name + ".pdf")
# plt.show()  # blank when using pgf

# plot the offline MSE
fig = plt.figure(2)
ax = fig.gca(projection='3d')
# # ax.set_xlabel(x_label)
# # ax.set_ylabel(y_label)
# # ax.set_zlabel(z_label)
ax.set_title(title + ' (Offline)')
ax.scatter(x, y, z_off, c=z_off)
fig.savefig(plotsPath + output_image_name + " (Offline).pdf")

plt.show()  # blank when using pgf
