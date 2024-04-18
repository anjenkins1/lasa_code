import re

def split_at_first_digit(s):
    match = re.search(r'\d', s)
    if match:
        return s[:match.start()], s[match.start():]
    else:
        return s, ""

def split_addresses(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    before_digits = []
    after_digits = []

    for line in lines:
        before, after = split_at_first_digit(line.strip())
        before_digits.append(before)
        after_digits.append(after)

    return before_digits, after_digits

def export_to_combined_file(data, file_name):
    with open(file_name, "w") as file:
        for item in data:
            file.write(item + "\n")

# Read data from the file and split addresses
before_digits, after_digits = split_addresses("address.txt")

# Combine all before_digits into one text file
export_to_combined_file(before_digits, "combined_before_digits.txt")

# Combine all after_digits into one text file
export_to_combined_file(after_digits, "combined_after_digits.txt")
