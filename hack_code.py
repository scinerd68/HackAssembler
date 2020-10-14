def code(command):
    if len(command) == 2:
        return A_instruction(command)
    return C_instruction(command)
    

def A_instruction(command):
    """
    command: a list that has 2 elements: @, some_number
    """
    machine_code = '0'
    machine_code += str(bin(int(command[1]))[2:].zfill(15))
    return machine_code


def C_instruction(command):
    """
    command: a tuple that has 3 elements: dest, comp, jump
    return the machine_code of the command
    """
    machine_code = '111'
    dest, comp, jump = command
    comp_table = {
        '0': '0101010', '1': '0111111', '-1': '0111010',
        'D': '0001100', 'A': '0110000', '!D': '0001101', '!A': '0110001',
        '-D':'0001111',  '-A':'0110011', 'D+1':'0011111','A+1':'0110111',
        'D-1':'0001110', 'A-1':'0110010', 'D+A':'0000010',
        'D-A':'0010011', 'A-D':'0000111',  'D&A':'0000000','D|A':'0010101',             
        'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111', 
        'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111', 
        'D&M':'1000000', 'D|M':'1010101' }

    dest_table = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A' : '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }

    jump_table = {
        'null': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }


    machine_code = machine_code + comp_table[comp] + dest_table[dest] + jump_table[jump]
    return machine_code