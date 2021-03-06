#!/usr/bin/env python

# Import

import os
import configparser
import time
import requests
import subprocess
import sys
from os import listdir
from pathlib import Path

# Variables

# Mac Paths

debugSet        = True
debugLog        = []
home            = str(Path.home())
fileDir         = os.path.dirname(os.path.realpath('__file__'))
outfileMac      = os.path.join(fileDir, 'out/out.txt')
outfile         = os.path.join(fileDir, 'out/out.txt')
debugfileMac    = os.path.join(fileDir, 'debug/debug.txt')
debugfile       = os.path.join(fileDir, 'debug/debug.txt')
scansrc         = os.path.join(fileDir, 'scansrc/')
mypath          = ''
mypathMac       = home + "/Projects/gh-oB-recon/in/"

# Checking for if the OS is Windows or Linux

osCheck         = ''
isWin           = 0

# Windows Paths

debugfileWin    = os.path.join(fileDir, 'debug\\debug.txt')
# mypathWin       = home + "\\Projects\\gh-oB-recon\\in\\"
mypathWin       = home + "\\Projects\\oB-Recon\\in\\"
outfileWin      = os.path.join(fileDir, 'out\\out.txt')

targets         = []
fileCount       = int(0)
conf            = {}
lineBreaks      = str('\n')
scanresults     = []
totalTargetsAndScans = int(0)
percentageComplete = int(0)

# Functions

"""
Inbound function is meant to take in files of types txt, log, or csv. Handling for each file
is differentiated.

CSV files should only contain the data elements meant to be gathered. There should be no headers
or labels.

IP addresses and hostnames are accepted in the inbound files.
"""

def boot():
    global osCheck
    global isWin

    """
    Commented out because this would not work on Macs and it is just for making it look nice
    on the command line.

    try:
        os.system('cls')
    except SyntaxError:
        pass

    """
    print('Initializing program: oB-Recon.')
    print('Debug activated is: ' + str(debugSet) + '.')
    print('')

    osCheck = os.name
    if osCheck == 'nt':
        isWin = 1
    if isWin == 1:
        debugLog.append('Program running on Windows.')
    pass


def readConf():
    global conf
    conf = configparser.ConfigParser()
    conf.read('conf.ini')
    if debugSet == True:
        debugLog.append('Configuration sections loaded:')
        debugLog.append(conf.sections())
    return

def inbound():
    global fileCount, mypath
    iF = []   # iF is inbound files
    try:
        for f in listdir(mypathWin):
            if f.find(".txt", len(f) - 4) != -1:
                iF.append(f)
            elif f.find(".log", len(f) - 4) != -1:
                iF.append(f)
            elif f.find(".csv", len(f) - 4) != -1:
                iF.append(f)
            else:
                #print(f + ' outside of txt, log, or csv types.')
                fileCount = fileCount - 1
            fileCount = fileCount + 1
            print (range(fileCount))
        mypath = mypathWin
    except FileNotFoundError:
        for f in listdir(mypathMac):
            if f.find(".txt", len(f) - 4) != -1:
                iF.append(f)
            elif f.find(".log", len(f) - 4) != -1:
                iF.append(f)
            elif f.find(".csv", len(f) - 4) != -1:
                iF.append(f)
            else:
                #print(f + ' outside of txt, log, or csv types.')
                fileCount = fileCount - 1
            fileCount = fileCount + 1
        mypath = mypathMac
    if debugSet == True:
        debugLog.append('iF (inbound files) contains:')
        for x in iF:
            debugLog.append(x + ' added to iF')
        debugLog.append('fileCount is: ' + str(fileCount))
    return iF

def parse(x):
    file = open('in/' + x, 'r')
    for line in file:
        line = line.strip() # Removes blank lines.
        if line:
            ''' This portion of the script is meant to discover if the inbound files are correctly formatted.
            Decision tree:
                If IP -> Add IP to target list (in other languages, this is an array)
                If CIDR -> Convert to IPs
                    -> Add all IPs to targets list
                If IP Range -> Convert to IPs
                    -> Add all IPs to targets list
                
            
            if line == IP address format:
                targets.append(line)
                if debugSet == True:
                debugLog.append('Appending ' + line + ' to targets.')
            '''
            targets.append(line)
            if debugSet == True:
                debugLog.append('Appending ' + line + ' to targets.')
    pass

def outbound():
    print('\n================\n==Begin output==\n================\n')
    n = 0
    global outfile
    if os.path.isfile(outfile):
        print(outfile + ' exists; appending timestamp to written file.')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        outfilefull = str(outfile)
        outfiletype = outfilefull[-4:]
        outfilename = outfilefull[:(len(outfilefull) - 4)]
        outfilefull = outfilename + '-' + timestr + outfiletype
        print(outfilefull)
        outfile = os.path.join(fileDir, outfilefull)

    try:
        f = open(outfile, 'a')
        print('')
        print('\tSetting output file,', outfile)
        print('')
    except:
        print("\tFailed to open output file!")
        f.close()
    for j in scanresults:
        f.write(j)
        f.write(lineBreaks)  # This is to add a new line at the end of each line of the log or text file.
        n = n + 1
        if n % 100 == 0:
            print('\tWriting outputs: ' + str(n) + ' scan results complete.')
        else:
            pass
    else:
        pass
    print('\tOutput complete: ' + str(n) + ' scan results written.')
    print('\n')
    return

def scan(t): # Runs each scan on target 't'.
    """
    Possible candidate for combination with scanselect

    Right now this function is basically just a for loop for all scans to call and send values to
    scanselect(s,t) which does the actual selection and execution of the scans.

    Current function is for each configurable scan in the config:

    - check if a scan is set to run, if yes, add debug line if debug is on.
    - check if scan is set to run, run the scan on target t.
    """
    for s in conf['scans']:
        if conf['scans'][s] == 'True':
            if debugSet == True:
                debugLog.append('Running ' + s + ' against ' + t + ' in scan(t)')
            pass
        if conf['scans'][s]== 'True':
            scanselect(s,t)
    return

def scanselect(s,t):
    """
    Receives values s and t, where:

    - s is the scan number, based on the configuration .ini file
    - t is the target on which to run the scan

    To add a new scan:

    - add an additional function scanx where x is an integer.
    - add an additional line to the switcher, 'scanx': int(x) and insert a comma if there
    is a follow on scan.
    """
    switcher = {
        'scan1': int(1),
        'scan2': int(2),
        'scan3': int(3),
        'scan4': int(4),
        'scan5': int(5),
        'scan6': int(6),
        'scan7': int(7),
        'scan8': int(8),
        'scan9': int(9),
        'scan10': int(10)  # Add more scans here
    }
    y=(switcher[s])
    if y == 1:
        print('Launching scan1 on ' + t)
        scan1(t)
    elif y == 2:
        print('Launching scan2 on ' + t)
        scan2(t)
    elif y == 3:
        print('Launching scan3 on ' + t)
        scan3(t)
    elif y == 4:
        print('Launching scan4 on ' + t)
        scan4(t)
    elif y == 5:
        print('Launching scan5 on ' + t)
        scan5(t)
    elif y == 6:
        print('Launching scan6 on ' + t)
        scan6(t)
    elif y == 7:
        print('Launching scan7 on ' + t)
        scan7(t)
    elif y == 8:
        print('Launching scan8 on ' + t)
        scan8(t)
    elif y == 9:
        print('Launching scan9 on ' + t)
        scan9(t)
    elif y == 10:
        print('Launching scan10 on ' + t)
        scan10(t)
    else:
        print ('Invalid scan selected.')
    return


def scan1(x):
    '''
    Scan 1 target is set up to do a "quick scan" from nmap on target x. In order to do a more intense scan,
    the options would be nmap -T4 -A -v <ipaddress>. More to be added.
    '''
    y = 'Begin scan1 on ' + x
    scan1target = ['nmap', '-T4', '-F', x]
    result = subprocess.run(scan1target, stdout=subprocess.PIPE)
    scanresults.append(result.stdout.decode('utf-8'))
    return y

def scan2(x):
    #print(x)
    y = 'Begin scan2 on ' + x
    scan2target = ['nmap', '--script', 'ssl-enum-ciphers', '-p 443', x]
    result = subprocess.run(scan2target, stdout=subprocess.PIPE)
    scanresults.append(result.stdout.decode('utf-8'))
    return y

def scan3(x):  # This is doing an ARIN lookup.
    url1 = 'http://whois.arin.net/rest/ip/'
    url2 = '.txt'
    y = url1 + x + url2
    payload = {'key': 'val'}
    headers = {}
    res = requests.get(y, data=payload, headers=headers)
    txt = res.text
    scanresults.append(txt)
    return y

def scan4(x): #ping
    y = 'Begin scan4 on ' + x
    scan4target = ['ping', '-c 1', '-W 500', x]
    try:
        result = subprocess.run(scan4target, stdout=subprocess.PIPE)
        scanresults.append(result.stdout.decode('utf-8'))
    except KeyError:
        print('did not work')
    return y

def scan5(x):
    y = 'Begin scan5 on ' + x
    scan5target = ['nmap', '-v', '-p 137,138,139', x]
    try:
        result = subprocess.run(scan5target, stdout=subprocess.PIPE)
        scanresults.append(result.stdout.decode('utf-8'))
    except KeyError:
        print('did not work')
    return y

def scan6(x):
    y = 'Begin scan6 on ' + x
    arg = "'llmnr-resolve.hostname=" + x + "'"
    scan6target = ['nmap', '--script', 'llmnr-resolve', '--script-args', arg]
    print (scan6target)
    try:
        result = subprocess.run(scan6target, stdout=subprocess.PIPE)
        scanresults.append(result.stdout.decode('utf-8'))
    except KeyError:
        print('did not work')
    return y

def scan7(x):
    #print(x)
    y = 'Begin scan7 on ' + x
    scanresults.append('These are the results of the scan.')
    return y

def scan8(x):
    #print(x)
    y = 'Begin scan8 on ' + x
    scanresults.append('These are the results of the scan.')
    return y

def scan9(x):
    #print(x)
    y = 'Begin scan9 on ' + x
    scanresults.append('These are the results of the scan.')
    return y

def scan10(x):
    #print(x)
    y = 'Begin scan10 on ' + x
    scanresults.append('These are the results of the scan.')
    return y

def debug():
    if debugSet == True:
        debugLog.append('\n\n=============================\n=======DEBUG==OUTPUT=========\n=============================')
        debugLog.append('debugSet\t = ' + str(debugSet))
        debugLog.append('home\t\t = ' + str(home))
        debugLog.append('fileDir\t\t = ' + str(fileDir))
        debugLog.append('outfile\t\t = ' + str(outfile))
        debugLog.append('mypath\t\t = ' + str(mypath))
        debugLog.append('targets\t\t = ')
    return

def debug2():
    global debugfile
    if debugSet == True:
        print('\n================')
        print('==Debug output==')
        print('================')
        n = 0
        if os.path.isfile(debugfile):
            print(debugfile + ' exists; appending timestamp to written file.')
            timestr = time.strftime("%Y%m%d-%H%M%S")
            debugfilefull = str(debugfile)
            debugfiletype = debugfilefull[-4:]
            debugfilename = debugfilefull[:(len(debugfilefull) - 4)]
            debugfilefull = debugfilename + '-' + timestr + debugfiletype
            print(debugfilefull + ' created.')
            debugfile = os.path.join(fileDir, debugfilefull)

        try:
            f = open(debugfile, 'a')
            print('')
            print('\tSetting debug file,', debugfile)
            print('')
        except:
            print("\tFailed to open debug file!")
            f.close()
        for j in debugLog:
            f.write(str(j))
            f.write(lineBreaks)  # This is to add a new line at the end of each line of the log or text file.
            n = n + 1
            if n % 100 == 0:
                print('\tWriting outputs: ' + str(n) + ' lines complete.')
            else:
                pass
        else:
            pass
        print('\tOutput complete: ' + str(n) + ' lines written.')
        print('\n')
        return

def arin(x):
    url1		=	'http://whois.arin.net/rest/ip/'
    url2		=	'.txt'
    y 		 	=	url1+x+url2
    payload 	=	{'key':'val'}
    headers		=	{}
    res 		= 	requests.get(y, data=payload, headers=headers)
    txt 		=   res.text
    return txt

def completionTrackerInit():
    global totalTargetsAndScans
    totalTargets = int(0)
    totalScans = int(0)
    for t in targets:
        totalTargets = totalTargets + 1
    for s in conf['scans']:
        if conf['scans'][s] == 'True':
            totalScans = totalScans + 1
    totalTargetsAndScans = totalTargets * totalScans
    return

def main():
    global percentageComplete
    scansComplete = int(0)
    boot()
    readConf()
    i = inbound()
    for file in range(fileCount):
        parse(i[file])
    completionTrackerInit()
    for t in targets:
        scan(t)
        scansComplete = scansComplete + 1
        try:
            percentageComplete = round(scansComplete/totalTargetsAndScans, 2)
        except ZeroDivisionError:
            print ('No targets or scans configured to run. Cannot divide by zero.')
        print(str(percentageComplete*100) + '% percent complete. Finished scan ' + str(scansComplete) + ' of ' + str(totalTargetsAndScans))
    pass

# Run

debug()
main()
outbound()
debug2()

