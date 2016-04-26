import json as js
import numpy as np


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


def loadprofile(data, energytype, day):
    loadprofiles = []
    rawdata = js.loads(open(data).read())
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
