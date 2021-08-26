from datetime import datetime

import numpy as np
import termplot as plt

filename = "Ryzen_log"


def read_file(filename):

    with open(filename) as f:
        data = f.readlines()

    return data


data = read_file(filename)

data_dict = {"stamp": [], "epoch": [], "up": []}
for i, point in enumerate(data):
    if point[0] == "[":
        n = point.find("]")
        epoch = float(point[1:n])
        data_dict["epoch"].append(epoch)
        stamp = datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M")
        data_dict["stamp"].append(stamp)

        if "Unreachable" in point:
            # 0=down
            data_dict["up"].append(0)
        else:
            # 1=up
            data_dict["up"].append(1)


plt.plot(data_dict["epoch"], data_dict["up"])

previous = data_dict["up"][0]
for i, up in enumerate(data_dict["up"][1::]):
    if up != previous:
        if up == 0:
            y = 0.75
        if up == 1:
            y = 0.25
        plt.text(
            data_dict["epoch"][i] - 1750,
            y,
            data_dict["stamp"][i],
            fontsize=6,
            color="red",
        )
        # print("added stamp")

    previous = up

plt.show()
