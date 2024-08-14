# sid_data.py

sid_info = [
    {"SID": "S-1-5-18", "Type": "Local", "Exploitability": "Very High", "Explanation": "NT AUTHORITY\\SYSTEM: The SYSTEM account has the highest level of privileges on a Windows system.", "Example": "Service Exploitation (MS16-032)"},
    {"SID": "S-1-5-19", "Type": "Local", "Exploitability": "High", "Explanation": "NT AUTHORITY\\LocalService: Runs services with minimum privileges.", "Example": "Service Exploitation (JuicyPotato)"},
    {"SID": "S-1-5-20", "Type": "Local", "Exploitability": "High", "Explanation": "NT AUTHORITY\\NetworkService: Runs services that access network resources.", "Example": "Service Exploitation (JuicyPotato)"},
    {"SID": "S-1-5-21domain-500", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Domain Admin (Administrator): The built-in Administrator account in a domain environment.", "Example": "Pass-the-Hash (Mimikatz)"},
    {"SID": "S-1-5-21domain-512", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Domain Admins Group: Full control over the domain.", "Example": "DCSync, DCShadow (Mimikatz, DCShadow)"},
    {"SID": "S-1-5-21domain-519", "Type": "Domain", "Exploitability": "Very High", "Explanation": "Enterprise Admins Group: Administrative tasks across all domains in a forest.", "Example": "Pass-the-Hash, Golden Ticket (Mimikatz)"},
    {"SID": "S-1-5-80", "Type": "Local", "Exploitability": "High", "Explanation": "NT SERVICE\\All Services: Represents all services running under service accounts.", "Example": "Service Exploitation (JuicyPotato)"},
    {"SID": "S-1-5-80-...", "Type": "Local", "Exploitability": "High", "Explanation": "NT SERVICE\\Service Accounts: Specific services such as MSSQL or other applications.", "Example": "Service Exploitation (varies by service)"},
    {"SID": "S-1-5-32-544", "Type": "Local/Domain", "Exploitability": "High", "Explanation": "BUILTIN\\Administrators: Full control over local resources.", "Example": "Token Manipulation, Pass-the-Hash"},
    {"SID": "S-1-5-32-547", "Type": "Local", "Exploitability": "Medium", "Explanation": "BUILTIN\\Power Users: Historically had significant privileges.", "Example": "DLL Injection, Registry Editing"},
    {"SID": "S-1-5-32-551", "Type": "Local/Domain", "Exploitability": "Medium", "Explanation": "BUILTIN\\Backup Operators: Back up and restore files bypassing file system security.", "Example": "SAM Hive Extraction"},
    {"SID": "S-1-5-32-555", "Type": "Local", "Exploitability": "Medium", "Explanation": "BUILTIN\\Remote Desktop Users: Remote access to the system.", "Example": "RDP Hijacking, Credential Stealing"},
    {"SID": "S-1-5-32-556", "Type": "Local", "Exploitability": "Medium", "Explanation": "BUILTIN\\Network Configuration Operators: Network configuration changes.", "Example": "Network Misconfiguration"},
    {"SID": "S-1-5-21domain-518", "Type": "Domain", "Exploitability": "Medium", "Explanation": "Schema Admins Group: Modify the Active Directory schema.", "Example": "Schema Modification"},
    {"SID": "S-1-5-21domain-520", "Type": "Domain", "Exploitability": "Medium", "Explanation": "Group Policy Creator Owners Group: Create and modify group policies.", "Example": "GPO Exploitation"},
    {"SID": "S-1-5-32-550", "Type": "Local/Domain", "Exploitability": "Medium", "Explanation": "BUILTIN\\Print Operators: Manage printers and potentially execute code in the context of SYSTEM.", "Example": "Driver Exploitation (PrintNightmare)"},
    {"SID": "S-1-5-32-549", "Type": "Local/Domain", "Exploitability": "Low", "Explanation": "BUILTIN\\Server Operators: Manage servers, including restarting and managing services.", "Example": "Service Exploitation"},
]
