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


input_file_name = "Analyzing spectral radius using Mackey-Glass Time Series"  # test
output_image_name = "testReservoirPerformance"
folder = "hyperparameter_performance/"
x_label = "$N_{\\mathrm{x}}$"
y_label = "$\\rho$"
title = "Reservoir Performance Plot Test"
plot_type = "-"
n_values_per_measurement = 4
n_measurements = 1
is_x_numeric = True

if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
    output_image_name = sys.argv[2]  # same as title
    title = sys.argv[2]
    folder = sys.argv[3]
if len(sys.argv) > 4:
    x_label = sys.argv[4]
    y_label = sys.argv[5]
    plot_type = sys.argv[6]
if len(sys.argv) > 7:
    n_values_per_measurement = int(sys.argv[7])
    n_measurements = int(sys.argv[8])
if len(sys.argv) > 9:
    is_x_numeric = True if sys.argv[9] == "true" else False

input_file_path = folder + input_file_name

data = csv.reader(open('../python_plots/plot_data/' + input_file_path + ".csv"))
data = np.array(list(data))

plt.xlabel(x_label)
plt.ylabel(y_label)

for i in range(n_measurements):
    start = i*n_values_per_measurement
    stop = start + n_values_per_measurement
    measurement_data = data[start:stop]
    x = [float(x) if is_x_numeric else x for (x,y) in measurement_data]
    y = [float(y) for (x,y) in measurement_data]
    plt.plot(x, y, plot_type)

plt.title(title)
plotsPath = "../python_plots/plots/" + folder
plt.savefig(plotsPath + output_image_name + ".pdf")
# plt.show()  # blank when using pgf
