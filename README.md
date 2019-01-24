# oB-recon

For recon against networked assets.

### Author

oBreak ([email](mailto:obreakemail@gmail.com))

### Version 

0.6

### Compatibility

Not entirely compatible for Windows yet. Working on this. Scan 3 works for 
Windows, but the program will error on other scans.

### Pre-requisites (Important or this will not work!)

- Python 3.6+ installed
- Network connectivity, assuming target is outside of local machine
- Install `configparser` and `requests` modules.
- nmap installed and callable (https://nmap.org/download.html)
- sudo privileges (if running certain scans)

### Usage

Place target ip addresses in .txt or .log files in the `/in/`
directory. One IP per line.

When `scan1` or `scan2` is `true`, Python must be run as sudo since it is using nmap.

- Scan 1 - Port scan (nmap "quick" scan)
- Scan 2 - SSL checking scan (powered by nmap)
- Scan 3 - ARIN lookup 
- Scan 4 - Quick ping sweep. Tries 1 ping per target with .5s delay. If no response, it
skips to the next target. This scan works on Mac, I don't believe it works on Windows.
Would need to edit the argument flags.
- Scan 5 - Scan for NetBIOS port (139) to determine possible responder targets.
- Scan 6 - || **DOES NOT WORK YET** || Scan for LLMNR resolutions to determine 
possible responder targets.
- Scan 7 - || **DOES NOT WORK YET** || Capture available web elements.

Scan results are found in the `/out/` directory

### Compatibility

Need to verify if this is both Windows and Mac compatible. It should be.