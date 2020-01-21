FROM i386/ubuntu:18.04

# Prepare the system
RUN apt-get update && \
    apt-get install -y nano python3 crudini libx11-6 libxext6 && \
    rm -rf /var/lib/apt/lists/*

ENV UT_SERVERNAME="My UT Server"
ENV UT_ADMINNAME="UTAdmin"
ENV UT_ADMINEMAIL="no@one.com"
ENV UT_MOTD1="Have Fun"
ENV UT_ADMINPWD="admin"
ENV UT_GAMEPWD=""
ENV UT_WEBADMINUSER="admin"
ENV UT_WEBADMINPWD="admin"

# Original Server v436
ADD ut-server-linux-436.tar.gz /
# Update to 451
ADD Patches/UTPGPatch451LINUX.tar.gz /ut-server/
# Fix for broken maps from the original file
ADD Patches/BrokenMapsFix.tar.gz /ut-server/
# Add the bonus packs
ADD UTBonusPack1.tar.gz /ut-server/
ADD UTBonusPack2.tar.gz /ut-server/
ADD UTBonusPack3.tar.gz /ut-server/
ADD UTBonusPack4.tar.gz /ut-server/
# Mutators
ADD Mutators/FlagAnnouncementsV2.tar.gz /ut-server/
ADD Mutators/MapVoteLAv2.tar.gz /ut-server/
ADD Mutators/WhoPushedMe.tar.gz /ut-server/
ADD Mutators/ZeroPingPlus103.tar.gz /ut-server/
# Maps Packed
ADD Maps-Packed/CTF-Bollwerk109.tar.gz /ut-server/
# Maps
ADD Maps/CTF-AceOfSpace.unr /ut-server/Maps/
ADD Maps/CTF-AllYourW00t.unr /ut-server/Maps/
ADD Maps/CTF-andACTION.unr /ut-server/Maps/
ADD Maps/CTF-EternalCommandv2.unr /ut-server/Maps/
ADD Maps/CTF-Frostburn][[].unr /ut-server/Maps/
ADD Maps/CTF-Lucius.unr /ut-server/Maps/
ADD Maps/CTF-MarsDuo.unr /ut-server/Maps/
ADD Maps/CTF-Niven.unr /ut-server/Maps/
ADD Maps/CTF-Schmall.unr /ut-server/Maps/
ADD Maps/CTF-Visse.unr /ut-server/Maps/
ADD Maps/DM-Dexterity.unr /ut-server/Maps/
# Startup scripts
ADD Scripts/initialize.sh /
ADD Scripts/startup.sh /
ADD Scripts/startup.py /

# Create a link of this file to the missing file
RUN ln -s /ut-server/System/libSDL-1.1.so.0 /ut-server/System/libSDL-1.2.so.0

EXPOSE 27900/udp 5580/tcp 7777/udp 7778/udp 7779/udp 7780/udp 7781/udp

RUN "/initialize.sh"

CMD ["/startup.sh"]
