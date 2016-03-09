
import rhinoscriptsyntax as rs
import Rhino
import zipfile
import os.path
import json


def SetTemp(bldg,temp):
    rs.SelectObject(bldg)
    rs.Command("UmiSetBuildingSetting S T "+temp)

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

def moveObject(bldg,translation):
    rs.MoveObject(bldg,translation)


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
