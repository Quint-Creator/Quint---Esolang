# === CONFIGURABLE COMMANDS ===
COMMANDS = {
    
    
    '1': 'right',
    '2': 'left',
    '3': 'up',
    '4': 'down',
    '5': 'inc',
    '6': 'dec',
    '7': 'loopL',
    '8': 'loopR',
    '9': 'pnum',
    '0': 'plet',
    '?': 'input',
    
    
    
}




# === Initialize 2D Tape ===
WIDTH, HEIGHT = 300, 300
tape = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# === Pointer Position ===
x, y = 0, 0  # Top-left start

def move_up():
    global y
    y = (y - 1) % HEIGHT

def move_down():
    global y
    y = (y + 1) % HEIGHT

def move_left():
    global x
    x = (x - 1) % WIDTH

def move_right():
    global x
    x = (x + 1) % WIDTH
    
def inc():
    tape[y][x] = (tape[y][x] + 1) % 256

def dec():
    tape[y][x] = (tape[y][x] - 1) % 256
    
 

def output_num():
    columnd = x
    value = sum(tape[y][columnd] for y in range(HEIGHT))
    print(value)

def output_let():
    print(chr(tape[y][x]), end='')
    
def input_cell():
    try:
        val = int(input("Input:"))
        tape[y][x] = val % 256
    except:
        print("Invalid input. Defaulting to 0.")
        tape[y][x] = 0
    
    
    
FUNCTIONS = {
    'right': move_right,
    'left': move_left,
    'up': move_up,
    'down': move_down,
    'inc': inc,
    'dec': dec,
    'pnum': output_num,
    'plet': output_let,
    'input': input_cell,
    
}

#for the loops
def match_loops(code):
    loop_stack = []
    loop_map = {}

    for pos, c in enumerate(code):
        if c == '7':  # loop start
            loop_stack.append(pos)
        elif c == '8':  # loop end
            start = loop_stack.pop()
            loop_map[start] = pos
            loop_map[pos] = start

    return loop_map

#this is for loading the code
def load_quint_code(filename):
    try:
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"🚫 File not found: {filename}")
    except Exception as e:
        print(f"⚠️ Error loading file: {e}")
    return []


# the interpreter
def run(code):
    
    
    
    ip = 0
    loop_map = match_loops(code)

    while ip < len(code):
        c = code[ip]
        cmd = COMMANDS.get(c)
        

        if cmd in FUNCTIONS:
            FUNCTIONS[cmd]()
        elif cmd == 'loopL':  # Jump forward if cell == 0
            if tape[y][x] == 0:
                ip = loop_map[ip]
        elif cmd == 'loopR':  # loop end
            if tape[y][x] != 0:
                ip = loop_map[ip]   # Go back to matching loopL
                
                


        ip += 1

#Some of the Strings and what they do:
        
        #Simply Prints HI: 5555555555715555555155555552268155015550
        
        #Prints Hello World:  555555555571555555515555555555155555555555
#                             15555555555515555555555515551555555555155555555
#                             55515555555555515555555555515555555555222222222
#                             226815515166166151551666151555516672817018

    #Basic Fibonacci Sequence Calculator ( up to 12 ) : 6111111111111155
#                                         76258445331675427145326847153542683319168

    #Truth Machine : ?71526819 
    

    #Simple Multiplication : ?1?27617645135284763548328119




if __name__ == '__main__':
    
    #input String of numbers into test object below
    test = load_quint_code("Quint_Code.txt")
    flat_code = [char for row in test for char in row]
    
    
    run(flat_code)
    
    
    
    
    
    
    
    
    