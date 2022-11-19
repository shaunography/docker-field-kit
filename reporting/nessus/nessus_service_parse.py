#!/usr/bin/python3
import argparse
import sys
import xml.etree.ElementTree
import os
import re

#def get_findings(i):
#    try:
#        for file in os.listdir(i):
#            if file.endswith(".nessus"):
#                scan =  os.path.join(i, file)
#                nessus = xml.etree.ElementTree.parse(scan).getroot()
#                findings = nessus.findall("Report/ReportHost")
#                for finding in findings:
#                    yield finding
#    except NotADirectoryError:
#        if i.endswith(".nessus"):
#            nessus = xml.etree.ElementTree.parse(scan).getroot()
#            findings = nessus.findall("Report/ReportHost")
#            for finding in findings:
#                yield finding
#    except:
#        print("invalid input file or dir")
#        print("supply path to .nessus file or directory containing .nessus files")

def get_findings(i):
    if i.endswith(".nessus"):
        nessus = xml.etree.ElementTree.parse(i).getroot()
        findings = nessus.findall("Report/ReportHost")
        for finding in findings:
            yield finding
    else:
        for file in os.listdir(i):
            if file.endswith(".nessus"):
                scan =  os.path.join(i, file)
                nessus = xml.etree.ElementTree.parse(scan).getroot()
                findings = nessus.findall("Report/ReportHost")
                for finding in findings:
                    yield finding 

def main():
    parser = argparse.ArgumentParser(description="Parse .nessus file for services")
    parser.add_argument(
        "-i",
        help=".nessus file or dir containing .nessus files",
        dest="i",
        required=True,
        metavar="input"

    ),
    parser.add_argument(
        "-o",
        help="output dir",
        dest="o",
        required=True,
        metavar="output"
    )
    args = parser.parse_args()
    #input_dir = sys.argv[1]
    
    services = {
        "10342" : "vnc",
        "10267" : "ssh",
        "11011" : "smb",
        "10394" : "smb_null",
        "10144" : "mssql",
        "10719" : "mysql",
        "22073" : "oracle",
        "26024" : "pgsql",
        "35296" : "snmp",
        "10281" : "telnet",
        "108804" : "exchange",
        "77910" : "exchange_server_installed",
        "10940" : "terminal_services",
        "10092" : "ftp",
        "65914" : "mongodb",
        "81777" : "mongodb_noauth",
        "43829" : "kerberos",
        "10223" : "rpc_portmapper",
        "39446" : "tomcat",
        "24260" : "http",
        "10395" : "shares",
        "42411" : "readable_shares",
        "48204" : "apache",
        "10205" : "rlogin",
        "29700" : "iscsi",
        "51368" : "iscsi_noauth",
        "10437" : "nfs",
        "10437" : "nfs_readable",
        "124029" : "docker_api",
        "10407" : "Xserver",
        "11002" : "dns",
        "20870" : "ldap",
        "10762" : "rtsp",
        "22227" : "rmi_registry",
        "105161" : "cisco_smart_install",
        "100635" : "redis",
        "72063" : "ipmi",
        "53337" : "jboss_jmx_console_bypass",
        "46181" : "jboss_web_console_bypass",
        "151440" : "spooler_service",
        "97833" : "ms17-010",
        "125313" : "bluekeep"
    }
    
    results_ips = {}
    results_hostnames = {}
    results_urls = {}
    results_kerb = []
    results_relay = []
    results_all_shares = []
    results_readable_shares = []
    results_writable_shares = []
    
    for host in get_findings(args.i):
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        try:
            ip = host.find("HostProperties/tag[@name='host-ip']").text
        except AttributeError:
            pass
            #hostname = host.find("HostProperties/tag[@name='hostname']").text
            #netbios_name = host.find("HostProperties/tag[@name='netbios-name']").text
            #host_fqdn = host.find("HostProperties/tag[@name='host-fqdn']").text
        else:
            for item in host.iter("ReportItem"):
                plugin_name = item.attrib["pluginName"]
                plugin_id = item.attrib["pluginID"]
                port = item.attrib["port"]
                
                # get ips
                if plugin_id in services:
                    if services[plugin_id] in results_ips:
                        results_ips[services[plugin_id]] += [ip]
                    else:
                        results_ips[services[plugin_id]] = [ip]

                # get hostnames
                if plugin_id in services:
                    if services[plugin_id] in results_hostnames:
                        results_hostnames[services[plugin_id]] += ["{}({})".format(hostname, ip)]
                    else:
                        results_hostnames[services[plugin_id]] = ["{}({})".format(hostname, ip)]

                # http, apache, tomcat
                if plugin_id in ["24260", "48204", "39446"]:
                    plugin_output = item.find("plugin_output").text
                    if plugin_output != None:
                        if re.search("SSL\s:\sno", plugin_output):
                            url = "http://{}:{}/".format(ip, port)
                        else:
                            url = "https://{}:{}/".format(ip, port)
                    
                    if services[plugin_id] in results_urls:
                        results_urls[services[plugin_id]] += [url]
                    else:
                        results_urls[services[plugin_id]] = [url]
                    
                # kerb
                if plugin_id == "43829":
                    plugin_output = item.find("plugin_output").text
                    try:
                        realm = re.search("Realm\s+:\s(.*)", plugin_output)[1]
                    except TypeError:
                        pass
                    else:
                        results_kerb += ["{}\{} ({})".format(realm, hostname, ip)]

                # smb relay
                if plugin_id == "57608":
                    results_relay += [ip]

                # readable and writable smb shares
                if plugin_id == "42411":
                    plugin_output = item.find("plugin_output").text
                    readable_shares = re.findall("-\s([+$=A-Za-z0-9_-]+)\s.*\s\(readable\)", plugin_output)
                    writable_shares = re.findall("-\s([+$=A-Za-z0-9_-]+)\s.*\s\(writable\)", plugin_output)
                    results_readable_shares += [ '\\\\{}\\{}'.format(hostname, i) for i in readable_shares ]
                    results_writable_shares += [ '\\\\{}\\{}'.format(hostname, i) for i in writable_shares ]
                
                # all shares
                if plugin_id == "10395":
                    plugin_output = item.find("plugin_output").text
                    shares = re.findall("-\s(.*)", plugin_output)
                    results_all_shares += [ '\\\\{}\\{}'.format(hostname, i) for i in shares ]


    # ips
    for service, ips in results_ips.items():
        file_name = "{}_ips.txt".format(service)
        file_path = os.path.join(args.o, file_name)
        with open(file_path, 'w') as f:
            # convert ip list to a set to uniq it when paesing multiple scans
            uniq_ips = set(ips)
            for ip in uniq_ips:
                f.write(ip + "\n")
    # hostnames
    for service, hosts in results_hostnames.items():
        file_name = "{}_hosts.txt".format(service)
        file_path = os.path.join(args.o, file_name)
        with open(file_path, 'w') as f:
            # convert ip list to a set to uniq it when paesing multiple scans
            uniq_hosts = set(hosts)
            for host in uniq_hosts:
                f.write(host + "\n")
    # urls
    for service, urls in results_urls.items():
        file_name = "{}_urls.txt".format(service)
        file_path = os.path.join(args.o, file_name)
        with open(file_path, 'w') as f:
            # convert ip list to a set to uniq it when paesing multiple scans
            uniq_urls = set(urls)
            for url in uniq_urls:
                f.write(url + "\n")
    # kerb
    file_name = "kerberos.txt"
    file_path = os.path.join(args.o, file_name)
    with open(file_path, 'w') as f:
        for k in results_kerb:
            f.write(k + "\n")

    # smb relay
    file_name = "smb_relay_ips.txt"
    file_path = os.path.join(args.o, file_name)
    with open(file_path, 'w') as f:
        for k in results_relay:
            f.write(k + "\n")
    
    # shares
    file_name = "smb_all_shares.txt"
    file_path = os.path.join(args.o, file_name)
    with open(file_path, 'w') as f:
        for s in results_all_shares:
            f.write(s + "\n")
    file_name = "smb_readable_shares.txt"
    file_path = os.path.join(args.o, file_name)
    with open(file_path, 'w') as f:
        for r in results_readable_shares:
            f.write(r + "\n")
    file_name = "smb_writable_shares.txt"
    file_path = os.path.join(args.o, file_name)
    with open(file_path, 'w') as f:
        for w in results_writable_shares:
            f.write(w + "\n")

if __name__ == '__main__':
    main()