alias dgobuster='docker run --network host --rm -ti -v ~:/home/$(whoami) -v /media:/media gobuster'

dgobuster_common() {
	docker run --network host --rm -ti -v ~:/home/$(whoami) -v /media:/media gobuster dir -w /media/shaun/data/field-kit/wordlists/SecLists/Discovery/Web-Content/common.txt -u $*
}

dgobuster_raft() {
	docker run --network host --rm -ti -v ~:/home/$(whoami) -v /media:/media gobuster dir -w /media/shaun/data/field-kit/wordlists/SecLists/Discovery/Web-Content/raft-medium-directories.txt -u $*
}
