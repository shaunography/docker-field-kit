### covenant ###
# Run in covenant directory!
alias dcovenant='docker run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v $HOME:$HOME -v $PWD:/app/Data covenant'
