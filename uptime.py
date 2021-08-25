import matplotlib.pyplot as plt
filename="Ryzen_log"

def read_file(filename):

    with open(filename) as f:
        data=f.readlines()

    return data


data=read_file(filename)

data_dict={"time":[],"up":[]}
for i,point in enumerate(data):
    if point[0]=="[":
        n=point.find("]")
        time=float(point[1:n])
        data_dict["time"].append(time)
        if "Unreachable" in point:
            #0=down
            data_dict["up"].append(0)
        else:
            #1=up
            data_dict["up"].append(1)

plt.plot(data_dict["time"],data_dict["up"])
plt.show()
