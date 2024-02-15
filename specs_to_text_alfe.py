import csv

specs = open("MALFE1_part.edn","r")
# part_keywords = ["ALFE2BGA_A","ALFE2BGA_B","ALFE2BGA_C","ALFE2BGA_D","ALFE2BGA_E","ALFE2BGA_F","ALFE2BGA_G","ALFE2BGA_H"]
part_keywords = ["ALFE2BGA"]
long_data = specs.read().splitlines()
data = list()
for i in range(len(part_keywords)):
    for j in range(len(long_data)):
        if long_data[j].find("cell " + part_keywords[i]) != -1:
            start = j
            for k in range(start+1, len(long_data)):
                if long_data[k].find("cell ") != -1:
                    stop = k
                    break
            for k in range(start, stop):
                data.append(long_data[k])
# these lines contain the info about ports, change them for your own use
# data = specs.read().splitlines()[418:1812]
specs.close()

# generates the list of ports with their raw data
port_indexes = list()
for i in range(len(data)):
    if data[i].find("(port ") != -1:
        port_indexes.append(i)
ports_list = list()
port_indexes.append(port_indexes[-1]+10) # adds a dummy entry to not break the next loop indexing
for i in range(len(port_indexes)-1):
    ports_list.append(data[port_indexes[i]:port_indexes[i+1]])

# set search keywords for desired parameters, these should be changed if different data is desired
direction_key = "direction "
designator_key = "designator \""
pintype_key = "PINTYPE  (string \""
rows = list()
for i in range(len(ports_list)):
    # extracting pin name, direction, number (designator), pin type
    # pin name in row 0
    pin_row = ports_list[i][0]
    pin_name = pin_row[pin_row.find("port")+5:].upper()
    # iterating over other rows to account for differing formats
    for j in range(len(ports_list[i])):
        direction_index = ports_list[i][j].find(direction_key)
        designator_index = ports_list[i][j].find(designator_key)
        pintype_index = ports_list[i][j].find(pintype_key)
        if  direction_index != -1:
            pin_direction = ports_list[i][j][direction_index + len(direction_key):-1] # ending index is -1 or -2 depending on format
        elif designator_index != -1:
            pin_number = ports_list[i][j][designator_index + len(designator_key):-2]
        elif pintype_index != -1:
            pintype = ports_list[i][j][pintype_index + len(pintype_key):-2] 
    pin_info = [pin_number, pin_name, pintype, pin_direction]
    rows.append(pin_info)

# sorting and file writing 
rows.sort()
header = ["Pin Number", "Pin Name", "Pin Type", "Pin Direction"]
filename = "alfe_part_data.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for i in range(len(ports_list)):
        csvwriter.writerow(rows[i])