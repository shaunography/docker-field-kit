dfirefox() {
    if [ $1 ]
      then
  	  	x11docker --network=container:$1 -c --home --name firefox jess/firefox
      else
		    x11docker -I --home -c --name firefox jess/firefox
    fi
}