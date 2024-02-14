The repository contains a python script "specs_to_text" designed to parse the data from a netlist and format it into a csv.
The netlist "FLX155_V1" was made by a colleague based on a chip schematic (not included), and I needed to comapare it with the manufacturer's provided text file "xcvp1552vsva3340pkg".
The script is very simple. It takes advantage of the netlist's consistent formatting to extract the data, which it writes to "data.csv". Note that I had to modify the netlist (line 262 was not formatted consistently) and the script uses the modified file. 
Finally, "differences.xlsx" is a very simple spreadsheet that checks that the pin names and numbers in the text file and the csv are consistent.

The script was written in Python 3.11. Once it is run, it does not indicate whether or not it executed successfully, instead, users will need to check for "data.csv" in the same directory. 

There's a few things that may require changing to use this for a similar application. First, I indexed only the lines I needed from the netlist, which I determined manually. Similarly, my code utilizes that each pin had 9 lines about it in the netlist, and extracts the pin information from the naming scheme. 
