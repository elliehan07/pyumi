# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 14:08:07 2016

@author: rjf
"""
import zipfile
import os
import shutil
#import json
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

umifiles = "C:\\Users\\rjf\\Desktop\\PB2_C_2080"
#umifiles = raw_input("Please paste the path of you folder full of umi files:")


umijson = umifiles+"\\"+"umijson"

if os.path.exists(umijson+'\\'+'sdl-common'):
    shutil.rmtree(umijson+'\\'+'sdl-common')
 
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

for i in os.listdir(umijson): 
    os.remove(umijson+'\\'+i)
    
for i in os.listdir(umifiles):    
    if i != "umijson":
        unzip(umifiles+'\\'+i,umijson)
        os.rename(umijson+'\\sdl-common\\sdl-common\\project.json',umijson+'\\'+i)
 
if os.path.exists(umijson+'\\'+'sdl-common'):
    shutil.rmtree(umijson+'\\'+'sdl-common')       
        
for i in os.listdir(umijson):
    if os.path.splitext(i)[1] != '.umi':
        os.remove(umijson+'//'+i)





