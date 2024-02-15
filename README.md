The repository contains a python script "specs_to_text_alfe.py" designed to parse the data from a netlist and format it into a csv.
The netlist "MALFE1_part.edn" was made based on a chip schematic (not included), and I needed to comapare it with the manufacturer's provided text file "ALFE2 pinout type.xlsx". The task is to extract the pin names, numbers, and other information from the netlist so it can be compared. The script also works for the "MALFE_symbol.edn" file (which is organized differently), and gives the same results.

The script was written in Python 3.11. Once it is run, it does not indicate whether or not it executed successfully, instead, users will need to check for "alfe_data.csv" in the same directory. 
Some elements of the script will need changing to be adapted to your use. 
First, you will need to proide keywords for the script to find the part(s) you're looking for. Two examples are given in the code and comments - the part file only requires 1 keyword as all the data is under cell ALFE2BGA at line 401, while the symbol file divides the chip into parts A-H, requiring 8 keywords.
Next, lines 20-22 set search keywords for pin data. These should be changed depending on the desired data, as well as the ending indexes in lines 35, 37, and 39. Adding more data to be searched for is simple: add a keyword  like lines 20-22, add an indexing line like line 31, and add another elif statement. You may also want to change variable names and the labels in the output file (line 45).
