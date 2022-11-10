### shadowsocks ###
# https://github.com/shadowsocks/shadowsocks-libev/blob/master/docker/alpine/Dockerfile

alias dshadowsockslocal='docker run -d \
    -e PASSWORD=keYjSo5BFjHa \
    -e DNS_ADDRS 94.140.14.14,94.140.15.15 \
    -p 8388:8388 \
    -p 8388:8388/udp \
    shadowsocks/shadowsocks-libev \
    '

#alias shadowsocksclient='ss-local -k keYjSo5BFjHa -p 8388 -s 127.0.0.1 -l 1080 -m aes-256-gcm'

alias dshadowsocksairvpnserver='docker run -d --rm \
    --name shadowsocksairvpnserver \
    --network container:airvpn \
    -e PASSWORD=keYjSo5BFjHa \
    -e DNS_ADDRS=94.140.14.14,94.140.15.15 \
    shadowsocks/shadowsocks-libev \
    '
    # port 8388 is exposed via airvpn container.

alias dshadowsockssbuvpnserver='docker run -d --rm \
    --name shadowsockssbuvpnserver \
    --network container:sbuvpn \
    -e PASSWORD=keYjSo5BFjHa \
    -e DNS_ADDRS=94.140.14.14,94.140.15.15 \
    shadowsocks/shadowsocks-libev \
    '
    # port 8388 is exposed via airvpn container.

alias dshadowsocksairvpnclient='docker run -d --rm \
    --name shadowsocksairvpnclient \
    --network container:airvpn \
    shadowsocks/shadowsocks-libev \
    ss-local \
    -k keYjSo5BFjHa \
    -p 8388 \
    -s 127.0.0.1 \
    -b 0.0.0.0 \
    -l 1080 \
    -m aes-256-gcm \
    '
    # port 1080 is exposed via airvpn container.

alias dshadowsockssbuvpnclient='docker run -d --rm\
    --name shadowsockssbuvpnclient \
    --network container:sbuvpn \
    shadowsocks/shadowsocks-libev \
    ss-local \
    -k keYjSo5BFjHa \
    -p 8388 \
    -s 127.0.0.1 \
    -b 0.0.0.0 \
    -l 1080 \
    -m aes-256-gcm \
    '    
    # port 1080 is exposed via sec1vpn container.

