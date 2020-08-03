from lib.utilities.JSONDeserializer import JSONDeserializer
from lib.utilities.TapeGenerator import TapeGenerator
from lib.TuringMachine import TuringMachine
from lib.Head import Head
import json
import os

###################################################################################
# ******************** START - RECOMMENDED STEPS FOR EXECUTION ********************
###################################################################################
#
# 1) Update the controller_type (table, binary_table, or network)
# 2) Update the operation_type (addition, multiplication, or successor)
# 3) Update the tape generator (addition, multiplication, or succession)
#
###################################################################################
# ******************** END - RECOMMENDED STEPS FOR EXECUTION **********************
###################################################################################

# build deserializer
deserializer = JSONDeserializer()

# define the controller type
controller_type = "table"

# define the operation type
operation_type = "addition"

if operation_type == "addition":
	tape = TapeGenerator.addition(a=3, b=5)
elif operation_type == "multiplication":
	tape = TapeGenerator.multiplication(a=1, b=1)
else:
	tape = TapeGenerator.succession(a=1)

# define config file paths
root_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(root_path, "config")
example_path = os.path.join(root_path, "/".join(["input", operation_type]))
controller_path = os.path.join(config_path, "/".join(["controller", controller_type]))

# define the controller_path and tape_head_path
controller_path = os.path.join(controller_path, operation_type + ".json")

# load in extractor JSON definition
with open(controller_path) as f:
	json_string = json.load(f)

# Convert JSON object to configured Python TM Controller
controller = deserializer.deserialize(obj_json=json_string)

# Construct the tape head
tape_head = Head(tape=tape)

# construct the Turing Machine
tm = TuringMachine(controller=controller, tape_head=tape_head)

# execute the TM
tm.run()
