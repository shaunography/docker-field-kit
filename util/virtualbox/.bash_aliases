### VirtualBox ###
windows() {
    VBoxManage startvm "Windows"  --type gui
}

windowsheadless() {
    VBoxManage startvm "Windows"  --type headless
}


snapshotwindows() {
	date=$(date +"%Y%m%d%H%M")
	echo "Current Snapshots"
	VBoxManage snapshot "Windows" list
	echo "Snapshotting Windows VM"
	VBoxManage snapshot "Windows" take $date

}

vmstate() {
	VBoxManage showvminfo "Windows" | grep State | cut -d ":" -f2 | xargs
}
