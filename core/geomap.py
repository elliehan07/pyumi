##@Jamie_Farrell

from json import load
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

jsondata = "example.json" 



with open(jsondata) as data_file:
    data = load(data_file)

data = data["features"]

coordinate = []
coordinates = []
for i in range(0, len(data)):
    if len (data[i])>2:
        for j in range(0,len(data[i]['geometry']["coordinates"][0][0])):
            coordinate.append(tuple(data[i]['geometry']["coordinates"][0][0][j]))
        coordinates.append(coordinate)
        coordinate = []
    else:
        coordinates.append("null")



codes = []
for i in range(0,len(coordinates)):
    code = [1]
    for j in range(2,len(coordinates[i])):
        code.append(2)
    code.append(79)
    codes.append(code)
    code = [1]

verts = coordinates
fig = plt.figure(num=None, figsize=(15, 10), dpi=150, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111)

cmap = plt.cm.get_cmap('Spectral')

for i in range(0,len(codes)):
    if coordinates[i] != "null":
        path = Path(verts[i], codes[i])
        color = np.random.random(10)
        patch = patches.PathPatch(path, facecolor = cmap(i/1))
        ax.add_patch(patch)


ax.autoscale_view()
plt.axes().set_aspect('equal', 'datalim')

ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())
plt.show()