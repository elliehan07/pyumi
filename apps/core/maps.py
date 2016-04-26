# insert notes and name
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np


def coordinates(data):
    geodata = data["features"]
    coordinate = []
    coordinates = []
    for i in range(0, 225):
        if len(geodata[i]['geometry']["coordinates"]) > 0:
            for j in range(0, len(geodata[i]['geometry']["coordinates"][0][0])):
                coordinate.append(tuple(geodata[i]['geometry']["coordinates"][0][0][j]))
            coordinates.append(coordinate)
            coordinate = []
        else:
            coordinates.append("null")
    return coordinates


def polygonscode(coordinates):
    codes = []
    for i in range(0, len(coordinates)):
        code = [1]
        for j in range(2, len(coordinates[i])):
            code.append(2)
            code = [1]
        code.append(79)
        codes.append(code)
    return codes


def MakeChart(data, hour, coordinates, lineweights, codes):
    cmap = plt.cm.get_cmap('YlOrRd')
    fig = plt.figure(num=None, figsize=(15, 10), dpi=150, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)
    ax.set_title('Winter Day: Hour '+str(hour), fontsize=20, fontweight='bold')
    for i in range(0,len(codes)):
        if coordinates[i] != "null":
            path = Path(coordinates[i], codes[i])
            color = np.random.random(10)
            patch = patches.PathPatch(path, facecolor=cmap(data), lw=lineweights[i])
            ax.add_patch(patch)
    ax.autoscale_view()
    plt.axes().set_aspect('equal', 'datalim')





