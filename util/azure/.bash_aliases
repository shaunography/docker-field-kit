### Azure ###
alias dazure-cli='docker run --rm -ti -v ~/.azure/:/root/.azure/ -v $HOME:$HOME -v /media/$USER:/media/$USER mcr.microsoft.com/azure-cli:latest'
alias dazure-powershell='docker run --rm -ti -v ~/.azure/:/root/.azure/ -v $HOME:$HOME -v /media/$USER:/media/$USER mcr.microsoft.com/azure-powershell'
