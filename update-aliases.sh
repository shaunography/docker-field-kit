#!/bin/bash

update-aliases() {
    files=$(find . -name "\.bash\_aliases" -type f)
    for i in $files; do cat $i >> $HOME/.bash_aliases;done
    source ~/.bash_aliases
}

#if [ $1 ]
#then
    if [ -f $HOME/.bash_aliases ]
    then
        rm $HOME/.bash_aliases
        update-aliases
    else
        update-aliases
    fi
#else
#    echo "update-aliases.sh <username>"
#fi
