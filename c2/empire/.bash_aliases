alias dempire_server='docker run --rm -it --network host -v $HOME:$HOME -v /media:/media -v /tmp:/tmp --entrypoint powershell-empire empire server'
alias dempire_client='docker run --rm -it --network host -v $HOME:$HOME -v /media:/media -v /tmp:/tmp --entrypoint powershell-empire empire client'

