#!/usr/bin/python3

import sys, os, re

# Preparations
utServerPath = "/ut-server"
utDataPath = "/ut-data"
folders = ["Maps", "Music", "Sounds", "System", "Textures"]
utIniFileServer = f"/{utServerPath}/System/UnrealTournament.ini"
utIniFileData = f"/{utDataPath}/System/UnrealTournament.ini"
userIniFileServer = f"/{utServerPath}/System/User.ini"
userIniFileData = f"/{utDataPath}/System/User.ini"

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "i":
        initial_setup()
    else:
        prepare()

def initial_setup():
    # Prepare the directories
    os.makedirs('/ut-data/Maps', exist_ok=True)
    os.makedirs('/ut-data/Music', exist_ok=True)
    os.makedirs('/ut-data/Sounds', exist_ok=True)
    os.makedirs('/ut-data/System', exist_ok=True)
    os.makedirs('/ut-data/Textures', exist_ok=True)

    # Initialize ini with good default values
    ## Enable the web admin and set username/password
    set_config_value(utIniFileServer, 'UWeb.WebServer', 'bEnabled', 'True')
    set_config_value(utIniFileServer, 'UWeb.WebServer', 'ListenPort', '5580')
    set_config_value(utIniFileServer, 'UTServerAdmin.UTServerAdmin', 'AdminUsername', 'admin')
    set_config_value(utIniFileServer, 'UTServerAdmin.UTServerAdmin', 'AdminPassword', 'admin')
    ## Replace / Add Server information
    set_config_value(utIniFileServer, 'Engine.GameReplicationInfo', 'ServerName', 'My UT Server')
    set_config_value(utIniFileServer, 'Engine.GameReplicationInfo', 'AdminName', 'UTAdmin')
    set_config_value(utIniFileServer, 'Engine.GameReplicationInfo', 'AdminEmail', 'no@one.com')
    set_config_value(utIniFileServer, 'Engine.GameReplicationInfo', 'MOTDLine1', 'Have Fun')
    ## Replace / Add Admin and Game password
    set_config_value(utIniFileServer, 'Engine.GameInfo', 'AdminPassword', 'admin')
    set_config_value(utIniFileServer, 'Engine.GameInfo', 'GamePassword', '')
    ## Add some bots by default
    set_config_value(utIniFileServer, 'Botpack.DeathMatchPlus', 'MinPlayers', '4')
    set_config_value(utIniFileServer, 'Botpack.CTFGame', 'MinPlayers', '8')
    set_config_value(utIniFileServer, 'Botpack.DeathMatchPlus', 'InitialBots', '4')
    set_config_value(utIniFileServer, 'Botpack.CTFGame', 'InitialBots', '8')
    ## Section to enable/disable publishing the server in the server list
    set_config_value(utIniFileServer, 'IpServer.UdpServerUplink', 'DoUpLink', 'True')
    set_config_value(utIniFileServer, 'IpServer.UdpServerUplink', 'UpdateMinutes', '1')
    set_config_value(utIniFileServer, 'IpServer.UdpServerUplink', 'MasterServerPort', '27900')
    ## Add server visibility in server browser inside game by adding correct URLs
    remove_config_key(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink.*')
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=utmaster.epicgames.com MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.333networks.com MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.qtracker.com MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.telefragged.com MasterServerPort=27500', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.errorist.eu MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.hlkclan.net MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.openspy.net MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.oldunreal.com MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master2.oldunreal.com MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.hypercoop.tk MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.newbiesplayground.net MasterServerPort=27900', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'IpServer.UdpServerUplink MasterServerAddress=master.gonespy.com MasterServerPort=27900', True)

    # Add Mutators
    ## CustomCrossHairScale
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'CCHS4', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerActors', 'CCHS4.CCHS', True)
    os.remove(f"/{utDataPath}/System/CCHS4.int")
    ## FlagAnnouncementsV2
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'FlagAnnouncementsV2', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'DefaultAnnouncements', True)
    ## KickIdlePlayers2
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'KickIdlePlayers2', True)
    ## Map Vote Extended
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'MVE2f', True)
    ## VoteSys
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'VoteSys_v7d', True)
    ## WhoPushedMe
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'EnhancedItems', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'WhoPushedMe', True)
    ## ZeroPingPlus103
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'ZeroPingPlus103', True)
    ## SLV205 (StrangeLove)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'SLV205', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'SLV2Models', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'SLV2Sounds', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'SLV2Fonts', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'SLV2Textures', True)

    # Add Mods
    ## BunnyTrack
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'BTPPUser', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'CountryFlags3', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'BTPlusPlusPublicUTBT_beta3', True)
    ## ChaosUT
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'UTChaosMap', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'ChaosUTRHUD', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'ChaosUT', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'ChaosUTMiscMuts', True)
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'ChaosGames', True)
    ## MonsterHunt
    set_config_value(utIniFileServer, 'Engine.GameEngine', 'ServerPackages', 'MonsterHunt', True)

    # Move and/or symlink the original ini files
    move_and_symlink(utIniFileServer, utIniFileData)
    move_and_symlink(userIniFileServer, userIniFileData)

    # Remove the original BotPack.u and just keep the newer Botpack.u from the latest patch
    os.remove(f"/{utServerPath}/System/BotPack.u")

    # Fix some file cases (to prevent a warning)
    os.rename(f"/{utServerPath}/Textures/UTcrypt.utx", f"/{utServerPath}/Textures/utcrypt.utx")
    os.rename(f"/{utServerPath}/Textures/GenFluid.utx", f"/{utServerPath}/Textures/genfluid.utx")
    os.rename(f"/{utServerPath}/Textures/Soldierskins.utx", f"/{utServerPath}/Textures/SoldierSkins.utx")

def prepare():
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
            if not (os.path.lexists(targetPath)):
                os.symlink(fullFilePath, targetPath)

    # Update some config values according to optional environment variables
    ## Enable the web admin and set username/password
    set_config_to_environment('UT_WEBADMINUSER', utIniFileServer, 'UTServerAdmin.UTServerAdmin', 'AdminUsername')
    set_config_to_environment('UT_WEBADMINPWD', utIniFileServer, 'UTServerAdmin.UTServerAdmin', 'AdminPassword')
    ## Replace / Add Server information
    set_config_to_environment('UT_SERVERNAME', utIniFileServer, 'Engine.GameReplicationInfo', 'ServerName')
    set_config_to_environment('UT_ADMINNAME', utIniFileServer, 'Engine.GameReplicationInfo', 'AdminName')
    set_config_to_environment('UT_ADMINEMAIL', utIniFileServer, 'Engine.GameReplicationInfo', 'AdminEmail')
    set_config_to_environment('UT_MOTD1', utIniFileServer, 'Engine.GameReplicationInfo', 'MOTDLine1')
    ## Replace / Add Master server connection information
    set_config_to_environment('UT_DOUPLINK', utIniFileServer, 'IpServer.UdpServerUplink', 'DoUpLink')
    ## Replace / Add Admin and Game password
    set_config_to_environment('UT_ADMINPWD', utIniFileServer, 'Engine.GameInfo', 'AdminPassword')
    set_config_to_environment('UT_GAMEPWD', utIniFileServer, 'Engine.GameInfo', 'GamePassword')
    ## Replace / Add Minimum Players
    set_config_to_environment('UT_MINPLAYERS_DM', utIniFileServer, 'Botpack.DeathMatchPlus', 'MinPlayers')
    set_config_to_environment('UT_MINPLAYERS_CTF', utIniFileServer, 'Botpack.CTFGame', 'MinPlayers')
    set_config_to_environment('UT_INITIALBOTS_DM', utIniFileServer, 'Botpack.DeathMatchPlus', 'InitialBots')
    set_config_to_environment('UT_INITIALBOTS_CTF', utIniFileServer, 'Botpack.CTFGame', 'InitialBots')

def move_and_symlink(fileSrc, fileDest):
    os.replace(fileSrc, fileDest)
    symlink(fileDest, fileSrc)

def symlink(fileSrc, fileDest):
    os.symlink(fileSrc, fileDest)

def set_config_to_environment(environmentKey, filePath, section, key):
    if os.environ.get(environmentKey) is not None:
        set_config_value(filePath, section, key, os.environ.get(environmentKey))

def remove_config_key(filePath, section, key, valueRegex = None):
    """
    This method removes all occurences of the desired key in the desired section.

    Args:
        filePath (str)    : The path to the file.
        section (str)     : The desired section name.
        key (str)         : The desired key.
        valueRegex (str)  : The regex of the value which needs to match in order to remove the line.
    """
    # Read all lines of the file (including newlines)
    f = open(filePath, "r")
    contents = f.readlines()
    f.close()
    # Loop thru all existing lines
    inSection = False
    linesWithKey = []
    for index, line in enumerate(contents):
        # Skip empty lines
        if len(line) == 0:
            continue
        # Skip comments
        if line[0] == '#' or line[0] == '/':
            continue
        # We found a section start
        if line[0] == '[':
            currSection = line[1:line.index(']')]
            # Check if we are in the desired section
            if currSection == section:
                inSection = True
                continue
            else:
                # If we're in the desired section and found another section, break out of the loop
                if inSection:
                    break
        # No section header found but we are in the desired section
        elif inSection:
            # Make sure there is an = so it should be a key/value pair
            if '=' in line:
                # Parse the key and value
                (currKey, currValue) = line.split('=', 1)
                # If the key is the desired key
                if (currKey == key):
                    # Check if the value matches the regex if any is given
                    if (valueRegex == None or re.search(valueRegex, currValue.strip()) != None):
                        linesWithKey.append(index)

    # Delete the lines (reversed so the indices are correct when removed)
    if (len(linesWithKey) > 0):
        linesWithKey.reverse()
        for keyIndex in linesWithKey:
            del contents[keyIndex]

    # Write back the file
    f = open(filePath, "w")
    f.writelines(contents)
    f.close()

def set_config_value(filePath, section, key, value, alwaysInsert=False):
    """
    This method replaces an exiting key with the value or adds a new one. Also adds the section if it cannot be found.

    Args:
        filePath (str)    : The path to the file.
        section (str)     : The desired section name.
        key (str)         : The desired key.
        value (str)       : The value to set.
        alwaysInsert (bool): A flag to indicate if the value should always be added or replaced if the key already exists.
    """
    # Read all lines of the file (including newlines)
    f = open(filePath, "r")
    contents = f.readlines()
    f.close()
    # Loop thru all existing lines
    inSection = False
    foundSection = False
    foundKey = False
    for index, line in enumerate(contents):
        # Skip empty lines
        if len(line) == 0:
            continue
        # Skip comments
        if line[0] == '#' or line[0] == '/':
            continue
        # We found a section start
        if line[0] == '[':
            currSection = line[1:line.index(']')]
            # Check if we are in the desired section
            if currSection == section:
                foundSection = True
                inSection = True
                continue
            else:
                # If we're in the desired section and found another section, break out of the loop
                if inSection:
                    break
        # No section header found but we are in the desired section
        elif inSection:
            # Make sure there is an = so it should be a key/value pair
            if '=' in line:
                # Parse the key and value
                (currKey, currValue) = line.split('=', 1)
                # If the key is the desired key
                if (currKey == key):
                    if (currValue.strip() == value):
                        # The value is already the desired value, so skip it
                        return
                    if (alwaysInsert):
                        # Continue searching for the exact key/value pair
                        continue
                    foundKey = True
                    break

    if (foundKey):
        # We found a key where we want to replace the value, so delete the old key/value
        del contents[index]
    elif (not foundSection):
        # We couldn't find the section, so add the section at the very end and adjust the index
        index += 1
        contents.insert(index, f"\n")
        index += 1
        contents.insert(index, f"[{section}]\n")
        index += 1
    elif index == len(contents) - 1:
        # We are at the very last line, increase the index so we add the new value below at the end
        index += 1
    else:
        # As we are past the last key/value of the desired section, we will go back one line
        index -= 1
    # Insert the new value
    newLine = f"{key}={value}\n"
    contents.insert(index, newLine)
    # Write back the file
    f = open(filePath, "w")
    f.writelines(contents)
    f.close()

if __name__== "__main__":
    main()
