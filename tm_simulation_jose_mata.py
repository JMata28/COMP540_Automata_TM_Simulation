#This is Jose Mata's Submission for COMP 540 Automata - Turing Machine Simulator Project
#Fall 2024, Bridgewater State University 


class turing_machine:
    states = ['q1', 'q2']
    input_alphabet = ['_', '1', '0']
    tape_alphabet = ['_', '1', '0', 'H']
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
    initial_state = 'q1'
    accept_state = 'A'
    reject_state = 'R'
    
tape = []

tm1 = turing_machine()

tm1.transition_function(1, 'q1')
print(tm1.print_transition_function())

