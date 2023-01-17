### tailscale ###
alias dtailscale='docker run -d --name=tailscaled -v /var/lib:/var/lib -v /dev/net/tun:/dev/net/tun --network=host --privileged tailscale/tailscale tailscaled'
alias dtailscale_status='docker exec tailscaled tailscale status'
alias dtailscale_up='docker exec tailscaled tailscale up'
