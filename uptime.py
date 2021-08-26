import sys
import tkinter
# import matplotlib
# matplotlib.use("GTK3Agg")
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from format_seconds import format_seconds

filename = str(sys.argv[1])


def read_file(filename):

    with open(filename) as f:
        data = f.readlines()

    return data


data = read_file(filename)

data_dict = {"stamp": [], "epoch": [], "up": []}
for i, point in enumerate(data):
    if point[0] == "[":
        n = point.find("]")
        epoch = int(round(float(point[1:n]), 0))
        data_dict["epoch"].append(int(epoch))
        stamp = datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M")
        data_dict["stamp"].append(stamp)
        if "Unreachable" in point:
            # 0=down
            data_dict["up"].append(0)
        else:
            # 1=up
            data_dict["up"].append(1)


plt.plot(data_dict["epoch"], data_dict["up"])
plt.title(f"{filename} Last log at: {data_dict['stamp'][-1]}")

previous = data_dict["up"][0]
last_change = data_dict["epoch"][0]
for i, up in enumerate(data_dict["up"][1::]):
    if up != previous:
        plt.text(
            data_dict["epoch"][i],
            1 - data_dict["up"][i],
            data_dict["stamp"][i],
            fontsize=10,
            color="red",
            bbox=dict(facecolor="black", edgecolor="black", pad=2.0),
            ha="center",
            va="center",
        )
        plt.text(
            (data_dict["epoch"][i] + last_change) / 2,
            0.5,
            format_seconds(int((data_dict["epoch"][i] - last_change)), "{d}:{h}:{m}"),
            fontsize=10,
            color="red",
            ha="center",
            va="center",
        )

        last_change = data_dict["epoch"][i]
    previous = up


plt.show()
