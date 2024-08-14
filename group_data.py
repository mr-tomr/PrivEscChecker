# group_data.py

group_info = [
    {"Group": "BUILTIN\\Administrators", "Type": "Local/Domain", "Exploitability": "Very High", "Explanation": "Full control over local resources.", "Example": "Token Manipulation, Pass-the-Hash"},
    {"Group": "NT AUTHORITY\\SYSTEM", "Type": "Local", "Exploitability": "Very High", "Explanation": "Highest level of privileges on the system.", "Example": "Service Exploitation (MS16-032)"},
    {"Group": "Domain Admins", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Full control over the domain.", "Example": "Pass-the-Hash, DCSync, DCShadow"},
    {"Group": "Enterprise Admins", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Administrative tasks across all domains in a forest.", "Example": "Pass-the-Hash, Golden Ticket"},
    {"Group": "Schema Admins", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Modify the Active Directory schema.", "Example": "Schema Modification"},
    {"Group": "Domain Controllers", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Control over domain controllers.", "Example": "DCSync, DCShadow"},
    {"Group": "BUILTIN\\Remote Desktop Users", "Type": "Local", "Exploitability": "High", "Explanation": "Remote access to the system.", "Example": "Credential Stealing, RDP Hijacking"},
    {"Group": "BUILTIN\\Backup Operators", "Type": "Local/Domain", "Exploitability": "High", "Explanation": "Back up and restore files, bypassing file system security.", "Example": "SAM Hive Extraction"},
    {"Group": "BUILTIN\\Power Users", "Type": "Local", "Exploitability": "High", "Explanation": "Historically had significant privileges.", "Example": "DLL Injection, Registry Editing"},
    {"Group": "BUILTIN\\Print Operators", "Type": "Local/Domain", "Exploitability": "Medium", "Explanation": "Manage printers and potentially execute code in the context of SYSTEM.", "Example": "Driver Exploitation (PrintNightmare)"},
    {"Group": "NT AUTHORITY\\Authenticated Users", "Type": "Local/Domain", "Exploitability": "Medium", "Explanation": "Authenticated users with access to certain system resources.", "Example": "Privilege Escalation via Misconfigurations"},
    {"Group": "NT AUTHORITY\\Local Service", "Type": "Local", "Exploitability": "Medium", "Explanation": "Runs services with minimum privileges.", "Example": "Service Exploitation (JuicyPotato)"},
    {"Group": "NT AUTHORITY\\Network Service", "Type": "Local", "Exploitability": "Medium", "Explanation": "Runs services that access network resources.", "Example": "Service Exploitation (JuicyPotato)"},
    {"Group": "BUILTIN\\Performance Monitor Users", "Type": "Local", "Exploitability": "Medium", "Explanation": "Monitor perf. counters, possible gathering sens data.", "Example": "Information Disclosure"},
    {"Group": "NT SERVICE\\ALL SERVICES", "Type": "Local", "Exploitability": "Medium", "Explanation": "Represents all services running under service accounts.", "Example": "Service Exploitation (JuicyPotato)"},
]
