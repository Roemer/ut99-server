#!/bin/bash

# Prepare the custom data
python3 /prepare.py

# Start the server
cd /ut-server/System
./ucc-bin-x86 server $UT_SERVERURL ini=UnrealTournament.ini log=ut.log -nohomedir -lanplay
