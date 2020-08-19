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
controller_type = "binary_table"

# define the operation type
operation_type = "successor"

# operation param 1
param_1 = 14

# operation param 1
param_2 = 15

# The label padding to pad the output label with
label_padding = -1

# The log file name
log_file = os.path.join("training/data/raw", operation_type)

if operation_type == "addition":
	label_padding = 2
	tape = TapeGenerator.addition(a=param_1, b=param_2)
	name = str(param_1) + "_plus_" + str(param_2) + ".csv"
	log_file = os.path.join(log_file, name)
elif operation_type == "multiplication":
	label_padding = 0
	tape = TapeGenerator.multiplication(a=param_1, b=param_2)
	name = str(param_1) + "_times_" + str(param_2) + ".csv"
	log_file = os.path.join(log_file, name)
else:
	label_padding = 6
	tape = TapeGenerator.succession(a=param_1)
	name = "succeed_" + str(param_1) + ".csv"
	log_file = os.path.join(log_file, name)

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

# Close the controller's undefined input states
tm.controller.close_domain()

# Rebase the labels
tm.controller.rebase()

# execute the TM
tm.run()

# export the execution log
tm.log.export_csv(
	filepath=log_file,
	label_padding=label_padding
)
