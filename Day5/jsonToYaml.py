import sys
import os
import json
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")
    exit(1)

# 1. Convert the JSON to YAML - use yaml library
yml = yaml.dump(source_content, default_flow_style=False)

# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
if len(sys.argv) < 3:
    print(yml)
    exit(0)

target_file = sys.argv[2]

# 2.2 Check the target file doesn't already exist
if os.path.exists(target_file):
    print("ERROR: " + target_file + " already exists")
    exit(1)

# 2.3 If previous conditions not met, then save YAML file
with open(target_file, "w") as f:
    f.write(yml)

print(f"YAML successfully written to {target_file}")
