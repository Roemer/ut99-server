#!/bin/bash

# Prepare the custom data
python3 /startup.py

# Start the server
/ut-server/ucc server CTF-Face?game=BotPack.CTFGame? ini=UnrealTournament.ini log=ut.log -nohomedir -lanplay