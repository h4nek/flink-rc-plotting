import os
import matplotlib.pyplot as plt
import csv
import numpy as np
import math
import sys
import matplotlib as mpl
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)   # using a vector graphics extension (more suitable for LaTeX figures)
# mpl.use("pgf")  # using a vector graphics extension (more suitable for LaTeX figures)
plt.rcParams.update({
    "text.usetex": True,  # LaTeX style of text (math with $$) formatting,
    "pgf.rcfonts": False,
    "pgf.texsystem": "pdflatex",
})


def getPlottingData(file_name, column_index):
    axis = []
    with open('../python_plots/plot_data/' + file_name + ".csv") as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            if len(row) <= column_index:    # the column is either not present or corrupt
                return []
            try:
                axis.append(float(row[column_index]))
            except ValueError:  # skip invalid lines
                continue
    return axis


input_file_name = "test"
output_image_name = "testRCFit"
x_label = "x"
y_label = "y"
title = "RC Plot Test"
plot_type = "-"

if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
    output_image_name = sys.argv[2]
    x_label = sys.argv[3]
    y_label = sys.argv[4]
    title = sys.argv[5]
    plot_type = sys.argv[6]

plt.xlabel(x_label)
plt.ylabel(y_label)

if title.endswith("LR"):
    if plot_type == "-":
        predictionsLabel = "linear predictor function"
    else:
        predictionsLabel = "LR fit"
else:
    if plot_type == "-":
        predictionsLabel = "predictor function"
    else:
        predictionsLabel = "RC fit"

x = getPlottingData(input_file_name, 1)
y = getPlottingData(input_file_name, 2)
plt.plot(x, y, ".", label="real data")

y = getPlottingData(input_file_name, 3)
if y:   # online predictions
    plt.plot(x, y, plot_type, label=predictionsLabel + " (online)")

y = getPlottingData(input_file_name, 4)
if y:   # offline predictions
    plt.plot(x, y, plot_type, label=predictionsLabel + " (offline)")

plt.title(title)
plt.legend()
plotsPath = "../python_plots/plots/"
plt.savefig(plotsPath + output_image_name + ".pdf")
# plt.show()  # blank when using pgf
