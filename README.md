The repository contains a python script "specs_to_text" designed to parse the data from a netlist and format it into a csv.
The netlist "FLX155_V1" was made by a colleague based on a chip schematic (not included), and I needed to comapare it with the manufacturer's provided text file "xcvp1552vsva3340pkg".
The script is very simple. It takes advantage of the netlist's consistent formatting to extract the data, which it writes to "data.csv". 
