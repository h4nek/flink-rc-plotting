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
            try:
                axis.append(float(row[column_index]))
            except ValueError:  # skip invalid lines
                continue
    return axis


inputs_file_name = "test"
outputs_file_name = "test"
predictions_file_name = "test"
output_image_name = "testLRFit"
input_index = 1
shift_data = 0
x_label = "x"
y_label = "y"
title = "Linear Regression Test"
plot_type = "-"
predictions_file_name = ""

# print("args num.: " + len(sys.argv).__str__())
# print(sys.argv)
if len(sys.argv) > 1:
    inputs_file_name = sys.argv[1]
    outputs_file_name = sys.argv[2]
    predictions_file_name = sys.argv[3]
    output_image_name = sys.argv[4]
    input_index = int(sys.argv[5])
    shift_data = int(sys.argv[6])
    x_label = sys.argv[7]
    y_label = sys.argv[8]
    title = sys.argv[9]
    plot_type = sys.argv[10]
if len(sys.argv) > 11:
    predictions_offline_file_name = sys.argv[11]

x = []
y = []

plt.xlabel(x_label)
plt.ylabel(y_label)

x = getPlottingData(inputs_file_name, input_index)
y = getPlottingData(outputs_file_name, 1)
plt.plot(x, y, ".", label="real data")
if predictions_file_name != "/":
    y = getPlottingData(predictions_file_name, 1)
    plt.plot([i+shift_data for i in x], y, plot_type, label="linear predictor function (online)" if plot_type == "-" else "LR fit (online)")
plt.title(title)

# adding offline predictions
if len(sys.argv) > 11:
    y = getPlottingData(predictions_offline_file_name, 1)
    plt.plot([i+shift_data for i in x], y, plot_type, label="linear predictor function (offline)" if plot_type == "-" else
        "LR fit (offline)")

plt.legend()
plotsPath = "../python_plots/plots/"
plt.savefig(plotsPath + output_image_name + ".pdf")
# plt.show()  # blank when using pgf
