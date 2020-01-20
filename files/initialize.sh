# Functions
moveAndSymlink() {
    mv "$1" "$2"
    ln -s "$2" "$1"
}

# Preparations
UT_SERVERPATH="/ut-server"
UT_INIPATH="$UT_SERVERPATH/System/UnrealTournament.ini"

# Prepare the directories
mkdir /ut-data
mkdir /ut-data/Maps
mkdir /ut-data/Music
mkdir /ut-data/Sounds
mkdir /ut-data/System
mkdir /ut-data/Textures

# Replace / Add Server information
crudini --set "$UT_INIPATH" 'Engine.GameReplicationInfo' 'ServerName' "$UT_SERVERNAME"
crudini --set "$UT_INIPATH" 'Engine.GameReplicationInfo' 'AdminName' "$UT_ADMINNAME"
crudini --set "$UT_INIPATH" 'Engine.GameReplicationInfo' 'AdminEmail' "$UT_ADMINEMAIL"
crudini --set "$UT_INIPATH" 'Engine.GameReplicationInfo' 'MOTDLine1' "$UT_MOTD1"

#Replace / Add Admin and Game password
crudini --set "$UT_INIPATH" 'Engine.GameInfo' 'AdminPassword' "$UT_ADMINPWD"
crudini --set "$UT_INIPATH" 'Engine.GameInfo' 'GamePassword' "$UT_GAMEPWD"

# Enable the web admin and set username/password
crudini --set "$UT_INIPATH" 'UWeb.WebServer' 'bEnabled' "True"
crudini --set "$UT_INIPATH" 'UWeb.WebServer' 'ListenPort' "5580"
crudini --set "$UT_INIPATH" 'UTServerAdmin.UTServerAdmin' 'AdminUsername' "$UT_WEBADMINUSER"
crudini --set "$UT_INIPATH" 'UTServerAdmin.UTServerAdmin' 'AdminPassword' "$UT_WEBADMINPWD"

# Fix all lines that contain spaces around the equal sign (added by crudini)
sed -i -r "s/(\S*)\s*=\s*(.*)/\1=\2/g" "$UT_INIPATH"

# Add Mutators
## WhoPushedMe
sed -i '/ServerPackages=Botpack/a ServerPackages=EnhancedItems\nServerPackages=WhoPushedMe' "$UT_INIPATH"
## FlagAnnouncementsV2
sed -i '/ServerActors=UWeb.WebServer/a ServerActors=FlagAnnouncementsV2.FlagAnnouncements' "$UT_INIPATH"
sed -i '/ServerPackages=Botpack/a ServerPackages=FlagAnnouncementsV2\nServerPackages=DefaultAnnouncements' "$UT_INIPATH"
# ZeroPingPlus103
sed -i '/ServerPackages=Botpack/a ServerPackages=ZeroPingPlus103' "$UT_INIPATH"
# MapVoteLAv2
sed -i '/ServerPackages=Botpack/a ServerPackages=MapVoteLAv2' "$UT_INIPATH"

# Move and symlink the configs
moveAndSymlink "/ut-server/System/UnrealTournament.ini" "/ut-data/System/UnrealTournament.ini"
moveAndSymlink "/ut-server/System/FlagAnnouncements.ini" "/ut-data/System/FlagAnnouncements.ini"
