### deluge ###
alias ddeluge="docker run -d \
  --name=deluge \
  -e PUID=$(id -u) \
  -e PGID=$(id -u) \
  -e TZ=Europe/London \
  --network container:airvpn \
  -v /media/$USER/media/.deluge:/config \
  -v /media/$USER/media:/media/$USER/media \
  lscr.io/linuxserver/deluge \
  "
# ports are specified in airvpn container

