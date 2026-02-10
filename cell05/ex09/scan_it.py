import sys, re

if len(sys.argv) < 3:
    print("none")
else:
    count = len(re.findall(sys.argv[1], sys.argv[2]))
    print(count if count > 0 else "none")
