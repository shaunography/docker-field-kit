### theharvester ###
alias dtheharvester='docker run --rm -ti -v $HOME:$HOME -v /media/$USER:/media/$USER theharvester'
alias dtheharvester='docker run --rm -ti -p 8888 --entrypoint /app/restfulHarvest.py theharvester -H 0.0.0.0 -p 8888'
