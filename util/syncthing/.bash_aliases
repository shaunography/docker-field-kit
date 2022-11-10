### syncthing ###
alias dsyncthing='docker run -d --restart unless-stopped --network host --name syncthing -e PUID=1000 -e PGID=1000 -e TZ=Europe/London -v $HOME:$HOME -v /media/$USER:/media/$USER -v ~/.syncthing/config:/config linuxserver/syncthing'
