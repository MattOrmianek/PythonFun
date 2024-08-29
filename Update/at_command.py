import re

print("AT COMMAND TESTING: ")
out = '[LTE Monitor Service] out:  +QCSQ: "GSM",-82 OK'


pattern = r"(-\d+)"

# Search for the pattern in the string
match = re.search(pattern, out)
signal_strength = match.group(1)


print(f"signal_strength: {signal_strength}")
