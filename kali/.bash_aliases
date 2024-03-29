## kali ##
dkali-rolling() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        else
		docker run -ti --rm --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        fi
}

dkali() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		docker run -ti --rm --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

dkali-rolling-x11() {
        if [ $1 ]
        then
		docker run -ti --name $1 -e DISPLAY=$DISPLAY --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kalilinux/kali-rolling
        else
		docker run -ti --rm -e DISPLAY=$DISPLAY --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kalilinux/kali-rolling
        fi
}

dkali-x11() {
        if [ $1 ]
        then
		docker run -ti --name $1 -e DISPLAY=$DISPLAY --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority kali
        else
		docker run -ti --rm -e DISPLAY=$DISPLAY --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media -v $XAUTHORITY:/root/.Xauthority  kali
        fi

}

dkali_sbu() {
        if [ $1 ]
        then
		docker run -ti --name $1 --network container:sbuvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		docker run -ti --rm --network container:sbuvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

dkali_air() {
        if [ $1 ]
        then
                docker run -ti --name $1 --network container:airvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
                docker run -ti --rm --network container:airvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

pkali-rolling() {
        if [ $1 ]
        then
		sudo podman run -ti --security-opt label=disable --name $1 --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        else
		sudo podman run -ti --security-opt label=disable --rm --network host -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kalilinux/kali-rolling
        fi
}

pkali() {
        if [ $1 ]
        then
		sudo podman run -ti --security-opt label=disable --name $1 --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		sudo podman run -ti --security-opt label=disable --rm --network host --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

pkali_sbu() {
        if [ $1 ]
        then
		sudo podman run -ti --security-opt label=disable --name $1 --network container:sbuvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
		sudo podman run -ti --security-opt label=disable --rm --network container:sbuvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

pkali_air() {
        if [ $1 ]
        then
                sudo podman run -ti --security-opt label=disable --name $1 --network container:airvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        else
                sudo podman run -ti --security-opt label=disable --rm --network container:airvpn --privileged -v $HOME:$HOME -v /tmp:/tmp -v /media:/media kali
        fi

}

