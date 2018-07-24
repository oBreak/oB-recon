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
- Extracted changelog to be a separate file.

