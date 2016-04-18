# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 15:19:27 2016

@author: rjf
"""

import unpack as up
import os
import shutil
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#umifiles = str(raw_input("Please paste the path of you folder full of umi files."))
umifiles = "C:\\Users\\rjf\\Desktop\\PB1_C_2016"

#protoblockname = raw_input("Name of you run:")
#Residential or Commercial 
protoblockname = 'Protoblock 1  2016'


if os.path.exists(umifiles+'\\'+'umijson'):
    shutil.rmtree(umifiles+'\\'+'umijson') 

up.unpack(umifiles)


umijson = umifiles + '\\umijson'


key = umijson+'\\run1.umi'

with open(key) as data_file:
    data = json.load(data_file)

features = data["features"]


bldgs = []
for i in range(0,int(len(features))):
    bldgs.append(data["features"][i]["properties"]['Name'])

df = pd.DataFrame(bldgs)
df.columns = ['Name']

d = {}
for i in os.listdir(umijson):
    index = 0
    df =[]
    df.append(i)
    jsondata = umijson+'\\'+i
    with open(jsondata) as data_file:    
        data = json.load(data_file)
    features = data["features"]
    bldgs = []
    for f in range(0,int(len(features))):
        bldgs.append(data["features"][f]["properties"]['Name'])
    df = df[index]
    index += 1
    df = pd.DataFrame(bldgs)
    df.columns = ['Name']
    d.update({str(i):df})
    
sims = d

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

AddData(sims,'properties','WwrN')
AddTotalData(sims,'properties','OETotal')
AddTotalData(sims,'properties','OECooling')
AddTotalData(sims,'properties','OEHeating')
AddTotalData(sims,'properties','OEEquipment')
AddTotalData(sims,'properties','OELighting')    

concatenated = pd.concat(sims,join='outer',ignore_index=True)
table = pd.pivot_table(concatenated, index=['WwrN'])
table2 = table
del table2['OETotal']
lables = table2.columns.values
plt.xlabel('WWR')
plt.ylabel('kWh')
plt.title(protoblockname+'\nAggregate Energy Demand by Source')
plt.xlim([0.05,0.8])
plt.ylim([0,250000])
plt.plot(table2)
plt.legend(lables,bbox_to_anchor=(1.05, 0.75), loc=2, borderaxespad=0.)
fig1 = plt.gcf()
plt.draw()
plt.show()
fig1.savefig("C:\\Users\\rjf\\Desktop\\Vis\\"+protoblockname+'_Demand'+'.svg',bbox_inches='tight')
fig1.savefig("C:\\Users\\rjf\\Desktop\\Vis\\"+protoblockname+'_Demand'+'.png',bbox_inches='tight',dpi=200)
        
 
AddData(sims,'properties','GrossFloorArea') 
concatenated = pd.concat(sims,join='outer',ignore_index=True)
table = pd.pivot_table(concatenated, index=['Name','WwrN'])
table['EUI'] = table['OETotal'] / table['GrossFloorArea']
del table['GrossFloorArea']
del table['OECooling']
del table['OEEquipment']
del table['OEHeating']
del table['OELighting']
del table['OETotal']
concatenated2 = pd.concat(sims,join='outer',ignore_index=True)
nametable = pd.pivot_table(concatenated2, index=['Name'])
wwtable = pd.pivot_table(concatenated2, index=['WwrN'])
#plt.figure()
plt.xlabel('WWR')
plt.ylabel('EUI')
plt.title(protoblockname+'\nEUI of Individual Buildings')
plt.axis([0.1,.9, 60,180])
lables = nametable.index.values
for names in nametable.index.values:
    plot = table.query('Name == "'+str(names)+'"')
    y = plot['EUI'].values
    x = wwtable.index.values
    plt.plot(x,y)
    plt.draw()
plt.legend(lables,bbox_to_anchor=(1.05, 0.75), loc=2, borderaxespad=0.)
fig2 = plt.gcf()
plt.draw()
plt.show()
#fig2.savefig("C:\\Users\\rjf\\Desktop\\Vis\\"+protoblockname+'_EUI'+'.svg',bbox_inches='tight')
#fig2.savefig("C:\\Users\\rjf\\Desktop\\Vis\\"+protoblockname+'_EUI'+'.png',bbox_inches='tight',dpi=200)          
            
