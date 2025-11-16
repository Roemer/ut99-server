FROM amd64/ubuntu:latest

# Original Server v436
ADD files/ut-server-linux-436.tar.gz /
# Update to 469e
ADD files/Patches/OldUnreal-UTPatch469e-Linux-x86.tar.bz2 /ut-server/
# Fix for broken maps from the original file
ADD files/Patches/BrokenMapsFix.tar.gz /ut-server/
# Add the bonus packs
ADD files/UTBonusPack* /ut-server/
# Additional Mutators
ADD files/Mutators/* /ut-data/
# Additional Mods
ADD files/Mods/* /ut-data/
# Additional Maps Packed
ADD files/Maps-Packed/* /ut-data/
# Customized Configs
ADD files/Configs/* /ut-data/System/
# Additional Single Maps
ADD files/Maps/* /ut-data/Maps/
# Startup & health scripts
ADD files/Scripts/ /

# Environment variables
ENV UT_SERVERURL="CTF-Face?game=BotPack.CTFGame?mutator=BotPack.InstaGibDM,MVES.MapVote,FlagAnnouncementsV2.FlagAnnouncements"

# Prepare the system
RUN dpkg --add-architecture i386 \
    && apt update \
    && apt install -y nano curl wget python3 jq libx11-6:i386 \
    && rm -rf /var/lib/apt/lists/*

# Create a link of this file to the missing file
RUN ln -s /ut-server/System/libSDL-1.1.so.0 /ut-server/System/libSDL-1.2.so.0

# Run the initial setup
RUN python3 /prepare.py i

EXPOSE 5580/tcp 7777/udp 7778/udp 7779/udp 7780/udp 7781/udp 8777/udp 27500/tcp 27500/udp 27900/tcp 27900/udp
VOLUME /ut-data

# Run the startup script
RUN chmod +x startup.sh
CMD ["/startup.sh"]
HEALTHCHECK --interval=30s --timeout=3s --start-period=1m --retries=3 CMD python3 health.py || exit 1
