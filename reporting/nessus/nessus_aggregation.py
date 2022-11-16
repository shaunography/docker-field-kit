#!/usr/bin/python3
import argparse
import sys
import xml.etree.ElementTree
import os
import re
#import openpyxl

client_software = {
    "Apple Software Update" : "(?:^Apple\SSoftware\SUpdate\s.*)(?!.*Unsupported.*)",
    "Foxit 3D Plugin" : "(?:^Foxit\s3D\sPlugin.*)(?!.*Unsupported.*)",
    "Adobe Flash Player" : "(?:^Adobe\sFlash\sPlayer\s.*)(?!.*Unsupported.*)",
    "Adobe AIR" : "(?:^Adobe\sAIR\s.*)(?!.*Unsupported.*)",
    "Adobe Acrobat" : "(?:^Adobe\sAcrobat.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "Adobe Reader" : "(?:^Adobe\sReader.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "Adobe InDesign" : "(?:^Adobe\sInDesign\s.*)(?!.*Installed.*)(?!.*Unsupported.*)",
    "Adobe Creative Cloud" : "(?:^Adobe\sCreative\sCloud\sDesktop.*)(?!.*Unsupported.*)",
    "Adobe After Effects" : "(?:^Adobe\sAfter\sEffects.*)(?!.*Unsupported.*)",
    "Adobe Photoshop" : "(?:^Adobe\sPhotoshop\s.*)(?!.*Unsupported.*)",
    "Adobe Illustrator" : "(?:^Adobe\sIllustrator\s.*)(?!.*Unsupported.*)",
    "Adobe Shockwave Player" : "(?:^Adobe\sShockwave\sPlayer\s.*)(?!.*Unsupported.*)",
    "Adobe Bridge" : "(?:^Adobe\sBridge\sCC\s.*)(?!.*Unsupported.*)",
    "Adobe SVG Viewer" : "(?:^Adobe\sSVG\sViewer\s.*)(?!.*Unsupported.*)",
    "Adobe Premiere Pro" : "(?:^Adobe\sPremiere\sPro\s.*)(?!.*Unsupported.*)",
    "Adobe Media Encoder" : "(?:^Adobe\sMedia\sEncoder\s.*)(?!.*Unsupported.*)",
    "Adobe Prelude" : "(?:^Adobe\sPrelude\s.*)(?!.*Unsupported.*)",
    "Adobe Digital Editions" : "(?:^Adobe\sDigital\sEditions\s.*)(?!.*Unsupported.*)",
    "Adobe Premiere Rush" : "(?:^Adobe\sPremiere\sRush\s.*)(?!.*Unsupported.*)",
    "Shibboleth" : "(?:^Shibboleth\s.*)(?!.*Unsupported.*)",
    "Oracle Java" : "(?:^Oracle\sJava\s.*)(?!.*Unsupported.*)|(?:^Sun\sJava\s.*)(?!.*Unsupported.*)",
    "Mozilla Firefox" : "(?:^Mozilla\sFirefox\s.*)(?!.*Unsupported.*)|(?:^Firefox\s.*)(?!.*Unsupported.*)",
    "Microsoft Office" : "^Security\sUpdates.*Office.*",
    "VLC Media Player" : "(?:^VLC.*Vulnerabilities.*)(?!.*Unsupported.*)|(?:^VLC\sMedia\sPlayer\s.*)(?!.*Unsupported.*)",
    "Apple iTunes" :"(?:^Apple\siTunes.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "7-Zip" : "(?:^7-[Zz]ip\s<\s)(?!.*Unsupported.*)",
    "Autodesk" : "(?:^Autodesk\s.*)(?!.*Unsupported.*)",
    "Veritas Backup" : "(?:^Veritas.*)(?!.*Unsupported.*)",
    "HPE Smart" : "(?:^HPE\sSmart\s.*)(?!.*Unsupported.*)",
    "Symantec Enpoint Protection" : "(?:^Symantec\sEndpoint\sProtection\s)(?!.*Unsupported.*)",
    "Wireshark" : "(?:^Wireshark.*)(?!.*Unsupported.*)",
    "WinRAR" : "(?:^RARLAB\sWinRAR.*)(?!.*Unsupported.*)",
    "Google Chrome" : "(?:^Google\sChrome.*)(?!.*Unsupported.*)",
    "Evernote" : "(?:^Evernote.*)(?!.*Unsupported.*)",
    "Oracle Document Capture" : "(?:^Oracle\sDocument\sCapture.*)(?!.*Unsupported.*)",
    "Oracle VM VirtualBox" : "(?:^Oracle\sVM\sVirtualBox.*)(?!.*Unsupported.*)",
    "Git for Windows" : "(?:^Git\sfor\sWindows.*)(?!.*Unsupported.*)",
    "VMware Tools" : "(?:^VMware\sTools.*)(?!.*Unsupported.*)",
    "VMware vSphere Client" : "(?:^VMware\svSphere\sClient.*)(?!.*Unsupported.*)",
    "VMware Workstation" : "(?:^VMware\sWorkstation\s.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "VMware Horizon View Client" : "(?:^VMware\sHorizon\sView\sClient.*)(?!.*Unsupported.*)",
    "Fortinet Forticlient" : "(?:^Fortinet\sFortiClient.*)(?!.*Unsupported.*)",
    "SolarWinds Dameware Mini Remote Control" : "(?:^SolarWinds\sDameware\sMini\sRemote\sControl)(?!.*Unsupported.*)",
    "Zoom Client" : "(?:^Zoom\sClient.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "Artifex Ghostscript" : "(?:^Artifex\sGhostscript.*)(?!.*Unsupported.*)",
    "ImageMagick" : "(?:^ImageMagick\s.*)(?!.*Unsupported.*)",
    "EasyMail SMTP" : "(?:^EasyMail\sSMTP.*)(?!.*Unsupported.*)",
    "Microsoft Visual Studio Code" : "(?:Microsoft\sVisual\sStudio\sCode)(?!.*Unsupported.*)",
    "Microsoft Visual Studio" : "(?:Microsoft\sVisual\sStudio)(?!.*Visual\sStudio\sCode.*)(?!.*Unsupported.*)",
    "Microsoft Teams" : "(?:^Microsoft\sTeams\s.*)(?!.*Unsupported.*)",
    "Data Dynamics ActiveBar" : "(?:^Data\sDynamics\sActiveBar.*)(?!.*Unsupported.*)",
    "KeyWorks KeyHelp ActiveX Control" : "(?:^KeyWorks\sKeyHelp\sActiveX\sControl\s.*)(?!.*Unsupported.*)",
    "HP Version Control Agent" : "(?:^HP\sVersion\sControl\sAgent\s.*)(?!.*Unsupported.*)",
    "HP Insight Management Agent" : "(?:^HP\sInsight\sManagement\sAgents\s.*)(?!.*Unsupported.*)",
    "Apple Software Update" : "(?:^Apple\sSoftware\sUpdate\s.*)(?!.*Unsupported.*)",
    "FlexCell Grid FlexCell.Grid ActiveX Control" : "(?:^FlexCell\sGrid\s.*)(?!.*Unsupported.*)",
    "OpenOffice" : "(?:.*OpenOffice\s.*)(?!.*Unsupported.*)",
    "LibreOffice" : "(?:^LibreOffice\s.*)(?!.*Unsupported.*)",
    "Cisco AnyConnect" : "(?:^Cisco\sAnyConnect\sSecure\s.*)(?!.*Unsupported.*)",
    "Cisco WebEx" : "(?:^Cisco\sWeb[eE]x\s.*)(?!.*Unsupported.*)",
    "Cisco VPN CLient" : "(?:^Cisco\sVPN\sClient.*)(?!.*Unsupported.*)",
    "IBM Tivoli Storage Manager Client" : "(?:^IBM\sTivoli\sStorage\sManager\sClient\s.*)(?!.*Unsupported.*)",
    "IBM Spectrum Protect" : "(?:^IBM\sSpectrum\sProtect\s.*)(?!.*Unsupported.*)",
    "Sybase ASA Client" : "(?:^Sybase\sASA\sClient\s.*)(?!.*Unsupported.*)",
    "WinSCP" : "(?:^WinSCP\s.*)(?!.*Unsupported.*)",
    "Citrix Workspace" : "(?:^Citrix\sWorkspace\s.*)(?!.*Unsupported.*)",
    "Intel PROSet/Wireless WiFi Software" : "(?:.*PROSet/Wireless\sWiFi\sSoftware\s.*)(?!.*Unsupported.*)",
    "SizerOne ActiveX Control" : "(?:^SizerOne\sActiveX\sControl.*)(?!.*Unsupported.*)",
    "Citrix XenApp XML Service Interface" : "(?:^Citrix\sXenApp\sXML\sService\sInterface.*)(?!.*Unsupported.*)",
    "SigPlus Pro ActiveX Control" : "(?:^SigPlus\sPro\sActiveX\sControl\s.*)(?!.*Unsupported.*)",
    "Dell Webcam CrazyTalk ActiveX" : "(?:^Dell\sWebcam\sCrazyTalk\sActiveX\s.*)(?!.*Unsupported.*)",
    "EMC NetWorker" : "(?:^EMC\sNetWorker\s.*)(?!.*Unsupported.*)",
    "PuTTY" : "(?:^PuTTY\s.*)(?!.*Unsupported.*)",
    "Apache JMeter" : "(?:^Apache\sJMeter\s.*)(?!.*Unsupported.*)",
    "Dell SupportAssist" : "(?:^Dell\sSupportAssist\s.*)(?!.*Unsupported.*)",
    "Google Earth" : "(?:^Google\sEarth\sPro\s.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "Docker for Windows" : "(?:^Docker\sfor\sWindows.*)(?!.*Unsupported.*)",
    "Microsoft Edge" : "(?:^Microsoft\sEdge\s\(Chromium\).*)(?!.*Unsupported.*)",
    "NVIDIA GeForce Experience" : "(?:^NVIDIA\sGeForce\sExperience.*)(?!.*Unsupported.*)",
    "McAfee Agent" : "(?:^McAfee\sAgent.*)(?!.*Unsupported.*)",
    "McAfee Endpoint Security" : "(?:^McAfee\sEndpoint\sSecurity.*)(?!.*Unsupported.*)",
    "Foxit PhantomPDF" : "(?:^Foxit\sPhantomPDF.*)(?!.*Unsupported.*)",
    "Pulse Secure Desktop Client" : "(?:^Pulse\sSecure\sDesktop\s.*)(?!.*Unsupported.*)",
    "Symantec Encryption Desktop" : "(?:^Symantec\sEncryption\sDesktop.*)(?!.*Unsupported.*)",
    "Morovia Barcode ActiveX" : "(?:^Morovia\sBarcode\s.*)(?!.*Unsupported.*)",
    "IBM Notes" : "(?:^IBM\sNotes.*)(?!.*Unsupported.*)",
    "Tenable Nessus Agent" : "(?:^Tenable\SNessus\SAgent\s.*)(?!.*Unsupported.*)",
    "Oracle Fusion Middleware" : "(?:^Oracle\sFusion\sMiddleware\s.*)(?!.*Unsupported.*)",
    "Apache Log4j" : "(?:^Apache\sLog4j\s.*)(?!.*Unsupported.*)",
    "Oracle Enterprise Manager Cloud Control" : "(?:^Oracle\sEnterprise\sManager\sCloud\sControl\s.*)(?!.*Unsupported.*)",
    "Spring Framework" : "(?:^Spring\sFramework\s.*)(?!.*Unsupported.*)",
    "OpenJDK" : "(?:^OpenJDK\s.*)(?!.*Unsupported.*)",
    "SizerOne ActiveX Control" : "(?:^SizerOne\sActiveX\sControl\s.*)(?!.*Unsupported.*)",
    "IBM Tivoli Monitoring" : "(?:^IBM\sTivoli\sMonitoring\s.*)(?!.*Unsupported.*)",
    "Cisco Packet Tracer" : "(?:^Cisco\sPacket\sTracer\s.*)(?!.*Unsupported.*)",
    "Azul Zulu" : "(?:^Azul\sZulu\s.*)(?!.*Unsupported.*)",
    "Oracle Mysql Connectors" : "(?:^Oracle\sMySQL\sConnectors\s.*)(?!.*Unsupported.*)",
    "Python" : "(?:^Python\s.*)(?!.*Unsupported.*)",
    "AMD Platform Security Processor" : "(?:^AMD\sPlatform\sSecurity\sProcessor\s.*)(?!.*Unsupported.*)",
    "Dell dbutil Driver" : "(?:^Dell\sdbutil\sDriver\s.*)(?!.*Unsupported.*)"
}

server_software = {
    "Firebird SQL Server" : "^Firebird\sSQL\sServer.*",
    "Oracle Database" : "^Oracle.*Database.*Server.*",
    "Oracle WebLogic" : "^Oracle\sWebLogic\s.*",
    "Oracle RDBMS" : "^Oracle\sRDBMS\s.*",
    "Oracle TNS Listener" : "^Oracle\sTNS\sListener\s.*",
    "Oracle Fusion" : "^Oracle\sFusion\s.*",
    "Apache" : "^(?:Apache\s.*)(?!.*\sStruts\s*)(?!.*\sTomcat\s*)(?!.*\sMultiviews\s*)",
    #"Apache" : "^(?:Apache\s.*Vulnerabilities.*)(?:Apache\s.*Vulnerability)(?:Apache\s.*Disclosure)(?!.*\sStruts\s*)(?!.*\sTomcat\s*)",
    "Apache Tomcat" : "(?:^Apache\sTomcat\s.*)(?!.*\sDefault\sFiles*)",
    "Apache Struts" : "(?:^Apache\sStruts\s.*)(?!.*\sDefault\sFiles*)",
    "Apache Multiviews" : "(?:^Apache\sMultiviews\s.*)(?!.*\sDefault\sFiles*)",
    "PHP" : "(?:^PHP.*)(?!.*Unsuported.*)(?!.*Detection.*)",
    "Dropbear SSH Server" : ".*Dropbear.*SSH.*Vulnerabilities.*",
    "OpenSSH Server" : ".*OpenSSH.*Vulnerabilities.*",
    "MongoDB" : ".*MongoDB.*Vulnerabilities",
    "Jenkins" : "^Jenkins.*Vulnerabilities.*",
    "Microsoft ASP.NET" : "^Microsoft\sASP\.NET*.*",
    "Microsoft ASP.NET Core" : ".*Microsoft\sASP\.NET\sCore.*",
    "JBoss Enterprise" : "^JBoss\sEnterprise\sApplication.*",
    "Microsoft Dynamics" : "^Microsoft\sDynamics\s365.*",
    "Microsoft SQL Server" : "(?:.*Microsoft\sSQL\sServer.*)(?!.*Unsupported.*)",
    "Microsoft DNS Server" : "(?:.*Microsoft\sDNS\sServer.*)(?!.*Unsupported.*)",
    "Microsoft IIS" : "(?:^Microsoft\sIIS\s.*Server.*)(?!.*Unsupported.*)",
    #"Exchange Server" : "(?:.*Exchange.*)(?!.*Unsupported.*)",
    "SonicWALL" : "(?:^SonicWALL.*)(?!.*Detection)",
    "OpenSSL" : "(?:^OpenSSL.*)(?!.*Detection.*)",
    "Dell iDrac" : "(?:^Dell\si[Dd][Rr][Aa][Cc].*)",
    "Dell OpenManage Server Administrator" : "^Dell\sOpenManage\sServer\sAdministrator\s*",
    "SolarWinds" : "^SolarWinds.*"        ,
    "HP iLO" : "HP\siLO.*",
    "WMware ESXi" : ".*ESXi\s.*",
    "WMware vCenter" : "^VMware\svCenter\s.*",
    "HPE Smart Storage Administrator" : "^HPE\sSmart\sStorage\sAdministrator.*",
    "HP System Management Homepage" : "^HP\sSystem\sManagement\sHomepage\s.*",
    "IBM Tivoli Management Framework" : "^IBM\sTivoli\sManagement\sFramework\s.*",
    "IBM DB2" : "^IBM\sDB2\s.*",
    "Jetty HTTP Server" : "^Jetty\s.*",
    "Tenable Nessus" : "^Tenable\sNessus\s.*",
    "Kibana" : "^Kibana\s.*",
    "Flexera FlexNet" : "^Flexera\sFlexNet\s.*",
    "Elasticsearch" : "^Elasticsearch\s.*",
    "Node.js" : "^Node.js\s.*Vulnerabilities.*",
    "MySQL" : "^MySQL\s.*Vulnerabilities.*",
    "ManageEngine Desktop Central" : "^ManageEngine\sDesktop\sCentral.*",
    "Nginx" : "^nginx\s.*",
    "Oracle MySQL Workbench" : "^Oracle\sMySQL\sWorkbench\s.*",
    "Oracle Coherence" : "^Oracle\sCoherence\s.*",
    "Oracle HTTP Server" : "^Oracle\sHTTP\sServer\s.*",
    "Dell EMC NetWorker" : "^Dell\sEMC\sNetWorker\s.*",
    "PostgreSQL" : "(?:^PostgreSQL\s.*Vulnerabilities.*)(?!.*Unsupported.*)",
    "Flask" : "^Flask\s.*",
    "QNAP QTS / QuTS Hero" : "^QNAP\sQTS\s.*",
    "Samba" : "^Samba\s.*[Vv]ulnerabilities.*",
    "Splunk" : "(?:^Splunk\s.*)(?!.*Unsupported.*)(?!.*Detection.*)",
    "Network Time Protocol" : "(?:^Network\sTime\sProtocol\s.*)(?:^NTP\s.*)(?!.*Scanner.*)",
    "Telnetd" : "(?:^Telnetd\s-\sRemote\sCode\sExecution\s.*)",
    "Sap Businessobjects Business Intelligence Platform" : "(?:^Sap\sBusinessobjects\sBusiness\sIntelligence.*)"
}

defender = {
    "Microsoft Windows Defender" : ".*Microsoft\sDefender.*|.*Windows\sDefender.*",
    "Microsoft Windows Malicious Software Removal Tool " : ".*Windows\sMalicious\sSoftware\sRemoval\sTool.*",
    "Microsoft Malware Protection Engine" : ".*Microsoft\sMalware\sProtection\sEngine.*"
}

ssl_tls = {
    "SSL/TLS Service is insecurely configured" : "(?=^SSL.*)(?!.*Certificate.*)(?!.*Certification.*)|(?=^TLS\s*)|(?=^Transport\sLayer\sSecurity.*)",
    "SSL Certificates" : "(?=^SSL.*Certificate.*)|(?=^SSL.*Certification.*)"
}

terminal_services = {
    "Terminal Services" : "(?=Microsoft\sWindows\sRemote\sDesktop\sProtocol\sServer\sMan-in-the-Middle\sWeakness)|(?=^Terminal\sServices\s.*)"
}

ssh_servers = {
    "SSH" : "(?=^SSH.*)(?!SSH\sAlgorithms\sand\sLanguages\sSupported)(?!.*Version\sInformation)(?!SSH\sProtocol\sVersions\sSupported)"
}

unsupported_software = {
    "Unsupported Software" : "(?=.*[Uu]nsupported.*)"#(?!.*OS.*)(?!.*XP.*)"
}

information_disclosure = {
    "Microsoft Windows IIS Default Index Page" : "Microsoft\sWindows\sIIS\sDefault\sIndex\sPage",
    "Web Server HTTP Header Information Disclosure" : "Web\sServer\sHTTP\sHeader\sInformation\sDisclosure"
}

clear_text_protocols = {
    "Telnet Server" : "Unencrypted\sTelnet\sServer",
    "rexecd Service" : "rexecd\sService\sDetection",
    "rlogin Service" : "rlogin\sService\sDetection"
}

### OS Patches
windows = [
    "Windows : Microsoft Bulletins"
]
redhat = [
    "Red Hat Local Security Checks"
]
solaris = [
    "Solaris Local Security Checks"
]
oracle = [
    "Oracle Linux Local Security Checks"
]
ubuntu = [
    "Ubuntu Local Security Checks"
]
fedora = [
    "Fedora Local Security Checks"
]

def name_aggregator(findings, names, filename):
    results = {}
    for host in findings:
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            #print(p.attrib)
            #if i.attrib["name"] == "host-ip'":
            #    print(i.text)
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        #hostip = host.find("HostProperties/tag[@name='host-ip']").text
        #hostfqdn = host.find("HostProperties/tag[@name='host-fqdn']").text
        #netbiosname = host.find("HostProperties/tag[@name='netbios-name']").text
        for item in host.iter("ReportItem"):
            try:
                risk_factor = item.find("risk_factor").text
            except AttributeError:
                pass
            else:
                if risk_factor == "None":
                    pass
                else:
                    plugin_name = item.attrib["pluginName"]
                    for name, regex in names.items():
                        if re.search(regex, plugin_name):
                            if name in results:
                                results[name]["affected"] += [hostname]
                                if item.find("cve") != None:
                                    for element in item.findall("cve"):
                                        results[name]["cves"] += [element.text]
                            else:
                                results[name] = { "affected" : [], "cves" : [] }
                                results[name]["affected"] += [hostname]
                                if item.findall("cve") != None:
                                    for element in item.findall("cve"):
                                        results[name]["cves"] += [element.text]
        
    # implement results check to not create empty files when no matches found
    if results:
        with open(filename, 'w') as f:
            f.write("Name|CVE|Affected\n")
            for name, results in results.items():
                cves = ", ".join(set(results["cves"]))
                affected = ", ".join(set(results["affected"]))
                line = "{}|{}|{}".format(name, cves, affected)
                f.write(line + "\n")
        
        #print(filename)
        #print(", ".join(set(results["affected"])))



def name_collector(findings, names, filename):
    results = {}
    for host in findings:
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            #if i.attrib["name"] == "host-ip'":
            #    print(i.text)
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        
        for item in host.iter("ReportItem"):
            try:
                risk_factor = item.find("risk_factor").text
            except AttributeError:
                pass
            else:
                if risk_factor == "None":
                    pass
                else:
                    plugin_name = item.attrib["pluginName"]
                    
                    if item.find("cve") != None:
                        cve = [e.text for e in item.findall("cve")]
                    else:
                        cve = []

                    if item.find("cvss3_base_score") != None:
                        try:
                            cvss_base_score = item.find("cvss3_base_score").text
                            cvss_vector = item.find("cvss3_vector").text
                        except AttributeError:                     
                            cvss_base_score = ""
                            cvss_vector = ""
                    elif item.find("cvss_base_score") != None:
                        try:
                            cvss_base_score = item.find("cvss_base_score").text
                            cvss_vector = item.find("cvss_vector").text
                        except AttributeError:
                            cvss_base_score = ""
                            cvss_vector = ""
                    else:
                        cvss_base_score = ""
                        cvss_vector = ""


                    for name, regex in names.items():
                        if re.search(regex, plugin_name):

                            if plugin_name in results:
                                results[plugin_name]["cves"] = cve
                                results[plugin_name]["cvss_base_score"] = cvss_base_score
                                results[plugin_name]["cvss_vector"] = cvss_vector
                                results[plugin_name]["affected"] += [hostname]
                            else:
                                results[plugin_name] = { "affected" : [], "cves" : [], "cvss_base_score" : "", "cvss_vector" : "" }
                                results[plugin_name]["cves"] = cve
                                results[plugin_name]["cvss_base_score"] = cvss_base_score
                                results[plugin_name]["cvss_vector"] = cvss_vector
                                results[plugin_name]["affected"] += [hostname]

    
    if results:
        with open(filename, 'w') as f:
            f.write("Name|CVE|CVSS Score|CVSS Vector|Affected\n")
            for name, result in results.items():
                cves = ", ".join(set(result["cves"]))
                affected = ", ".join(set(result["affected"]))
                line = "{}|{}|{}|{}|{}".format(name, cves, result["cvss_base_score"], result["cvss_vector"], affected)
                f.write(line + "\n")    


def family_collector(findings, families, filename):
    results = {}
    reg_keys = {}

    for host in findings:
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            #if i.attrib["name"] == "host-ip'":
            #    print(i.text)
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        #ip = host.find("HostProperties/tag[@name='host-ip']").text
        for item in host.iter("ReportItem"):
            try:
                risk_factor = item.find("risk_factor").text
            except AttributeError:
                pass
            else:
                if risk_factor == "None":
                    pass
                else:
                    plugin_name = item.attrib["pluginName"]
                    plugin_family = item.attrib["pluginFamily"]
                    plugin_id = item.attrib["pluginID"]
                    
                    if item.find("cve") != None:
                        cve = [e.text for e in item.findall("cve")]
                    else:
                        cve = []

                    if item.find("cvss3_base_score") != None:
                        try:
                            cvss_base_score = item.find("cvss3_base_score").text
                            cvss_vector = item.find("cvss3_vector").text
                        except AttributeError:
                            cvss_base_score = ""
                            cvss_vector = ""
                    elif item.find("cvss_base_score") != None:
                        try:
                            cvss_base_score = item.find("cvss_base_score").text
                            cvss_vector = item.find("cvss_vector").text
                        except AttributeError:
                            cvss_base_score = ""
                            cvss_vector = ""
                    else:
                        cvss_base_score = ""
                        cvss_vector = ""

                    if item.find("xref") != None:
                        xref = [item.find("xref").text]
                    else:
                        xref = []

                    if item.find("risk_factor") != None:
                        risk_factor = item.find("risk_factor").text
                    else:
                        risk_factor = ""


                    for family in families:
                        if plugin_family == family:

                            if item.find("plugin_output") != None:
                                plugin_output = item.find("plugin_output").text
                                if re.search("[Rr]egistry", plugin_output):
                                    reg_keys[plugin_name] = plugin_output
                            
                            if plugin_name in results:
                                results[plugin_name]["cves"] = cve
                                results[plugin_name]["cvss_base_score"] = cvss_base_score
                                results[plugin_name]["cvss_vector"] = cvss_vector
                                results[plugin_name]["risk_factor"] = risk_factor
                                results[plugin_name]["reference"] = xref                  
                                results[plugin_name]["affected"] += [hostname]
                            else:
                                results[plugin_name] = { "affected" : [], "cves" : [], "cvss_base_score" : "", "cvss_vector" : "", "reference" : [] }
                                results[plugin_name]["cves"] = cve
                                results[plugin_name]["cvss_base_score"] = cvss_base_score
                                results[plugin_name]["cvss_vector"] = cvss_vector
                                results[plugin_name]["risk_factor"] = risk_factor
                                results[plugin_name]["reference"] = xref
                                results[plugin_name]["affected"] += [hostname]
                    
    #print reg keys
    for name, key in reg_keys.items():
        print(name)
        print(key)
        print("---")
    
    
    if results:
        with open(filename, 'w') as f:
            f.write("Risk|Name|CVE|CVSS Score|CVSS Vector|Ref|Affected\n")
            for name, result in results.items():
                cves = ", ".join(set(result["cves"]))
                affected = ", ".join(set(result["affected"]))
                ref = ", ".join(set(result["reference"]))
                line = "{}|{}|{}|{}|{}|{}|{}".format(result["risk_factor"], name, cves, result["cvss_base_score"], result["cvss_vector"], ref, affected)
                f.write(line + "\n")

def compliance_collector(findings, filename):
    results = {}
    for host in findings:
        hostname = host.attrib["name"]
        for p in host.find("HostProperties"):
            #if i.attrib["name"] == "host-ip'":
            #    print(i.text)
            if p.attrib["name"] == "netbios-name":
                hostname = p.text
            if p.attrib["name"] == "host-fqdn":
                hostname = p.text.split(".")[0]
            if p.attrib["name"] == "hostname":
                hostname = p.text
        #ip = host.find("HostProperties/tag[@name='host-ip']").text
        for item in host.iter("ReportItem"):

            if item.find("compliance") != None:
                if item.find("compliance").text == "true":
                
                    if item.find("{http://www.nessus.org/cm}compliance-check-id") != None:
                        compliance_check_id = item.find("{http://www.nessus.org/cm}compliance-check-id").text
                    
                    if item.find("{http://www.nessus.org/cm}compliance-check-name") != None:
                        compliance_check_name = item.find("{http://www.nessus.org/cm}compliance-check-name").text
                    else:
                        compliance_check_name = ""
                    
                    if item.find("{http://www.nessus.org/cm}compliance-actual-value") != None:
                        compliance_actual_value = item.find("{http://www.nessus.org/cm}compliance-actual-value").text
                    else:
                        compliance_actual_value = ""
                    
                    if item.find("{http://www.nessus.org/cm}compliance-policy-value") != None:
                        compliance_policy_value = item.find("{http://www.nessus.org/cm}compliance-policy-value").text
                    else:
                        compliance_policy_value = ""
                    
                    if item.find("{http://www.nessus.org/cm}compliance-result") != None:
                        compliance_result = item.find("{http://www.nessus.org/cm}compliance-result").text
                    else:
                        compliance_result = ""
                    
                    if item.find("{http://www.nessus.org/cm}compliance-info") != None:
                        compliance_info = item.find("{http://www.nessus.org/cm}compliance-info").text
                    else:
                        compliance_info = ""
                    
                    if item.find("{http://www.nessus.org/cm}compliance-audit-file") != None:
                        compliance_audit_file = item.find("{http://www.nessus.org/cm}compliance-audit-file").text
                    else:
                        compliance_audit_file = ""
                    
                    results[compliance_check_id] = {}
                    results[compliance_check_id]["compliance_check_name"] = compliance_check_name
                    results[compliance_check_id]["compliance_actual_value"] = compliance_actual_value
                    results[compliance_check_id]["compliance_policy_value"] = compliance_policy_value
                    results[compliance_check_id]["compliance_result"] = compliance_result
                    results[compliance_check_id]["compliance_info"] = compliance_info
                    results[compliance_check_id]["compliance_audit_file"] = compliance_audit_file

   
    if results:
        with open(filename, 'w') as f:
            #f.write("Name|Expected Value|Actual Value|Result|Info|Audit File\n")
            f.write("Name|Expected Value|Actual Value|Result|Audit File\n")
            for compliance_id, result in results.items():
                line = "{}|{}|{}|{}|{}".format(result["compliance_check_name"], result["compliance_policy_value"], result["compliance_actual_value"], result["compliance_result"], result["compliance_audit_file"])
                f.write(line + "\n")

#def check_names(findings, names):
#    plugin_names = []
#    for host in findings:
#        for item in host.iter("ReportItem"):
#            if item.find("risk_factor").text == "None":
#                # ignore infos
#                pass
#            else:
#                plugin_names += [item.attrib["pluginName"]]
#
#    plugin_names_uniq = set(plugin_names)
#    
#    for plugin_name in plugin_names_uniq:
#        match = False
#        for name, regex in names.items():
#            if re.search(regex, plugin_name):
#                match = True
#        if match == False:
#            print(plugin_name)

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

    name_aggregator(get_findings(args.i), client_software, os.path.join(args.o, "common_client_software_aggregated.table"))
    name_aggregator(get_findings(args.i), server_software, os.path.join(args.o, "server_software_aggregated.table"))
    name_aggregator(get_findings(args.i), terminal_services, os.path.join(args.o, "terminal_services_aggregated.table"))
    name_aggregator(get_findings(args.i), ssl_tls, os.path.join(args.o, "ssl_tls_aggregated.table"))
    name_aggregator(get_findings(args.i), ssh_servers, os.path.join(args.o, "ssh_servers_aggregated.table"))
    name_aggregator(get_findings(args.i), information_disclosure, os.path.join(args.o, "information_disclosure_aggregated.table"))
    name_aggregator(get_findings(args.i), defender, os.path.join(args.o, "defender_aggregated.table"))
    name_aggregator(get_findings(args.i), clear_text_protocols, os.path.join(args.o, "clear_text_protocols_aggregated.table"))
    
    name_collector(get_findings(args.i), terminal_services, os.path.join(args.o, "terminal_services_collected.table"))
    name_collector(get_findings(args.i), ssl_tls, os.path.join(args.o, "ssl_tls_collected.table"))
    name_collector(get_findings(args.i), ssh_servers, os.path.join(args.o, "ssh_servers_collected.table"))
    name_collector(get_findings(args.i), information_disclosure, os.path.join(args.o, "information_disclosure_collected.table"))
    name_collector(get_findings(args.i), defender, os.path.join(args.o, "defender_collected.table"))
    name_collector(get_findings(args.i), clear_text_protocols, os.path.join(args.o, "clear_text_protocols_collected.table"))
    name_collector(get_findings(args.i), unsupported_software, os.path.join(args.o, "unsupported_software_collected.table"))
    
    family_collector(get_findings(args.i), windows, os.path.join(args.o, "windows_patches_collected.table"))
    family_collector(get_findings(args.i), redhat, os.path.join(args.o, "redhat_patches_collected.table"))
    family_collector(get_findings(args.i), solaris, os.path.join(args.o, "solaris_patches_collected.table"))
    family_collector(get_findings(args.i), oracle, os.path.join(args.o, "oracle_patches_collected.table"))
    family_collector(get_findings(args.i), ubuntu, os.path.join(args.o, "ubuntu_patches_collected.table"))
    family_collector(get_findings(args.i), fedora, os.path.join(args.o, "fedora_patches_collected.table"))  
    
    compliance_collector(get_findings(args.i), os.path.join(args.o, "compliance.table"))  
    
    #check_names(get_findings(args.i), client_software)

if __name__ == '__main__':
    main()
