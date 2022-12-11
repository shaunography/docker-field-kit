### nmap ###
nmap-discovery-fast() {
sudo nmap -sn -T4 -n --open --max-retries 0 --host-timeout 12 -oA nmap-discovery-fast-%Y_%m_%d-%H_%M_%S $*
}

nmap-discovery() {
sudo nmap -PS21-23,25,53,80,110-111,135,139,143,199,443,445,587,993,995,1025,1720,1723,3306,3389,5900,8080,8888 -PE -PP -PM -PU53,69,111,123,137,161,500,514,520 -sn -T4 -n --open -oA nmap-discovery-%Y_%m_%d-%H_%M_%S $*
}

nmap-fast() {
sudo nmap -sV --open -T4 -F -oA nmap-fast-%Y_%m_%d-%H_%M_%S $*
}

nmap-fast-no-ping() {
sudo nmap -sV --open -T4 -F -Pn -oA nmap-fast-no-ping-%Y_%m_%d-%H_%M_%S $*
}

nmap-standard() {
sudo nmap -sV --open -T4 -oA nmap-standard-%Y_%m_%d-%H_%M_%S $*
}

nmap-standard-no-ping() {
sudo nmap -sV --open -T4 -Pn -oA nmap-standard-no-ping-%Y_%m_%d-%H_%M_%S $*
}

nmap-all() {
sudo nmap -sV --open -T4 -p- -oA nmap-all-%Y_%m_%d-%H_%M_%S $*
}

nmap-all-no-ping() {
sudo nmap -sV --open -T4 -p- -Pn -oA nmap-all-no-ping-%Y_%m_%d-%H_%M_%S $*
}

nmap-smb-enum() {
sudo nmap -sV --open -T4 -p U:137,T:139,T:445 --script smb-enum-users,smb-enum-shares,smb-os-discovery,smb-security-mode,smb-mbenum,smb-vuln-* -oA nmap-smb-enum-%Y_%m_%d-%H_%M_%S $*
}

nmap-smb-enum-no-ping() {
sudo nmap -sV --open -T4 -p U:137,T:139,T:445 --script smb-enum-users,smb-enum-shares,smb-os-discovery,smb-security-mode,smb-mbenum,smb-vuln-* -Pn -oA nmap-smb-enum-no-ping-%Y_%m_%d-%H_%M_%S $*
}

nmap-http-default() {
sudo nmap -sV --open -T4 --script http-default-accounts -oA nmap-http-default-%Y_%m_%d-%H_%M_%S $*
}

nmap-http-default-no-ping() {
sudo nmap -sV --open -T4 --script http-default-accounts -Pn -oA nmap-http-default-no-ping-%Y_%m_%d-%H_%M_%S $*
}
