#!/bin/bash

# default allow
#ufw default allow outgoing
#
#rules_to_del=$(sudo ufw status numbered | grep "ALLOW OUT" | grep -o '\[.*\]' | grep -o '[0-9]*')
#for i in $rules_to_del
#do ufw delete $i
#done
#
#ufw status verbose

ufw reset
ufw enable

ufw default reject incoming
ufw default allow outgoing

# allow syncthing
ufw allow 22000
ufw allow 22000/udp
ufw allow 21027/udp

# allow ssh
if [ $(hostname) = "thor" ]
	then
		ufw allow ssh
fi

if [ $(hostname) = "odin" ]
	then
		ufw allow ssh
fi


# allow Bittorrent
if [ $(hostname) = "thor" ]
	then
		ufw allow 61618
		ufw allow 61618/udp
fi
