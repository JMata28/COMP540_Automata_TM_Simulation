# COMP540_Automata_TM_Simulation
This is Jose Mata's submission for COMP 540 - Automata "Turing Machine Simulator Project"

Fall 2024, Bridgewater State University

## Instructions for Running the Python File
Run the "CFG_jose_mata.py" file with Python 3.12.2 64-bit

## What the Program Does
This program simulates a Turing Machine that accepts inputs consisting of 0s and/or 1s and ending with an underscore "_". The program simulated for the Turing Machine then converts every 1 and 0 into a 0. This simualtion allows for a step-by-step or a complete execution of the processing of the input string, so the user can see the current step, state, tape, head position, and transition function at any point of the process. 

Upon running the program, you'll be prompted to select one of the following options (or steps). Simply choose a number from 1 to 5 to select an option. You'll be able to choose as many options as desired until you choose option 5, which terminates the program. The following are the choices, each of which is explained in further detail below: 
* '1' to enter your input.
* '2' to step through the Turing Machine's steps.
* '3' to run the Turing Machine's program to completion.
* '4' to reset the Turing Machine.
* '5' to exit this Turing Machine Simulator program.

Any input besides a number from 1 to 5 will result in an "Answer is invalid." message 

**IMPORTANT: The input from the user MUST begin with a 1 or a 0 (not an underscore) and MUST end with an underscore for the simulation to produce the desired output**

### Option 1 - Enter Input
This option allows the user to enter the input (the content of the tape that is fed to the Turing Machine). The program checks that only 0s, 1s, and underscore characters are in the input to accept it as valid. 

### Option 2 - Step through the Turing Machine's steps
This option allows the user to see the Turing Machine's program working step-by-step. The user must press Enter to go on to the next step until the program shows the resulting tape and displays the main menu again. This option is only going to work as expected when the user has previously entered a valid tape input using Option 1. 

Selecting Option 2 after obtaining the resulting tape of a previous input and before reseting the Turing Machine will result in the simulation simply displaying the resulting tape from the previous input that was correctly processed. To change the input tape of the Turing Machine, Option 4 must be selected to reset the Turing Machine and then Option 1 must be selected to enter the new input. After this, Option 2 will show the processing of the newest tape input.

### Option 3 - Run the Turing Machine's Program to Completion
This option the runs Turing Machine's program and displays the steps all at once after the program is completed. This option is only going to work as expected when the user has previously entered a valid tape input using Option 1. 

Selecting Option 3 after obtaining the resulting tape of a previous input and before reseting the Turing Machine will result in the simulation simply displaying the resulting tape from the previous input that was correctly processed. To change the input tape of the Turing Machine, Option 4 must be selected to reset the Turing Machine and then Option 1 must be selected to enter the new input. After this, Option 3 will show the processing of the newest tape input.

### Option 4 - Reset the Turing Machine
This option resets the input tape and the entire Turing Machine itself. After selecting this option, the user should select Option 1 to enter a new valid input for the tape. 

### Option 5 - Terminate the Program
The program finishes.