### python ###
alias dpythonservehere='docker run --rm -ti -p 1337:1337 -v "${PWD}:/tmp/serve" python:slim python -m http.server --directory /tmp/serve 1337'
alias dpython='docker run --rm -ti -v $HOME:$HOME -v /media/$USER:/media/$USER python:slim'
