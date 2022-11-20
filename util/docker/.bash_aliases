### Docker ###
alias dps='docker ps -a'
alias dis='docker images'
alias dis_clean='docker rmi $(docker images | grep "<none>" | grep -o "[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]")'

