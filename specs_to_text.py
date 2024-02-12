import csv
import re

specs = open("FLX155_V1_modified.edn","r")
# 30508 lines about the 3200 ports
data = specs.read().splitlines()[0:30508]
specs.close()

ports_list = list()
for i in range(len(data)):
    if data[i].find("(port ") != -1:
        ports_list.append(data[i:i+9]) # the edn file has 9 lines of data about each port

rows = list()
for i in range(len(ports_list)):
    # extracting pin number, name, bank number, io type
    pin_row = ports_list[i][1]
    pin = pin_row[pin_row.find("\"")+1:pin_row.find("\")")]
    
    pin_name_row = ports_list[i][2]
    pin_name = pin_name_row[pin_name_row.find("g \"")+3:-2]
    
    if re.search(r'\d''\d''\d', pin_name):
        bank = pin_name[-3:]
    else:
        bank = "NA"

    if "GTYP" in pin_name:
        io_type = "GTYP"
    elif "GTM" in pin_name:
        io_type = "GTM"
    elif "PMC_MIO" in pin_name:
        io_type = "PMCMIO"
    elif "LPD_MIO" in pin_name:
        io_type = "LPDMIO"
    elif "PMC_DIO" in pin_name:
        io_type = "PMCDIO"
    elif "IO_L" in pin_name:
        io_type = "XPIO"
    else:
        io_type = "NA"

    pin_info = [pin, pin_name, bank, io_type]
    rows.append(pin_info)

rows.sort()
header = ["Pin", "Pin Name", "Bank", "IO Type"]
filename = "data.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for i in range(len(ports_list)):
        csvwriter.writerow(rows[i])