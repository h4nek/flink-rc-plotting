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


inputs_file_name = "test"
outputs_file_name = "test"
output_image_name = "testLRFit"
input_index = 1
x_label = "x"
y_label = "y"
title = "Linear Regression Test"
plot_type = "-"

# print("args num.: " + len(sys.argv).__str__())
# print(sys.argv)
if len(sys.argv) > 1:
    inputs_file_name = sys.argv[1]
    outputs_file_name = sys.argv[2]
    output_image_name = sys.argv[3]
    input_index = int(sys.argv[4])
    x_label = sys.argv[5]
    y_label = sys.argv[6]
    title = sys.argv[7]
    plot_type = sys.argv[8]

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

x = getPlottingData(inputs_file_name, input_index)
y = getPlottingData(outputs_file_name, 1)
plt.plot(x, y, ".", label="real data")

y = getPlottingData(outputs_file_name, 2)
if y:   # online predictions
    plt.plot(x, y, plot_type, label=predictionsLabel + " (online)")

y = getPlottingData(outputs_file_name, 3)
if y:   # offline predictions
    plt.plot(x, y, plot_type, label=predictionsLabel + " (offline)")

plt.title(title)
plt.legend()
plotsPath = "../python_plots/plots/"
plt.savefig(plotsPath + output_image_name + ".pdf")
# plt.show()  # blank when using pgf
