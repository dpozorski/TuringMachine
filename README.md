# Python Turing Machine

## Controllers

The available controllers for operating the Turing Machine are the table, binary_table, and network controllers.


### Table Controller

The implementation of the Turing Machine (for the table controller) follows the definition provided by Epstein and Carnielli in Computability, 3rd Edition. 

Specifically, it defines a 4-tuple of the form <state_n, tape_value, op, state_m> where the tuple <state_n, tape_value> define the next state state_m and the operation to perform prior to the state transition.

state_n, state_m belong to the set of all defined states, tape_value is the value currently read by the tape head at time t, and op defines the action to perform.

Epstein and Carnielli defined the set {0, 1} as the tape vocabulary and {0, 1, R, L} as the available actions. They can be represented by 1 and 2 bits, respectively.

Some additional flags are added to the state objects in the table controller to make execution easier. These flags indicate whether a given state is an initial, terminal, or exception states.

The table controller has a `to_binary` method that will convert it into a binary table.

Example: `q5 1 0 q6`

This tuple indicates moving from state `q5` to `q6` if `1` is read by the tape head. In such a case, the tape head is supposed to print `0` before the machine moves to state `q6`.



### Binary Table Controller

The binary table is a modified table controller, which encodes states, flags, and transitions into a control sequence.

Control sequences are composed of two state sequences and a condition bit:

Control Sequence: <State Sequence 1 (time-steps t/t-1), Condition Bit, State Sequence 2 (time-steps t+1/t)>

State Sequences have the form: <Identity Sequence, Operation Sequence>

The Identity Sequence is variable length and of the form: <(1) root bit, (n) label bits, (1) termination bit, (1) status bit>

The Operation Sequence is fixed in length: <(1) operation bit, (1) op parameter bit>

The Identity Sequence represents the state at time-step t and the Operation Sequence represents the transition operation (time-step (t-1)) before moving to the specified state.

The point of this encoding scheme is to concretize the notion of Turing Machines as functions f: N -> N.

Example:

The Control Sequence `0010000011001010010` can be interpreted as follows:

Breaking it up into its components: `001000001` `1` `001010010`

State Sequence 1: `001000001`
Condition Bit (tape head value): `1`
State Sequence 2: `001010010`

State Sequence 1 can be further parsed: `0010000` `01`
Identity Sequence 1: `0010000`
Operation Sequence 1: `01`

Operation Sequence 1 denotes moving (`0`) the tape head to the right (`1`).
Identity Sequence 1 can be fractured again: `0` `0100` `00`
The State is not a root/initial state (`0`).
The State has the label 4 (`0100`).
The State was transitioned to by a move operation to the left (`00`).


### Network Controller

The network controller is a trained binary controller; it memorizes the defined binary table's functional mapping.

In some sense it is a deliberate over-fitting of the data, but this over-fitting should generalize to the entire domain of possible input sequences to the tape head.

The goal of this network controller is to not simply have an "over-fitted" graph/network, but by using the semantics of Linear Logic construct a network in correspondence with a proof or truth-preserving structure. 

By this logical semantic definition, there should be a predictable convergence in the graph. This convergence is what is under investigation here.
 