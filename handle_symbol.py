symbol_table = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6, 
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4 
}

def add_label(symbol_table, filename):
    count_line = 0
    file = open(filename, 'r') 
    for line in file.readlines():
        line = line.strip()
        if len(line) == 0 or line[0] == '/':
            continue
        if line[0] == '(':
            symbol_table[line[1:-1]] = count_line
            continue
        count_line += 1
    file.close()
    return symbol_table

if __name__ == '__main__':
    symbol_table = add_label(symbol_table, 'ASMFile/Max.asm')
    print(symbol_table)