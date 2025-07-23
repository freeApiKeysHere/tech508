import json

# Read from the file
with open("servers.json", "r") as f:
    servers_dict = json.load(f)

for x in servers_dict.values(): # type of servers???
    print(x["role"])

print(servers_dict["server1"])
print(servers_dict["server2"])

#print(servers_dict["server2"]["role"])
def tricky():
    for x,y in servers_dict.items():
        print(f"Key and value: '{x}' = '{y}'")
        for x,y in y.items():
            print(f"    Record key and sub value: '{x}' = '{y}'")
print()
print()
print()
tricky()