import zipfile
import os
import shutil
import pandas as pd
import json as js
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline  

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

#SPRING EQUINOX	March 20, 12:30 AM EDT   Day 80 
#SUMMER SOLSTICE	June 20, 6:34 P.M. EDT   Day 172 
#FALL EQUINOX	September 22, 10:21 A.M. EDT  Day 266
#WINTER SOLSTICE	December 21, 5:44 A.M. EST 356 




def AvgLoadProfile(data,usetype,energytype):
    loadprofiles = []
    rawdata = js.loads(open(data).read())
    for n in rawdata.get("features"):
        feature = n.get("properties")
        if usetype == feature.get("UseType"):
            year = feature.get(energytype)
            days = list(split_list(year,24))
            loadprofile = sum(map(np.array, days))
            loadprofiles.append(loadprofile)
    return loadprofiles


def WinterLoadProfile(data,usetype,energytype):
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

def SummerLoadProfile(data,usetype,energytype):
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


unzip("0411_Energy_v3.umi","unzipped")
json = "unzipped\sdl-common\sdl-common\project.json"

loads = WinterLoadProfile(json,"Residential and Lodging","OETotal")
loads = sum(map(np.array, loads))


data = pd.DataFrame(loads)
#data = data.transpose()
plt.plot(data)


