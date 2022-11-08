## Kali ##
dkali-wireless() {
        if [ $1 ]
        then
                docker run -ti --name $1 --network host -v $HOME:$HOME -v /media:/media kali-wireless
        else
                docker run -ti --rm --network host -v $HOME:$HOME -v /media:/media kali-wireless
        fi
}
