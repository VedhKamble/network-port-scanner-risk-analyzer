from datetime import datetime

def generate_report(target, results):
    target_sanitize=target.replace(".","_")
    current_datetime=datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_report_{target_sanitize}_{current_datetime}.txt"

    with open(filename, "w") as file:
        file.write("NETWORK PORT SCAN & RISK ANALYSIS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Target    : {target}\n")
        file.write(f"Scan Time : {datetime.now()}\n")
        file.write("=" * 60 + "\n\n")

        for item in results:
            file.write(f"Port           : {item['port']}\n")
            file.write(f"Service        : {item['service']}\n")
            file.write(f"Risk Level     : {item['risk']}\n")
            file.write(f"Risk Details   : {item['description']}\n")
            file.write("-" * 60 + "\n")

        file.write(
            "\nDisclaimer:\n"
            "This scan is intended for educational and authorized testing only.\n"
        )

    return filename

