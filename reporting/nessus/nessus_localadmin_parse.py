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

def get_local_admins(i):
    results = {}
    
    for host in get_findings(i):
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        admin_plugin_output = host.findall("ReportItem[@pluginID='10902']/plugin_output")
        for output in admin_plugin_output:
            local_admins = re.findall("([\sa-zA-Z0-9._!%-]+\s\(.+\))", output.text)
            for admin in local_admins:
                # build results dicitonary
                if admin in results:
                    results[admin] += ", "
                    results[admin] += hostname
                else:
                    results[admin] = hostname
    
    # remove default groups
    if "Domain Admins (Group)" in results:
        results.pop("Domain Admins (Group)")
    if "Enterprise Admins (Group)" in results:
        results.pop("Enterprise Admins (Group)")

    # build table
    print("Username|Hosts")
    for u, h in results.items():
        row = "{}|{}".format(u, h)
        print(row)       

def main():
    parser = argparse.ArgumentParser(description="parse .nessus file and produce table of local admins for pasta into word")
    parser.add_argument(
        "-i",
        help=".nessus file or dir containing .nessus files",
        dest="i",
        required=True,
        metavar="input"
    )
    args = parser.parse_args()
    #input_dir = sys.argv[1]
    get_local_admins(args.i)

if __name__ == '__main__':
    main()