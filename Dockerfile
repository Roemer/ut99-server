FROM i386/ubuntu:18.04

# Prepare the system
RUN apt-get update && \
    apt-get install -y nano python3 libx11-6 libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Original Server v436
ADD files/ut-server-linux-436.tar.gz /
# Update to 451
ADD files/Patches/UTPGPatch451LINUX.tar.gz /ut-server/
# Fix for broken maps from the original file
ADD files/Patches/BrokenMapsFix.tar.gz /ut-server/
# Add the bonus packs
ADD files/UTBonusPack1.tar.gz /ut-server/
ADD files/UTBonusPack2.tar.gz /ut-server/
ADD files/UTBonusPack3.tar.gz /ut-server/
ADD files/UTBonusPack4.tar.gz /ut-server/
# Mutators
ADD files/Mutators/FlagAnnouncementsV2.tar.gz /ut-server/
ADD files/Mutators/MapVoteLAv2.tar.gz /ut-server/
ADD files/Mutators/WhoPushedMe.tar.gz /ut-server/
ADD files/Mutators/ZeroPingPlus103.tar.gz /ut-server/
# Maps Packed
ADD files/Maps-Packed/CTF-Bollwerk109.tar.gz /ut-server/
# Maps
ADD files/Maps/CTF-AceOfSpace.unr /ut-server/Maps/
ADD files/Maps/CTF-AllYourW00t.unr /ut-server/Maps/
ADD files/Maps/CTF-andACTION.unr /ut-server/Maps/
ADD files/Maps/CTF-EternalCommandv2.unr /ut-server/Maps/
ADD files/Maps/CTF-Frostburn][[].unr /ut-server/Maps/
ADD files/Maps/CTF-Lucius.unr /ut-server/Maps/
ADD files/Maps/CTF-MarsDuo.unr /ut-server/Maps/
ADD files/Maps/CTF-Niven.unr /ut-server/Maps/
ADD files/Maps/CTF-Schmall.unr /ut-server/Maps/
ADD files/Maps/CTF-Visse.unr /ut-server/Maps/
ADD files/Maps/DM-Dexterity.unr /ut-server/Maps/
# Startup scripts
ADD files/Scripts/startup.sh /
ADD files/Scripts/prepare.py /

# Environment variables
ENV UT_SERVERURL="CTF-Face?game=BotPack.CTFGame?mutator=BotPack.InstaGibDM,MapVoteLAv2.BDBMapVote"

# Create a link of this file to the missing file
RUN ln -s /ut-server/System/libSDL-1.1.so.0 /ut-server/System/libSDL-1.2.so.0

EXPOSE 27900/udp 5580/tcp 7777/udp 7778/udp 7779/udp 7780/udp 7781/udp

RUN python3 /prepare.py i

CMD ["/startup.sh"]
