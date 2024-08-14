# privilege_data.py

privilege_info = [
    {"Privilege": "SeImpersonatePrivilege", "Exploitability": "Very High", "Explanation": "Impersonate a client after authentication.", "Example": "JuicyPotato/RoguePotato"},
    {"Privilege": "SeAssignPrimaryTokenPrivilege", "Exploitability": "High", "Explanation": "Replace a process level token.", "Example": "RottenPotatoNG"},
    {"Privilege": "SeLoadDriverPrivilege", "Exploitability": "High", "Explanation": "Load and unload device drivers.", "Example": "Capcom Driver Exploit"},
    {"Privilege": "SeBackupPrivilege", "Exploitability": "High", "Explanation": "Allows backing up files and directories, bypassing file system security.", "Example": "Copy SAM Hive"},
    {"Privilege": "SeRestorePrivilege", "Exploitability": "High", "Explanation": "Allows restoring files and directories, potentially overriding existing files.", "Example": "Overwrite System Files"},
    {"Privilege": "SeTakeOwnershipPrivilege", "Exploitability": "High", "Explanation": "Allows taking ownership of objects.", "Example": "Take Ownership"},
    {"Privilege": "SeDebugPrivilege", "Exploitability": "High", "Explanation": "Allows attaching a debugger to any process, including those running as SYSTEM.", "Example": "Debug SYSTEM Processes"},
    {"Privilege": "SeCreateTokenPrivilege", "Exploitability": "High", "Explanation": "Allows creating a security token.", "Example": "Token Forging (Churrasco)"},
    {"Privilege": "SeEnableDelegationPrivilege", "Exploitability": "High", "Explanation": "Allows delegation of user credentials to a remote server.", "Example": "Delegation Exploit (PrintNightmare)"},
    {"Privilege": "SeManageVolumePrivilege", "Exploitability": "Medium", "Explanation": "Grants ability to perform maintenance tasks on volumes.", "Example": "Volume Shadow Copy Manipulation"},
    {"Privilege": "SeRelabelPrivilege", "Exploitability": "Medium", "Explanation": "Allows modification of the mandatory integrity level of an object.", "Example": "Integrity Level Manipulation"},
    {"Privilege": "SeRemoteShutdownPrivilege", "Exploitability": "Medium", "Explanation": "Allows shutting down a system remotely.", "Example": "Remote Shutdown"},
    {"Privilege": "SeAuditPrivilege", "Exploitability": "Medium", "Explanation": "Allows generating security audits.", "Example": "Log Flooding"},
    {"Privilege": "SeChangeNotifyPrivilege", "Exploitability": "Low", "Explanation": "Allows bypassing traverse checking.", "Example": "Directory Traversal"},
    {"Privilege": "SeSystemtimePrivilege", "Exploitability": "Low", "Explanation": "Allows changing the system time.", "Example": "Timestamp Manipulation"},
    {"Privilege": "SeShutdownPrivilege", "Exploitability": "Low", "Explanation": "Allows shutting down the system.", "Example": "Local Shutdown"},
    {"Privilege": "SeLockMemoryPrivilege", "Exploitability": "Low", "Explanation": "Allows locking pages in memory.", "Example": "Rarely exploited directly."},
    {"Privilege": "SeMachineAccountPrivilege", "Exploitability": "Low", "Explanation": "Allows creating and joining computers to the domain.", "Example": "Domain Join Attack"},
    {"Privilege": "SeSecurityPrivilege", "Exploitability": "Very Low", "Explanation": "Allows viewing and modifying auditing and security log settings.", "Example": "Audit Log Tampering"},
]
