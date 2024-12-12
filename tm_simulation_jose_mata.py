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
        self.tape_alphabet = ['_', '1', '0']
        self.current_state = 'q1' #This attribute can change
        self.next_state = 'q1' #This attribute can change

    def transition_function(self, current_state, input):
        if input == '1' or input == '0':
            self.write_value = '0'
            self.direction_to_move = 'R'
            if current_state == 'q1':
                self.next_state = 'q2'
            elif current_state == 'q2':
                self.next_state = 'q1'
        elif input == '_':
            self.write_value = '_'
            self.direction_to_move = 'S'
            self.next_state = self.accept_state

        return (self.next_state, self.write_value, self.direction_to_move)
    
    def print_transition_function(self, current_state, input):
        state = "δ({}, {}) = ({}, {}, {})\n".format(current_state, input, self.next_state, self.write_value, self.direction_to_move)  
        return state  


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
    tape = [] #The tape will simply be a list. It can be "infinite" since lists in Python are dynamic and can be made larger or smaller as needed. The current head position can be tracked by following the index of the list
    for character in input_string:
        tape.append(character)
    return tape

#The "print_tape" function converts the tape list into a string with no spaces in between the characters
def print_tape(tape):
    current_tape = ""
    for character in tape:
        current_tape = current_tape + character
    return current_tape

#The "option_1" function allows the user to write the input to the Turing Machine and checks that it is valid
def option_1(tm1):
    input_string = input("Type your input string. It can ONLY be '1's, '0's BUT the final character MUST be an underscore '_':\n")
    input_valid = check_input_string(input_string, tm1.input_alphabet) #sends the input alphabet of the turing machine as the second parameter 
    if input_valid == True:
        tape = load_tape(input_string)
        print("Input is valid and was succesfully written to the tape.\n")
        return tape
    else:
        print("Error. Tape CANNOT contain a character not from the input alphabet.\n")
        return [] #This line is included for options 2 and 3 to not work if the input was invalid.

#The "option_2_and_3" function allows the user to either step-through the Turing Machine program or run it to full completion.
def options_2_and_3(tm1, step_through, tape):
    index = 0
    step = 0
    while tm1.current_state != tm1.accept_state:
        tm1.next_state, tm1.write_value, tm1.direction_to_move =tm1.transition_function(tm1.current_state, tape[index]) #carry out transition function 
        step = step + 1
        #print info
        print("Step: " + str(step) + "\n")
        print("State: " + tm1.current_state + "\n")
        print("Tape: " + print_tape(tape) + "\n")
        number_of_spaces = " " * index
        print("Head: " + number_of_spaces + "^\n")
        print("Next: " + tm1.print_transition_function(tm1.current_state, tape[index]) + "\n")
        #write a '0' unless it is the last character (blank)
        if tm1.write_value == '0': 
            tape[index] = '0'
        elif tm1.write_value == '_':
            tape[index] = '_'
        #move to the right unless it is the last character 
        if tm1.direction_to_move == 'R':
            index = index + 1
        #the current state becomes the next state for the while loop to begin again
        tm1.current_state = tm1.next_state
        if step_through == True:
            enter = input("Press 'Enter' to continue.\n")
    print("The output tape is: " + print_tape(tape) + "\n\n")

#tm1 is the instance of the Turing Machine used in this application
tm1 = Turing_machine()

print("Welcome to Jose Mata's Turing Machine Simulator Program!\n")
#This is the main menu which calls the funtions for each respective option. 
main_answer = 0
tape = []
while main_answer != 5:
    main_answer =  input("Please select one of the following choices:\nEnter '1' to enter your input.\nEnter '2' to step through the Turing Machine's steps.\nEnter '3' to run the Turing Machine's program to completion.\nEnter '4' to reset the Turing Machine.\nEnter '5' to exit this Turing Machine Simulator program.\n")
    if main_answer == '1':
        tape = option_1(tm1)
    elif main_answer == '2':
        if len(tape) == 0:
            print("You must enter an input first using Option 1.\n")
        else:
            print("Performing a step-through of the Turing Machine's program.")
            options_2_and_3(tm1, True, tape)
    elif main_answer == '3':
        if len(tape) == 0:
            print("You must enter an input first using Option 1.\n")
        else:
            print("Running to the Turing Machine program to completion...")
            options_2_and_3(tm1, False, tape)
    elif main_answer == '4':
        tm1 = Turing_machine() #Reset turing machine
        tape = [] #Reset tape
        print("Turing Machine has been reset. Choose option 1 to enter a new input.\n")
    elif main_answer == '5':
        print("Exiting the program...\n")
        break
    else: 
        print("Answer is invalid.\n")










        





