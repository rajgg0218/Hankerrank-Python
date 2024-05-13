import re

def is_valid_uid(uid):
    # Rule 1: At least 2 uppercase English alphabet characters
    uppercase_count = len(re.findall(r'[A-Z]', uid))
    if uppercase_count < 2:
        return False

    # Rule 2: At least 3 digits (0 - 9)
    digit_count = len(re.findall(r'\d', uid))
    if digit_count < 3:
        return False

    # Rule 3: Only alphanumeric characters
    if not uid.isalnum():
        return False

    # Rule 4: No character should repeat
    if len(set(uid)) != len(uid):
        return False

    # Rule 5: Exactly 10 characters
    if len(uid) != 10:
        return False

    return True

# Read the number of test cases
t = int(input().strip())

# Validate each UID
for _ in range(t):
    uid = input().strip()
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")
