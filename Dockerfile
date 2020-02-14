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
ADD files/UTBonusPack* /ut-server/
# Startup scripts
ADD files/Scripts/startup.sh /
ADD files/Scripts/prepare.py /

# Additonal Mutators
ADD files/Mutators/* /ut-data/
# Additonal Maps Packed
ADD files/Maps-Packed/* /ut-data/
# Maps
ADD files/Maps/* /ut-data/Maps/

# Environment variables
ENV UT_SERVERURL="CTF-Face?game=BotPack.CTFGame?mutator=BotPack.InstaGibDM,MapVoteLAv2.BDBMapVote,FlagAnnouncementsV2.FlagAnnouncements"

# Create a link of this file to the missing file
RUN ln -s /ut-server/System/libSDL-1.1.so.0 /ut-server/System/libSDL-1.2.so.0

EXPOSE 27900/udp 5580/tcp 7777/udp 7778/udp 7779/udp 7780/udp 7781/udp

RUN python3 /prepare.py i

VOLUME /ut-data

RUN chmod +x startup.sh

CMD ["/startup.sh"]
