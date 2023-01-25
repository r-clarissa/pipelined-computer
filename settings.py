
'''
    Title: Exercise 09: Programming Pipelined Computer
    Author: Clarissa G. Rodriguez
    Date: November 29, 2022
    Description: Accepts a list of instructions and outputs onscreen the pipelined version of processing those instructions.
'''

stageDesign = ['D', 'E', 'M', 'W'] 
operations = ['add', 'mul', 'sub', 'div'] 
registers = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15']
min = 1
max = 20
stall = 'S'
wait = '-'
fetch = 'F'
dec = 'D'
exec = 'E'
mem = 'M'
write = 'W'
fp = "data/instruction.txt" 
err = "\nFailed to pipeline.\nTry fixing the dataset."