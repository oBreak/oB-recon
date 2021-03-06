### Change Log

0.6 - 01/23/19

- Added `scan5(t)` code to scan for open NetBIOS ports, as possible responder targets.
- Added `scan6(t)` code to scan for LLMNR resolutions, as possible respodner targets.
- Added language for scan 5 and 6 in `README` and `oB-recon-configure.py`
- Added checker in boot for if program is run on Windows or Mac
- Determined that scan 1, 2, 4, 5, and 6 do *not* work on Windows, yet.

0.5 - 7/25/18

- Added placeholders for `scan1(t)` through `scan10(t)` in both `scans()` function 
and `scanselect(s,t)`. Just have to add the code/resources for the specific scans.
- Added checking for SSL configuration as `scan2(t)`. This runs `nmap
--script ssl-enum-ciphers -p 443 <target>`.
- Added ping sweep as `scan4(t)`.
- Added completion counter for scans, displaying x of y scans complete and percentage
complete (to one decimal)
- Added error handling for completion counter.
- Added support in `scans()` and `scanselect()` functions for scan 4-10.
- Updated readme, roadmap, changelog.

0.4 - 7/10/18

- Added nmap quick scan as 'scan1'
- Extracted changelog to be a separate file.

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

0.1 - 06/08/2018

- Begin development. 
- Created github repository, readme, gitignore.
- Added development roadmap.

