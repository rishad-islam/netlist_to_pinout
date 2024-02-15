The repository contains a python script "specs_to_text_alfe.py" designed to parse the data from a netlist and format it into a csv.
The netlist "MALFE1_part.edn" was made based on a chip schematic (not included), and I needed to comapare it with the manufacturer's provided text file "ALFE2 pinout type.xlsx". The task is to extract the pin names, numbers, and other information from the netlist so it can be compared.

The script was written in Python 3.11. Once it is run, it does not indicate whether or not it executed successfully, instead, users will need to check for "alfe_data.csv" in the same directory. 
Several elements of the script will need changing to be adapted to your use. 
The most tedious part is needing to go into the netlist and manually infer which lines have the needed data, and input that to line 6. This is a limitation of the way I searched the data, using the "(port " keyword in line 12. The keyword appears in other places that aren't the desired data, necessitating the indexing in line 6.
Next, lines 20-22 set search keywords for pin data. These should be changed depending on the desired data, as well as the ending indexes in lines 35, 37, and 39. Adding more data to be searched for is simple: add a keyword  like lines 20-22, add an indexing line like line 31, and add another elif statement. You may also want to change variable names and the labels in the output file (line 45).
