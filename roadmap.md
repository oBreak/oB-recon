### Development Roadmap

- Add encryption checking as scan 2 (available certificates and ciphers)
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