def parser(line):
    line = line.strip()
    line = line.split('/')
    command = line[0].strip()
    if command[0] == '@':
        command = A_parser(command)
    elif command[0] != '(':
        command = C_parser(command)

    return command


def A_parser(command):
    """
    Divide A instruction into 2 parts
    return A_command = ('@', 'somenumber')
    """
    A_command = [command[0], command[1:]]
    return A_command


def C_parser(command):
    """
    Divide C_instruction into 3 parts
    return C_command = (dest, comp, jump) 
    """
    command = command.split(';')
    if len(command) == 2:
        jump = command[1].replace(" ", "")
    else:
        jump = 'null'    
    dest_comp = command[0]

    dest_comp = dest_comp.split('=')
    if len(dest_comp) == 2:
        dest = dest_comp[0].replace(" ", "")
        comp = dest_comp[1].replace(" ", "")
    else:
        dest = 'null'
        comp = dest_comp[0].replace(" ", "")

    return (dest, comp, jump)


if __name__ == '__main__':
    command = parser('D = D + 1; JMP')
    print(command)

