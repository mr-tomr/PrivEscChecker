# PrivEscChecker

**PrivEscChecker** is a Python-based tool designed to analyze the output of the `whoami /all` command in Windows environments. It identifies potential privilege escalation paths based on Security Identifiers (SIDs), groups, and privileges that are present in the output. This tool is particularly useful for penetration testers and security researchers who need to quickly assess the privilege escalation risks in a Windows environment.

## Features

- **SID Analysis**: Identifies potentially exploitable SIDs that could lead to privilege escalation.
- **Group Analysis**: Detects dangerous groups that users might belong to, which could allow for privilege escalation.
- **Privilege Analysis**: Recognizes specific privileges that could be leveraged for privilege escalation attacks.
- **Detailed Output**: Provides explanations and example exploits for each identified risk.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package manager)

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine:

   ```bash
   git clone git clone https://github.com/user/PrivEscChecker.git
   cd PrivEscChecker
  
2. **Install Required Python Packages:**

   Install the necessary Python packages using pip:

     ```bash
    pip install -r requirements.txt
     ```

### Usage

**Preparing Input**

**Generate `whoami /all` Output:**

Run the following command in the Windows environment you want to analyze:

  ```bash
    whoami /all > whoami_output.txt
  ```
This will save the output to a file named whoami_output.txt.

**Execute the Script:**

Run the PrivEscChecker script with the generated `whoami_output.txt` as an argument:

  ```bash
  python3 priv_esc_checker.py whoami_output.txt
  ```
**Disclaimer**
This tool is intended for educational and professional purposes only. Unauthorized use of this tool in environments where you do not have explicit permission may be illegal and unethical. Always obtain proper authorization before performing security assessments.
