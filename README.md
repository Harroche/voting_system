# Voting_system
A single transferable voting system which works off txt/excel to python 

**Voting_system_excel**

Library’s used 
  Pyrankvote
  	Used for the voting system 
    To download “pip install pyrankvote”
  Openpyxl
    Used to read the excel sheet
    To download “pip install openpyxl”
    
Format of excel 
I used to google sheets which automatically collects time completed, email and password. So our first vote will always be on the D column last can vary.  The last column checks the validity of the voter if in database it will result in a 1, 0 if not. If 0 will not count the vote

Python programme 
Takes in the excel file. Selects which sheet in the file and then goes through verficantion counts votes and outputs the results. 

The only areas need to be edited 
Line 11 might need to be edited if your first vote does not start on column D 



**Voting_system_text**

1. Install library’s used
```bash
    pip install pyrankvote
```
    
    
Format of txt 
Each line is a vote. With left most being highest vote and the right most being the lowest vote. The names of each candidate should be separated only by a tab space. When the line is finished should start a new line. You will have to manually have to get rid of the false votes do not included in text file.

Python programme 
Takes in the txt file reads it and outputs the vote.   
