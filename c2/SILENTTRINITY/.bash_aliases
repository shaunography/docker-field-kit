### SILENTTRINITY ###
alias dsilentteamserver='docker run -it --network host --name silenttrinity -v $HOME:$HOME -v /media/$USER:/media/$USER silenttrinity teamserver localhost mysuperlongsecretpassword'
alias dsilentclient='docker run --rm -it --network host -v $HOME:$HOME -v /media/$USER:/media/$USER -v /tmp/:/tmp/ silenttrinity client wss://shaun:mysuperlongsecretpassword@127.0.0.1:5000'
