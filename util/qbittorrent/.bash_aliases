### qbittorrent ###
alias dqbittorrent="docker run -d \
    --name qbittorrent \
    --network container:airvpn \
    -e PUID=$(id -u) \
    -e PGID=$(id -u) \
    -e TZ=Europe/London \
    -e WEBUI_PORT=8888 \
    -v /media/$USER/media/.qbittorrent:/config \
    -v /media/$USER/media:/media/$USER/media \
    lscr.io/linuxserver/qbittorrent \
    " 
# ports are specified in airvpn container

