# Risk classification based on real-world attack surface

HIGH_RISK = {
    21: "FTP transmits credentials in clear-text, making it vulnerable to credential theft.",
    22: "SSH is often targeted by brute-force and credential-stuffing attacks.",
    23: "Telnet does not use encryption and exposes credentials.",
    137: "NetBIOS can leak system and network information.",
    138: "NetBIOS is a legacy protocol vulnerable to information disclosure.",
    139: "SMB can be abused for lateral movement inside networks.",
    445: "SMB is commonly exploited by ransomware and worms.",
    3389: "RDP is frequently targeted for unauthorized remote access.",
    3306: "MySQL exposure can lead to unauthorized database access.",
    5432: "PostgreSQL may expose sensitive application data.",
    27017: "MongoDB is often misconfigured with no authentication.",
    6379: "Redis may allow unauthorized data access or command execution.",
    5900: "VNC allows remote desktop access and can be brute-forced.",
    2375: "Docker API can give full control over containers.",
    2049: "NFS may expose shared files without proper authentication.",
    1433: "MSSQL exposure can compromise enterprise databases.",
    1521: "Oracle DB services expose critical business data.",
    2483: "Oracle DB services may be exploited if exposed publicly.",
    2484: "Encrypted Oracle DB services still expose sensitive assets.",
    4444: "This port is commonly used by exploitation frameworks.",
    7001: "WebLogic has a history of critical remote code execution flaws.",
    9000: "PHP-FPM exposure may allow remote code execution.",
    2181: "Zookeeper exposure can allow cluster takeover."
}

MEDIUM_RISK = {
    25: "SMTP may be abused for spam or email relay attacks.",
    53: "DNS services can be abused for amplification attacks.",
    80: "HTTP traffic is unencrypted and vulnerable to interception.",
    110: "POP3 may expose email credentials in clear-text.",
    143: "IMAP may expose mailbox data if misconfigured.",
    119: "NNTP services are rare but may be misconfigured.",
    123: "NTP can be abused for DDoS amplification attacks.",
    161: "SNMP may expose sensitive system information.",
    179: "BGP misconfigurations can affect network routing.",
    389: "LDAP exposure may leak directory information.",
    587: "SMTP submission services require strong authentication.",
    989: "FTPS is encrypted but still exposes file services.",
    990: "FTPS is encrypted but still sensitive if misconfigured.",
    3000: "Development servers may expose debug interfaces.",
    3690: "Subversion repositories may leak source code.",
    5601: "Kibana dashboards may expose internal analytics.",
    6667: "IRC is often used for botnet communication.",
    8000: "Alternate HTTP ports often host test services.",
    8080: "HTTP proxy or admin panels may be exposed.",
    9200: "Elasticsearch often exposes data without authentication."
}

LOW_RISK = {
    443: "HTTPS uses encryption to protect data in transit.",
    465: "SMTPS provides encrypted email transmission.",
    500: "ISAKMP is used for VPN key exchange.",
    636: "LDAPS encrypts directory authentication.",
    8443: "Alternate HTTPS port with encrypted communication.",
    2083: "cPanel SSL provides encrypted admin access.",
    2087: "WHM SSL provides encrypted admin access.",
    2096: "Webmail SSL encrypts user credentials."
}

def assess_risk(port):
    if port in HIGH_RISK:
        return "HIGH", HIGH_RISK[port]
    elif port in MEDIUM_RISK:
        return "MEDIUM", MEDIUM_RISK[port]
    elif port in LOW_RISK:
        return "LOW", LOW_RISK[port]
    else:
        return "MEDIUM", "Unknown service detected; further investigation is recommended."


    