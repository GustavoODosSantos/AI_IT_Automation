import json

def parse_log_file(input_line):
    """Parse the log file and return counts + error lines."""
    counts = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }
    error_lines = []

    with open(input_line, "r") as file:
        for line in file:
            if "INFO" in line:
                counts["INFO"] += 1
            if "ERROR" in line:
                counts["ERROR"] += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                counts["WARNING"] += 1
    return counts, error_lines
def save_summary(counts, output_file="log_summary.json"):
    """Save the summary counts to a JSON file."""
    with open(output_file, "w") as file:
        json.dump(counts, file, indent=4)

def save_errors(errors_lines, output_file="errors_found.txt"):
    """Save the error lines to a text file."""
    with open(output_file, "w") as file:
        for line in errors_lines:
            file.write(line + "\n")

if __name__ == "__main__":
    counts, errors = parse_log_file("sample.log")
    save_summary(counts)
    save_errors(errors)
    print("[DONE] Log summary saved to log_summary.json")
    print("[DONE] Error lines saved to errors_found.txt")
