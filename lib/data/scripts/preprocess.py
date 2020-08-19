import os
import pandas as pd


def pad_sequence(df: pd.DataFrame, padding: int = 0) -> pd.DataFrame:
	"""
	Pad the sequence with dummy terminal
	state values for the provided padding
	length.

	:param df: pd.DataFrame, The dataframe to pad.
	:param padding: int, The length of the padding
	:return: pd.DataFrame

	"""

	padding = max(0, padding)

	if padding > 0 and len(df) > 0:
		items = list()
		i = df["input"][len(df) - 1]
		o = df["output"][len(df) - 1][:-2]

		if o[-2:] != "10":
			raise ValueError

		o = o + "1" + i

		for p in range(0, padding):
			items.append({
				"input": i,
				"output": o
			})

		df = df.append(items)

	return df


def trunc_sequence(df: pd.DataFrame, max_len: int = -1) -> pd.DataFrame:
	"""
	Truncate the length of the passed
	in dataframe to the max length.

	:param df: pd.DataFrame, The dataframe to truncate.
	:param max_len: int, The length to truncate the df to.
	:return: pd.DataFrame

	"""

	return df.truncate(after=(max_len - 1))


fp = os.path.abspath(__file__)
lib_data_path = os.path.dirname(os.path.dirname(fp))
root_path = os.path.dirname(os.path.dirname(lib_data_path))
raw_data_path = os.path.join(root_path, "training/data/raw")
data_path = os.path.join(root_path, "training/data/processed")

for op in os.listdir(raw_data_path):
	op_raw_data_dir_path = os.path.join(raw_data_path, op)
	op_data_dir_path = os.path.join(data_path, op)

	if os.path.isdir(op_raw_data_dir_path):
		for fn in os.listdir(op_raw_data_dir_path):
			op_raw_data_file_path = os.path.join(op_raw_data_dir_path, fn)

			if not os.path.isdir(op_raw_data_file_path):
				df = pd.read_csv(
					op_raw_data_file_path,
					dtype={
						'input': str,
						'output': str
					}
				)
				op_data_file_path = os.path.join(op_data_dir_path, fn)
				df = trunc_sequence(df=df, max_len=20)
				df = pad_sequence(df=df, padding=(20 - len(df)))
				df.to_csv(path_or_buf=op_data_file_path, index=False)
