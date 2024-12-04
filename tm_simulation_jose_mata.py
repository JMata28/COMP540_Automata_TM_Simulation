#This is Jose Mata's Submission for COMP 540 Automata - Turing Machine Simulator Project
#Fall 2024, Bridgewater State University 

#This is the data structure that represents the Turing Machine at any given point during the program.
class Turing_machine:

    def __init__(self):
        self.initial_state = 'q1'
        self.accept_state = 'F'
        self.reject_state = 'R'    
        self.states = [self.initial_state, 'q2', self.accept_state, self.reject_state]
        self.input_alphabet = ['_', '1', '0'] #The '_' represents a blank character 
        self.tape_alphabet = ['_', '1', '0', 'H'] #The 'H' means that the program has halted, so the H is at the end of the output on the tape
        

    def transition_function(self, input, current_state):
        if input == 1 or input == 0:
            self.write_value = 0
            self.direction_to_move = 'R'
        if current_state == 'q1':
            self.next_state = 'q2'
        else:
            self.next_state = 'q2'
    def print_transition_function(self):
        return "Write value: {}\nDirection to move: {}\nNext state: {}\n".format(self.write_value, self.direction_to_move, self.next_state)        


#The tape will simply be a list. It can be "infinite" since lists in Python are dynamic and can be made larger or smaller as needed.    
#The current head position can be tracked by following the index of the list
tape = []

#The "check_input_string" function makes sures that the input entered by the user is only made up of characters in the input_alphabet
#The input alphabet is initiated in the instance of the turing machine and must be sent in as the "input_alphabet" parameter of this function 
def check_input_string(input_string, input_alphabet):
    input_valid = True 
    for character in input_string:
        if character not in input_alphabet:
            input_valid = False
    return input_valid

#The "load_tape" function "loads" the input from the user to the tape that will be the input of the Turing Machine
def load_tape(input_string):
    tape = []
    for character in input_string:
        tape.append(character)
    return tape

#tm1 is the instance of the Turing Machine used in this application
tm1 = Turing_machine()

input_string = input("Type your input string. It can only be '1's, '0's, or '_'s:\n")
input_valid = check_input_string(input_string, tm1.input_alphabet) #sends the input alphabet of the turing machine as the second parameter 
if input_valid == True:
    tape = load_tape(input_string)
    #print("The contents of the tape are: " + str(tape))
else:
    print("Tape CANNOT contain a character not from the input alphabet.\n")





        





