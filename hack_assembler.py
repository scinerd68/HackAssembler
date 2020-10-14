import hack_parser
import hack_code
import handle_symbol
import sys


def main(filename):
    symbol_table = handle_symbol.add_label(handle_symbol.symbol_table, filename)

    file = open(filename, 'r') 
    write_file = open(filename.split('.')[0] + '.hack', 'w')
    variable = 16 # store the address of current variable

    for line in file.readlines():
        if line[0] == '/' or len(line.strip()) == 0 or line[0] == '(':
            continue
        line = hack_parser.parser(line)

        # if it is an A instruction
        if len(line) == 2:
            try:
                line[1] = int(line[1])
            except ValueError:
                if line[1] not in symbol_table:
                    symbol_table[line[1]] = variable
                    line[1] = variable
                    variable += 1
                else:
                    line[1] = symbol_table[line[1]]

        line = hack_code.code(line)
        write_file.write(line + '\n')

    file.close()
    write_file.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python hack_assembler.py filename")
        sys.exit(1)
    else:
        main(sys.argv[1])
