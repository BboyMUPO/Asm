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
    
    line = re.sub('LSL', '00000', line)
    
    line = re.sub('LSR', '00001', line)
    
    line = re.sub('ASR', '00010', line)
    
    line = re.sub('ADD', '0001100', line)
    
    line = re.sub('SUB', '0001101', line)
    
    line = re.sub('ADDS', '0001110', line)
    
    line = re.sub('SUBS', '0001111', line)
    
    line = re.sub('MOVS', '00100', line)
    
    line = re.sub('CMP', '00101', line)
    
    line = re.sub('AND', '0100000000', line)
    
    line = re.sub('EOR', '0100000001', line)
    
    line = re.sub('LSLS', '0100000010', line)
    
    line = re.sub('LSRS', '0100000011', line)
    
    line = re.sub('ASRS', '0100000100', line)
    
    line = re.sub('ADCS', '0100000101', line)
    
    line = re.sub('SBCS', '0100000110', line)
    
    line = re.sub('RORS', '0100000111', line)
    
    line = re.sub('BICS', '0100001110', line)
    
    print(line) 

line1=raw_input()

process_line(line1)
