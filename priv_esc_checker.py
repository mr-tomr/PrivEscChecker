# priv_esc_checker.py

import re
import sys
import pandas as pd
from sid_data import sid_info
from group_data import group_info
from privilege_data import privilege_info

def load_data():
    try:
        sid_df = pd.DataFrame(sid_info)
        group_df = pd.DataFrame(group_info)
        privilege_df = pd.DataFrame(privilege_info)
        return sid_df, group_df, privilege_df
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def check_sids(text, sid_df):
    found_sids = []
    for sid in sid_df['SID']:
        if sid in text:
            found_sids.append(sid)
    return found_sids

def check_groups(text, group_df):
    found_groups = []
    for group in group_df['Group']:
        if group in text:
            found_groups.append(group)
    return found_groups

def check_privileges(text, privilege_df):
    found_privileges = []
    for privilege in privilege_df['Privilege']:
        if privilege in text:
            found_privileges.append(privilege)
    return found_privileges

def main():
    if len(sys.argv) != 2:
        print("Usage: python priv_esc_checker.py <whoami_output.txt>")
        print("Please provide the path to the file containing the output of 'whoami /all'.")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please provide a valid file path.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    sid_df, group_df, privilege_df = load_data()

    sids = check_sids(text, sid_df)
    groups = check_groups(text, group_df)
    privileges = check_privileges(text, privilege_df)

    if not sids and not groups and not privileges:
        print("No potential privilege escalation paths found.")
        return

    if sids:
        print("\nPotentially exploitable SIDs found:")
        print(sid_df[sid_df['SID'].isin(sids)].to_string(index=False))

    if groups:
        print("\nPotentially exploitable Groups found:")
        print(group_df[group_df['Group'].isin(groups)].to_string(index=False))

    if privileges:
        print("\nPotentially exploitable Privileges found:")
        print(privilege_df[privilege_df['Privilege'].isin(privileges)].to_string(index=False))

if __name__ == "__main__":
    main()
