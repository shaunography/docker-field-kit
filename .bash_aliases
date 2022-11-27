### update aliases ###
update-aliases() {
    if [ -f $HOME/.bash_aliases ]
    then
        rm $HOME/.bash_aliases
    fi
    files=$(find . -name "\.bash\_aliases" -type f)
    for i in $files; do cat $i >> $HOME/.bash_aliases;done
    source ~/.bash_aliases
}

append-aliases() {
    files=$(find . -name "\.bash\_aliases" -type f)
    for i in $files; do cat $i >> $HOME/.bash_aliases;done
    source ~/.bash_aliases
}

