
import rhinoscriptsyntax as rs
import Rhino
import zipfile
import os.path
import json
import tempfile, shutil
import time


# Function to get bulding IDs for use upstream.

def GetBldgs():
    path = tempfile.mkdtemp()
    path = str(path) + "\\umitemp.umi"
    rs.Command("_-UmiBundleSaveAs" +" " + path + " ")
    path_out = tempfile.mkdtemp()
    unzip(path,path_out)
    jsondata = str(path_out) + "\\sdl-common\\sdl-common\\project.json"
    with open(jsondata) as data_file:
        data = json.load(data_file)
        features = data["features"]
        bldgs = []
    for i in range(0,int(len(features))):
        bldgs.append(data["features"][i]["id"])
    return bldgs

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)




# Building Template/EPW Mods

def SetTemp(bldg,temp):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S T "+temp+ " ")

def umiTempLib(filepath):
    rs.Command("_-UmiImportTemplateLibrary" + " " + filepath + " ")

def umiEPW(filepath):
    rs.Command("_-UmiImportWeatherFile" + " " + filepath + " ")




# Building Window-Wall-Ratio Mods

def SetWWR_E(bldg,ratio):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S W "+str(ratio))

def SetWWR_N(bldg,ratio):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S I "+str(ratio))

def SetWWR_S(bldg,ratio):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S N "+str(ratio))

def SetWWR_W(bldg,ratio):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S D "+str(ratio))

def SetWWR(bldg,ratio):
    SetWWR_E(bldg,ratio)
    SetWWR_N(bldg,ratio)
    SetWWR_S(bldg,ratio)
    SetWWR_W(bldg,ratio)



# Geometry mods 

def moveObject(bldg,translation):
    rs.MoveObject(bldg,translation)


# File Save Ops 

def Save(OutputPath):
    rs.Command("_-UmiBundleSaveAs" +" " +OutputPath+".umi" " ")

def SaveTemp(OutputPath):
    rs.Command("_-SaveAs" +" " +OutputPath+ " ")


# Calcs 

def umiEnergy():
    rs.Command("_-UmiSimulateEnergy"+ " ")

def umiFAR():
    rs.Command("_-UmiCalculateFAR"+ " ")



### Hello World ## 
bldgs = GetBldgs()
SetWWR(bldgs,0.9)

