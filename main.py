from scanner import scan_ports
from services import get_service
from risk import assess_risk
from report import generate_report

def main():
    print("=== Network Port Scanner & Risk Analyzer ===")
    target = input("Enter target IP or domain: ")

    top_ports = [
        21,22,23,25,53,80,110,119,123,137,138,139,143,161,179,
        389,443,445,465,500,587,636,989,990,1433,1521,2049,
        2082,2083,2086,2087,2095,2096,2181,2375,2483,2484,
        3000,3306,3389,3690,4444,5432,5601,5900,6379,6667,
        7001,8000,8080,8443,9000,9200,27017
    ]

    open_ports = scan_ports(target, top_ports)
    results = []

    print("\nScan Results:")
    print("-" * 60)

    for port in open_ports:
        service = get_service(port)
        risk, description = assess_risk(port)

        results.append({
            "port": port,
            "service": service,
            "risk": risk,
            "description": description
        })

        print(f"Port {port}")
        print(f" Service      : {service}")
        print(f" Risk Level   : {risk}")
        print(f" Risk Details : {description}")
        print("-" * 60)

    if results:
        report_file = generate_report(target, results)
        print(f"\nReport saved as: {report_file}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
