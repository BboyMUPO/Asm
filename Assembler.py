#A program that converts assembly code to machine code
#Works line by line
#For now only with a low support
#Don't converts decimal numbers to binary..converter avilible here:https://github.com/BboyMUPO/Convs/blob/master/decimal2binary

import re

print"=========="
print"[BboyMUPO]"
print"=========="
print""
print"ASSEMBLER"

def process_line(line):
    
    line = re.sub('PC', '0b1111', line)
              
    line = re.sub('SP', '0b1101', line)
    
    line = re.sub('BLX', '010001111', line)
    
    line = re.sub('ADDS', '00110', line)
    
    line = re.sub('MOV', '00100', line)
    
    line = re.sub('CMP', '00101', line)
    
    line = re.sub('STR', '01100', line)
    
    line = re.sub('LDR', '01101', line)
    
    line = re.sub('SVC', '11011111', line)
    
    line = re.sub('EQ', '0000', line)
    
    line = re.sub('NE', '0001', line)
    
    print(line) 

line1=raw_input()

process_line(line1)
