# oB-recon

For recon against networked assets.

### Author

oBreakEmail@gmail.com

### Usage

Place target ip addresses in .txt or .log files in the /in/ 
directory. One IP per line.

When 'scan 1' is true, Python must be run as sudo since it is using nmap.

Scan 1 - nmap "quick" scan \
Scan 2 - undefined \
Scan 3 - ARIN lookup 

### Pre-requisites

- Internet connectivity
- nmap installed and callable
- sudo privileges

### Development Roadmap

- Combine `scan(t)` and `scanselect(s,t)`, they serve the same function.
- Enable imported targets to be either IP address, CIDR notation, or hostname.
- Code scans, recon tools, and exploit validation (not execution)
- Integration with nmap, openssl
- Output results to file, allow configurable output formats
- Search against composite block list
- Take screenshot of web landing page
- Make a web GUI (potentially)

### Not on Dev Roadmap (musing)

- Integrations

### Completed Roadmap Items

- [Complete] Import targets from file or argument.
- [Complete] Import scans to run from configurable ini file.
- [Complete] Write programmatic way to create the ini that is customizable.
- [Complete] Finished `scanselect(s,t)` function that will run the appropriate
named scans on the target when set to true in the config file.
- [Complete] Move printed output of debug to debugLog table.
- [Complete] Output debugLog to log file to be created with timestamps. Add these
to the .gitignore.


### Change Log

0.1 - 06/08/2018

- Begin development. 
- Created github repository, readme, gitignore.
- Added development roadmap.

0.2 - 06/10/18

- Created `parse()` function to read IP addresses from /in/ files of 
type txt, log, and (eventually) csv.
- Added functionality to handle blank lines gracefully.
- Added debugging information. Set debugSet to `True` or 
`False` to control output level.
- Identified targets are stored in the `targets` table.
- Created second script oB-recon-configure.py to write an ini file. It 
will contain any credentials used during the scans, switches for 
scan activation or skipping, and any connection strings (if required).
- Created default.ini file (conf.ini)
- Added config parser to read ini file in main program.
- Created handling for n scan types to be configured. Configuration parser
can handle any given number of configured scans.
- Wrote programmatic way to create the ini that is customizable.
- Finished `scanselect(s,t)` function that will run the appropriate
named scans on the target when set to true in the config file.
- Moved printed output of debug to debugLog table.

0.3 - 6/11/18

- Added support for Mac and Windows pathing by `try, except` when setting import 
file paths.
- Added 'blank.ini' files to /in/, /out/, and /debug/. Changed .gitignore to 
contain exceptions for these files so the folders are created when downloading
the program.
- Wrote output method for debugLog to be recorded in a debut-timestamp file in 
the debug folder.
- Modified a lot of the output.
- Added `debug2()` function for post processing information.
- Added import for time module.
- Added `scanresults` table for recording scan result messages.
- Added handling for files in the /in/ folder that do not match specified file types on
both Mac and Win versions.
- Added ARIN lookup as 'scan3'; verified functionality.

0.4 - 7/10/18

- Added nmap quick scan as 'scan1'


