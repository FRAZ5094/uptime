import matplotlib.pyplot as plt
from datetime import datetime
filename="Ryzen_log"

def read_file(filename):

    with open(filename) as f:
        data=f.readlines()

    return data


data=read_file(filename)

data_dict={"stamp":[],"epoch":[],"up":[]}
for i,point in enumerate(data):
    if point[0]=="[":
        n=point.find("]")
        epoch=float(point[1:n])
        data_dict["epoch"].append(epoch)
        stamp=datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
        data_dict["stamp"].append(stamp)

        if "Unreachable" in point:
            #0=down
            data_dict["up"].append(0)
        else:
            #1=up
            data_dict["up"].append(1)


plt.plot(data_dict["stamp"],data_dict["up"])

previous=3
for i,up in enumerate(data_dict["up"]):
    if up!=previous:
        plt.text(data_dict["epoch"][i],0.5,data_dict["stamp"])
    previous=up

plt.show()
