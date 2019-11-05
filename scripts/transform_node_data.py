import sys, json

with open(sys.argv[1]) as fh:
    node_data = json.load(fh)


# transform hidden setting to an auspice compatable string
# auspice recognises: "always", "timetree", "divtree"
for node in node_data["nodes"]:
    if "hidden" in node_data["nodes"][node]:
        v = int(node_data["nodes"][node]["hidden"])
        if (v != 0):
            node_data["nodes"][node]["hidden"] = "always"
        else:
            del node_data["nodes"][node]["hidden"]

# transform bloc to integers, not floats
for node in node_data["nodes"]:
    for trait in ["bloc"]:
        if trait in node_data["nodes"][node]:
            try:
                node_data["nodes"][node][trait] = int(node_data["nodes"][node][trait])
            except ValueError:
                del node_data["nodes"][node][trait]


for node in node_data["nodes"]:
    # remove social score as per email 6-nov-2019
    if "socialscore" in node_data["nodes"][node]:
        del node_data["nodes"][node]["socialscore"]
    if "district" in node_data["nodes"][node] and node_data["nodes"][node]["district"] == "unknown":
        del node_data["nodes"][node]["district"]



with open(sys.argv[2], 'w') as fh:
    json.dump(node_data, fh, indent=2)
