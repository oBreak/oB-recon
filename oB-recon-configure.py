#!/usr/bin/env python

"""


Writes a configuration file for the oB-recon program. This controls which
tests are run.

Scan1   = Scan 1 target is set up to do a "quick scan" from nmap on target x.
          The command line is 'nmap -T4 -F target'

          In order to do a more intense scan, the options would be nmap -T4 -A -v <ipaddress>,
          this is not a configurable toggle within the oB-recon program.

Scan2   = Scan 2 enumerates the available ciphers via nmap --script ssl-enum-ciphers -p 443 <target>

Scan3   = ARIN.net lookup for the IP in question.

Scan4   = Quick ping sweep.

Scan5   = File share enumeration for NFS shares.

Scan6   = Scan for responder possible targets, LLMNR and NetBIOS port scan.

Scan7   = Capture available web elements. ## Not built yet. Need to understand this better. How do I capture graphics?
          How do I determine which fields have inputs?

Scan8   = Example.
Scan9   = Example.
Scan10  = Example.

"""

# Import
import configparser

# Variables


# Functions
def writeConf():
    conf = configparser.ConfigParser()
    #conf['credentials-example']         = {'user1': 'example', 'pass1': 'password', 'user2': 'admin', 'pass2': 'root'}
    #conf['connectionstring-example']    = {'servername': 'server', 'port': '23'}
    conf['scans']                       = {'scan1': 'False',\
                                           'scan2': 'False',\
                                           'scan3': 'False',\
                                           'scan4': 'False',\
                                           'scan5': 'False',\
                                           'scan6': 'False',\
                                           'scan7': 'False',\
                                           'scan8': 'False',\
                                           'scan9': 'False',\
                                           'scan10': 'False'}
    with open ('conf.ini', 'w') as configfile:
        conf.write(configfile)
    return
# Main
writeConf()