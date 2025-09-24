# AI_IT_Automation
### Overview
This project was designed to automates system diagnostics for IT Team
It gather systems information (os, user name, disk usage, RM usage, and IP address) and outputs in a JSON report, and logging execution history

# Usage
Run the script from project root:
bash
python scripts/diagnostics.py

### Log Parser
The Log_parser.py script analyzes .log files and produces two outputs:
'log_summary.json' -> counts the number of INFO, WARNING, and ERROR entries.
'errors_found.txt' -> contains all ERROR lines extracted from the log.

# How to run
from the project root:
'''bash
python scripts/log_parser.py
