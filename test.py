import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import pickle

print("Hello World!")

x = []
y = []
# with open('../flink-rc/src/test/resources/glaciers/input_data/glaciers.csv') as csvfile:
with open('plot_data/test.csv') as csvfile:
    # '../flink-rc/src/test/resources/glaciers/input_data/glaciers.csv'
    data = csv.reader(csvfile)
    for row in data:
        try:
            x.append(float(row[0]))
            y.append(float(row[2]))
        except ValueError:  # skip invalid lines
            continue

# plt.style.use('seaborn-darkgrid')
# plt.grid(True)
fig_object = plt.figure()
plt.plot(x, y, label="input data")
plt.xlabel('Year')
plt.ylabel('Mean cumulative mass balance')
# plt.style.use('classic')
# plt.xlim(x[0]-5, x[-1]+6)
## Setting edge ticks by getting current tick spacing ##
ticks = plt.xticks()[0]
# print(ticks)
tick_spacing = ticks[1] - ticks[0]
# print(tick_spacing)
plt.xticks(np.arange(math.floor(x[0]/tick_spacing)*tick_spacing,
                     math.ceil(x[-1]/tick_spacing)*tick_spacing + 1, tick_spacing))

plt.legend()

pickle.dump(fig_object, open('test.fig.pickle', 'wb'))
# plotsPath = "./plots/"
# plt.savefig("./plots/testLRFit.png")
# plt.show()

# imRead = plt.imread("plots/Glaciers Meltdown.png")
# print(imRead)
# plt.plot(imRead)
# imPlot = plt.imshow(imRead)

loadedFig = pickle.load(open('test.fig.pickle','rb'))
loadedFig.show()
# plt.show()
