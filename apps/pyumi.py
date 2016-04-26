# insert notes and name
import zipfile
import os
import shutil
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import json as js

def unzip(source, dest_dir):
    with zipfile.ZipFile(source) as zf:
        for member in zf.infolist():
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)
    path = str(dest_dir) + '/sdl-common/sdl-common/project.json'
    return path

def bldgs(jsonpath):
    bldgs = []
    data = js.loads(open(jsonpath).read())
    features = data["features"]
    for i in range(0,int(len(features))):
        bldgs.append(data["features"][i]["properties"]['Name'])
    return bldgs

def types(jsonpath):
    types = []
    data = js.loads(open(jsonpath).read())
    features = data["features"]
    for i in range(0,int(len(features))):
        types.append(data["features"][i]["properties"]['UseType'])
    return types


def map(jsonpath):
    data = js.loads(open(jsonpath).read())
    coordinates = getcoords(data)
    codes = polygonscode(coordinates)
    fig = plt.figure(num=None, figsize=(15, 10), dpi=150, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(111)
    for i in range(0,len(codes)):
        if coordinates[i] != "null":
            path = Path(coordinates[i], codes[i])
            color = np.random.random(10)
            patch = patches.PathPatch(path, facecolor="black")
            ax.add_patch(patch)
    ax.autoscale_view()
    plt.axes().set_aspect('equal', 'datalim')



def AddData(dic,lvl,att):
    for key, value in dic.iteritems():
        if att in value:
            break
        else:
            jsondata = umijson+'//'+key
            with open(jsondata) as data_file:    
                data = json.load(data_file)
            features = data["features"]
            bldgs = []
            for f in range(0,int(len(features))):
                bldgs.append(data["features"][f][lvl][att])
            value.insert(len(d[key].count()),att,bldgs)

def AddTotalData(dic,lvl,att):
    for key, value in dic.iteritems():
        if att in value:
            break
        else:
            jsondata = umijson+'//'+key
            with open(jsondata) as data_file:    
                data = json.load(data_file)
            features = data["features"]
            bldgs = []
            for f in range(0,int(len(features))):
                bldgs.append(sum(data["features"][f][lvl][att]))
            value.insert(len(d[key].count()),att,bldgs)



def getcoords(data):
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
            #code = [1]
        code.append(79)
        codes.append(code)
    return codes


def time_map(jsonpath, hour, lineweights):
    data = js.loads(open(jsonpath).read())
    coordinates = getcoords(data)
    codes = polygonscode(coordinates)
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


################



def avgloadprofile(data, usetype, energytype):
    loadprofiles = []
    rawdata = js.loads(open(data).read())
    for n in rawdata.get("features"):
        feature = n.get("properties")
        if usetype == feature.get("UseType"):
            year = feature.get(energytype)
            days = zip(*(iter(year),) * 24)
            loadprofile = sum(map(np.array, days))
            loadprofiles.append(loadprofile)
    return loadprofiles


def winterloadprofile(data, usetype, energytype):
    loadprofiles = []
    rawdata = js.loads(open(data).read())
    for n in rawdata.get("features"):
        feature = n.get("properties")
        if usetype == feature.get("UseType"):
            year = feature.get(energytype)
            days = zip(*(iter(year),) * 24)
            days = days[356:365] + days[0:80]
            loadprofile = sum(map(np.array, days))
            loadprofiles.append(loadprofile)
    return loadprofiles


def summerloadprofile(data, usetype, energytype):
    loadprofiles = []
    rawdata = js.loads(open(data).read())
    for n in rawdata.get("features"):
        feature = n.get("properties")
        if usetype == feature.get("UseType"):
            year = feature.get(energytype)
            days = zip(*(iter(year),) * 24)
            days = days[172:266]
            loadprofile = sum(map(np.array, days))
            loadprofiles.append(loadprofile)
    return loadprofiles


def loadprofile(jsonpath, energytype, day):
    loadprofiles = []
    rawdata = js.loads(open(jsonpath).read())
    for n in rawdata.get("features"):
        feature = n.get("properties")
        energy = feature.get(energytype)
        days = zip(*(iter(energy),) * 24)
        loadprofile = days[day]
        loadprofiles.append(loadprofile)
    return loadprofiles


def makelineweight(data, usetype):
    lineweights = []
    rawdata = js.loads(open(data).read())
    usetypes = []
    for n in rawdata.get("features"):
        feature = n.get("properties")
        usetype = feature.get("UseType")
        usetypes.append(usetype)
    for i in usetypes:
        if i == "Residential and Lodging":
            lineweights.append(3.5)
        if i == "Office Spaces":
            lineweights.append(2)
        if i == "Retail":
            lineweights.append(1)
        if i == "Mixed use":
            lineweights.append(2.5)
