#!/usr/bin/python3

import sys, os

def main():
    # Preparations
    utServerPath = "/ut-server"
    utDataPath = "/ut-data"
    folders = ["Maps", "Music", "Sounds", "System", "Textures"]
    
    # Remove all Symlinks
    for folder in folders:
        folderPath = os.path.join(utServerPath, folder)
        for entry in os.listdir(folderPath):
            fullFilePath = os.path.join(folderPath, entry)
            if os.path.islink(fullFilePath):
                if entry == "libSDL-1.2.so.0":
                    continue
                print(f'[D] {os.path.join(folder, entry)}')
                os.remove(fullFilePath)
    
    # Add Symlinks
    for folder in folders:
        folderPath = os.path.join(utDataPath, folder)
        for entry in os.listdir(folderPath):
            fullFilePath = os.path.join(folderPath, entry)
            print(f'[L] {os.path.join(folder, entry)}')
            targetPath = os.path.join(utServerPath, folder, entry)
            os.symlink(fullFilePath, targetPath)

    # Initialize ini with default values
    #set_config_value("/ut-server/System/UnrealTournament.ini", "UWeb.WebServer", "bEnabled", "True")
    #set_config_value("/ut-server/System/UnrealTournament.ini", "UWeb.WebServer", "ListenPort", "5580")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'UTServerAdmin.UTServerAdmin', 'AdminUsername', "admin")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'UTServerAdmin.UTServerAdmin', 'AdminPassword', "admin")
#
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameReplicationInfo', 'ServerName', "My UT Server")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameReplicationInfo', 'AdminName', "UTAdmin")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameReplicationInfo', 'AdminEmail', "no@one.com")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameReplicationInfo', 'MOTDLine1', "Have Fun")
#
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameInfo', 'AdminPassword', "admin")
    #set_config_value("/ut-server/System/UnrealTournament.ini", 'Engine.GameInfo', 'GamePassword', "")


def set_config_value(filePath, section, key, value):
    f = open(filePath, "r")
    contents = f.readlines() # Note: Contains newline characters
    f.close()
    newLine = f"{key}={value}{os.linesep}"
    inSection = False
    foundKey = False
    for index, line in enumerate(contents):
        if line[0] == '[':
            currSection = line[1:line.index(']')]
            if currSection == section:
                inSection = True
                continue
            else:
                if inSection:
                    break
        if inSection:
            if '=' in line:
                (currKey, currValue) = line.split('=', 1)
                if (currKey == key):
                    foundKey = True
                    break

    if (foundKey):
        del contents[index]
    else:
        index = index - 1
    contents.insert(index, newLine)
    f = open(filePath, "w")
    f.writelines(contents)
    f.close()

if __name__== "__main__":
    main()
