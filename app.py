from settings import * # pipelining restrictions
import time

''' ==== START OF STEP 1. VALIDATION AND PARSING OF INSTRUCTION SET ===='''
# reads instruction.txt
def read(fp):
   pass

# validates the length of instruction set
def validate(lines):
   pass

# parses the instruction set
def parse(lines):
    pass
''' =========================  END OF STEP 1 ========================= '''


''' ============= START OF STEP 2. FIVE-STAGE PIPELINING ============= '''

''' ------------------ start of main functions ----------------------- '''
# performs five-stage design pipelining on valid instruction set
def pipelining(instructions):
   pass

# pipes D E M W on next instructions with hazards
def mainstage1(instruction):
    pass

# loops in order, perform stalls if there are hazards, otherwise the sequential stages D E , W
def mainstage2(instructions, instruction, code, decode, execute, memory, writeback, past):
   pass
''' ------------------- end of main functions ------------------------ '''

''' ------------------- start of helper functions -------------------- '''
 # appends pipes for first instruction
def first(instructions):
    pass

# gets instructions with hazards RAW, WAR, WAW
def getHazards(instructions, clk): 
    pass

# initializes succeeding instructions by introducing wait '-' and fetch 'F'
def init(instruction, clock):
    pass

# places stalls on succeeding instructions with hazards
def stalls(instructions, hazards, i):
    pass

# marks the stage existing, if an instruction has performed that stage
def staging(stage, instruction, char):
    pass

# on stages with no duplicates on same column, append corresponding char stage
def noDuplicates(instruction, decode, execute, memory, writeback):
    pass

# checks if an instruction is a hazard or not
def isHazard(instructionTest, char):
    pass

# appends stalls on an instruction
def waiting(instruction):
    pass
''' --------------------- end of helper functions -------------------- '''

''' =========================  END OF STEP 2 ========================= '''
 
''' ============ START OF STEP 3. DISPLAY OUTPUT PROCESS ============= '''
# displays the pipes based on five-stage design and three-operand format
def display(pipes):
    pass

''' =========================  END OF STEP 3 ========================= '''

''' ==================== START OF MAIN DRIVER ======================== '''
# boots the pipelining app
def boot():
   pass

boot() # boot caller
''' ==================== END OF MAIN DRIVER ======================== '''

