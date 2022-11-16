#!/usr/bin/python3
import argparse
import sys
import xml.etree.ElementTree
import os
#import re
#import openpyxl

def dump_names(findings, filename):
    names = []
    for host in findings:
        for item in host.iter("ReportItem"):
            if item.find("risk_factor").text == "None":
                # ignore infos
                pass
            else:
                names += [item.attrib["pluginName"]]
    
    with open(filename, 'w') as f:
        names_uniq = set(names)
        for i in names_uniq:
            f.write(i + "\n")


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

    if not os.path.exists(args.o):
        print("aggregation dir does not exist, creating it for you")
        os.makedirs(args.o)  
    
    dump_names(get_findings(args.i), os.path.join(args.o, "plugin_names.lst"))

if __name__ == '__main__':
    main()
