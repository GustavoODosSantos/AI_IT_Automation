# Logging Standards

## Why categorize log entries?

In IT troubleshooting, log files are often very large. Categorizing entries into `INFO`, `WARNING`, and `ERROR` helps engineers quickly identify what matters:

- **INFO** → Normal events (e.g., system started, service running).  
- **WARNING** → Something unusual that may need attention (e.g., low memory, high CPU).  
- **ERROR** → Critical failures that often explain why the user has an issue (e.g., disk not found, network unreachable).  

By automating log parsing, IT teams can:
- Save time by avoiding manual searches.  
- Focus directly on errors.  
- Provide structured data for future AI analysis.
