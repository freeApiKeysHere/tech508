
import json
# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
jsonStr = json.dumps(servers_dict)
print(jsonStr)

with open("generatedJson.json", "w") as f:
    json.dump(servers_dict, f, indent=4)

print("JSON file 'servers.json' created in current directory.")