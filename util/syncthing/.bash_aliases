### syncthing ###
#alias dsyncthing='docker run -d --restart unless-stopped -p 127.0.0.1:8384:8384 -p 22000:22000/tcp -p 22000:22000/udp -p 21027:21027/udp --name syncthing -e PUID=1000 -e PGID=1000 -e TZ=Europe/London -v $HOME:$HOME -v /media/$USER:/media/$USER -v ~/.syncthing/config:/config linuxserver/syncthing'
alias dsyncthing='docker run -d --restart unless-stopped --network host --name syncthing -e PUID=1000 -e PGID=1000 -e TZ=Europe/London -v $HOME:$HOME -v /media/$USER:/media/$USER -v $HOME/.syncthing/config:/config linuxserver/syncthing'
