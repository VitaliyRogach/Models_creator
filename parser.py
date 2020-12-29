import json
import os
import glob
import re
import time
import shutil


class JSONRead:
    jsonFileList = []
    mainDir = 'Directory_json/'
    fileList = os.listdir(mainDir)

    for fl in fileList:
        if '.json' in fl:
            jsonFileList.append(fl)
    for fl in jsonFileList:
        with open(mainDir + fl) as fileNM:
            data = json.load(fileNM)
            for i in data['strings']:
                renameDir = mainDir + fl
                acceptDir = mainDir + 'accept/' + fl
                nApprovedDir = mainDir + 'notApproved/' + fl
                # print(renameDir)
                # print(acceptDir)
                if " " in i['name']:
                    # fileNM.close()
                    # os.rename(renameDir , nApprovedDir)
                    shutil.copy(renameDir, nApprovedDir)
                    print("Error in name(space) ", i)
                    time.sleep(1)
                elif " " not in i['name']:
                    fileNM.close()
                    # os.rename(renameDir, acceptDir)
                    shutil.copy(renameDir, acceptDir)
                    print("DONE! ", i['name'])
                    time.sleep(1)


class Insert(JSONRead):
    a = []
    j = 0
    tmp = JSONRead
    modelName = 'class {}(models.Model):'
    tmpList = []
    modelList = []
    mainDir = 'Directory_json/'
    acceptDir = mainDir + 'accept/'
    tmpString = '{0} = models.{1}(max_length={2})'
    fileList = os.listdir(acceptDir)
    acceptFileList = []
    for fl in fileList:
        if '.json' in fl:
            acceptFileList.append(fl)
    # print(acceptFileList)
    for fl in acceptFileList:
        with open(acceptDir + fl) as fileNM:
            data = json.load(fileNM)
        for i in data:
            modelNm = data['model_name']
            modell = modelName.format(modelNm)
        modelList.append(modell)
        for j in data['strings']:
            name_field = j['name']
            type_field = j['type']
            max_length_field = j['max_length']
            abc = tmpString.format(name_field, type_field, max_length_field)
            tmpList.append(abc)
            fieldString = "    " + tmpList[-1]
            modelList.append(fieldString)
    with open('models.py', 'a') as modelFl:
        for string in modelList:
            modelFl.write('\n' + string)