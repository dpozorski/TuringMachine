from lib.utilities.JSONDeserializer import JSONDeserializer
import json
import os

###################################################################################
# ******************** START - RECOMMENDED STEPS FOR EXECUTION ********************
###################################################################################
#
# 1) Update the controller_type (table or network)
# 2) Update the operation_type (addition, multiplication, successor)
# 3) Update the example (example-XXX)
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

# select the example file to load in
example = "example-001"

# define config file paths
root_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(root_path, "config")
example_path = os.path.join(root_path, "/".join(["input", operation_type]))
controller_path = os.path.join(config_path, "/".join(["controller", controller_type]))

# define the controller_path and tape_head_path
controller_path = os.path.join(controller_path, operation_type + ".json")
tape_head_path = os.path.join(example_path, example + ".json")

# load in extractor JSON definition
with open(controller_path) as f:
	json_string = json.load(f)

# Convert JSON object to configured Python TM Controller
controller = deserializer.deserialize(obj_json=json_string)

# load in Tape Head JSON definition
with open(tape_head_path) as f:
	json_string = json.load(f)

# Convert JSON object to configured Python Transformer object
tape_head = deserializer.deserialize(obj_json=json_string)
