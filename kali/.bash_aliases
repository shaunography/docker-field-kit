## kali ##
dkali-rolling() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network host -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        else
		docker run -ti --rm --network host -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        fi
}

dkali() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network host --privileged -v $HOME/Docker:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		docker run -ti --rm --network host --privileged -v $HOME/Docker:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

dkali-rolling-x11() {
        if [ $1 ]
        then
		docker run -ti --name $1 -e DISPLAY=$DISPLAY --network host -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kalilinux/kali-rolling
        else
		docker run -ti --rm -e DISPLAY=$DISPLAY --network host -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kalilinux/kali-rolling
        fi
}

dkali-x11() {
        if [ $1 ]
        then
		docker run -ti --name $1 -e DISPLAY=$DISPLAY --network host --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kali
        else
		docker run -ti --rm -e DISPLAY=$DISPLAY --network host --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority  kali
        fi

}

dkali_sbu() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network container:sbuvpn --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		docker run -ti --rm --network container:sbuvpn --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

dkali_air() {
        if [ $1 ]
        then
                docker run -ti --name $1 --network container:airvpn --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kali
        else
                docker run -ti --rm --network container:airvpn --privileged -v $HOME/Docker/kali:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}
