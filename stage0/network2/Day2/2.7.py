import subprocess
import re

result = subprocess.run(["ss" , "-ltnu" , "-src" , "127.0.0.1"] , capture_output=True , text=True)
for line in result.stdout.splitlines():
    match = re.search(r':(\d+)\s', line)
    if match:
        port = match.group(1)
        print(f"Open port found: {port}")

