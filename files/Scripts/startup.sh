#!/bin/bash

# Prepare the custom data
python3 /prepare.py

# Start the server
/ut-server/ucc server $UT_SERVERURL ini=UnrealTournament.ini log=ut.log -nohomedir -lanplay