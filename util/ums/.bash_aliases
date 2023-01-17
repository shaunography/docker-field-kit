### universal media server ###
alias dums='docker run -it -p 5002:5002 -p 9001:9001 --network host -v /media/$USER/media/:/media -v ~/.config:/root/.config universalmediaserver/ums'

