#A program that converts armv6-m assembly code to machine code
#Works line by line
#For now only with a low function support
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
    
    line = re.sub('R0', '0b00000', line)
    
    line = re.sub('R1', '0b00001', line)
    
    line = re.sub('R2', '0b00010', line)
    
    line = re.sub('R3', '0b00011', line)
    
    line = re.sub('R4', '0b00100', line)
    
    line = re.sub('R5', '0b00101', line)
    
    line = re.sub('R6', '0b00110', line)
    
    line = re.sub('R7', '0b00111', line)
    
    line = re.sub('R8', '0b01000', line)
    
    line = re.sub('R9', '0b01001', line)
    
    line = re.sub('R10', '0b01010', line)
    
    line = re.sub('R11', '0b01011', line)
    
    line = re.sub('R12', '0b01100', line)
    
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
