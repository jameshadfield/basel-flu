import csv, sys

with open("./data/location_mapping.csv") as fh:
    data = csv.reader(fh, delimiter=',')
    next(data)
    
    
    for row in data:
        if row[1] == "NaN" or row[2] == "Nan":
            continue

        if row[0].isnumeric():
            # BLOC
            print("{}\t{}\t{}\t{}".format("bloc", int(row[0]), float(row[2]), float(row[1])))
        else:
            # DISTRICT -- note that lat/long order is reversed
            print("{}\t{}\t{}\t{}".format("district", row[0], float(row[1]), float(row[2])))

