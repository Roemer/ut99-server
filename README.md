# ut99-server
A dockerfile for a fully functional and easy configurable Unreal Tournament 99 server.
This image is based on the original linux server 436 with all four bonus packs and the OldUnreal 469c patch for linux.
It also includes some famous maps and mutators.
All data can be adjusted with a `named volume` (host bind won't work) (see `Usage` for details).

# Usage
Just run the docker image with the following command:
```
docker run --name ut99 -p 5580:5580 -p 7777:7777/udp -p 7778:7778/udp -p 7779:7779/udp -p 7780:7780/udp -p 7781:7781/udp -p 8777:8777/udp -p 27900:27900 -p 27900:27900/udp -v ut99-data:/ut-data roemer/ut99-server:latest
```
Alternatively, you can use compose with the file `docker-compose.yml` and run it:
```
docker compose up
```

This will create and run the container, exposing the web-admin under port 5580 and the game under 7777.
It will also create a docker volume named `ut99-data` which contains all the ini files and non-standard maps and mods.
You can even add your own maps and mods there or edit all the ini files in that volume and restart the server to load the new files or configs.
This basically works by having this files in this volume and on start of the server, all files in the volume are symlinked into the corresponding ut-server folder.

## Environment Variables
| Variable | Mandatory | Description |
| -------- | --------- | ----------- |
| UT_SERVERURL | Yes | This is the default uri for the server startup. By default, it looks like: `CTF-Face?game=BotPack.CTFGame?mutator=BotPack.InstaGibDM,MVES.MapVote,FlagAnnouncementsV2.FlagAnnouncements` |
| UT_SERVERNAME | No | If this variable is set, it will always override the server name in `UnrealTournament.ini` with this on startup. |
| UT_ADMINNAME | No | If this variable is set, it will always override the admin name in `UnrealTournament.ini` with this on startup. |
| UT_ADMINEMAIL | No | If this variable is set, it will always override the admin email in `UnrealTournament.ini` with this on startup. |
| UT_MOTD1 | No | If this variable is set, it will always override the MOTD1 in `UnrealTournament.ini` with this on startup. |
| UT_DOUPLINK | No | If this variable is set, it will always override the DoUpLink in `UnrealTournament.ini` with this on startup. Default is `true`.|
| UT_ADMINPWD | No | If this variable is set, it will always override the admin password in `UnrealTournament.ini` with this on startup. |
| UT_GAMEPWD | No | If this variable is set, it will always override the game password in `UnrealTournament.ini` with this on startup. |
| UT_WEBADMINUSER | No | If this variable is set, it will always override the web admin username in `UnrealTournament.ini` with this on startup. |
| UT_WEBADMINPWD | No | If this variable is set, it will always override the web admin password in `UnrealTournament.ini` with this on startup. |
| UT_MINPLAYERS_DM | No | Set the minimum number of players in DeathMatchPlus.
| UT_MINPLAYERS_CTF | No | Set the minimum number of players in CTF.
| UT_MAXPLAYERS | No | Set the max number of players.
| UT_INITIALBOTS_DM | No | Set the initial number of bots in DeathMatchPlus.
| UT_INITIALBOTS_CTF | No | Set the initial number of bots in CTF.

## Volumes
As mentioned above, there is one named volume that should point to `/ut-data` in the container.
This folder contains all important folders (`Maps`, `Music`, `Sounds`, `System`, `Textures`) where any non-standard files can be placed and will be loaded on the next restart of the server/container.
Also all ini files can be found there in the `System` folder so they can be adjusted as well.

# Included Mods and Mutators

## BunnyTrack
BunnyTrack is ready to use. Change the GameType to it to use it.

## ChaosUT
ChaosUT and a few maps are added. Change the GameType to it to use it.

## CustomCrossHairScale
This mod is loaded permanently. It allows to scale the crosshair as it might be too big on some resolutions.
Any player can just go to their console (tab) and execute the following command:
`mutate ch_scale 1`
Note: Usually fails for weapons with a secondary crosshair like sniper, so it is mostly only usefull for InstaGib.

## FlagAnnouncementsV2
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mod is enabled, there is a voice that tells if and which flag is taken/dropped/returned.
Further configuration can be done in the `System/FlagAnnouncements.ini` file.

## InstaGibPlus
Better InstaGib.
Thanks to: https://github.com/utspect/InstaGibPlus

## KickIdlePlayers2
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mod is enabled, inactive users will be kicked from the server.
Further configuration can be done in the `System/KickIdlePlayers2.ini` file.

## MonsterHunt
MonsterHunt and a few maps are added. Change the GameType to it to use it.

## MVE - Map Vote Extended
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mode is enabled, a map vote / kick screen will come after each map so the users can vote for the next map.
You can start a vote anytime by saying `!v`.
IF you login as admin with `adminlogin <password>` you see an additional admin tab.
Thanks to the author: https://github.com/peterekepeter/ut99-mves
Further configuration can be done in the `System/MVE_Config.ini` file.

## VoteSys
An alternative map voting. Still in testing phase.
Thanks to the author: https://github.com/Deaod/VoteSys

## NoSelfDamagev03
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mod is enabled, self damage (for example from rocket launchers) can be disabled.
Further configuration can be done in the `System/NoSelfDamage.ini` file.

## SLV - StrangeLove v2.05
SLV, or Strangelove, is a mod inspired by the film Dr. Strangelove where redeemers are replaced with missiles that a player can use to fly around a map.

## WhoPushedMe
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mode is enabled, detects if someone is killed because someone else pushed/hit them and they fell to their death and grants the killer the corresponding points (or negative points when a teammate is killed).

## ZeroPingPlus103
This mod is added as a mutator. So it must be added to the mutators list to work.
When this mod is enabled, the clientside calculates if a hit was a hit or not and tells this the server, effectively leading to 0 ping.
