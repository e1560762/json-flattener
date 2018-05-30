from json import load
import logging
logging.basicConfig(filename='flattener.log',level=logging.ERROR)

class JsonFlattener:
	DEFAULT_OUTPUT = "out_flattened_json.json"

	def parse(json_obj):
		try:
			queue = []
			result = {}
			for k,v in json_obj.items():
				if isinstance(v, dict):
					queue.append((k,v))
				else:
					result[k] = v
			while queue:
				key,value = queue.pop(0)
				for inner_key, inner_value in value.items():
					if isinstance(inner_value, dict):
						queue.append((".".join([key,inner_key]), inner_value))
					else:
						result[".".join([key,inner_key])] = inner_value
		except Exception as e:
			logging.error("In JsonFlattener.parse: {0}".format(str(e)))
		finally:
			return result

	def read(fp):
		try:
			stream = load(fp)
		except Exception as e:
			logging.error("In JsonFlattener.read: {0}".format(str(e)))
			stream = None
		finally:
			return stream

	def flatten(input_path, output_path, indent=4):
		try:
			result = {}
			with open(input_path, "r") as fin:
				result = JsonFlattener.parse(JsonFlattener.read(fin))

			with open(output_path, "w") as fout:
				fout.write("{\n")
				for key, value in result.items():
					if isinstance(value, str):
						value = "\\\"".join(value.split("\""))
						value = "\"%s\"" % (value)
					elif isinstance(value, bool):
						if value:
							value = "true"
						else:
							value = "false"
					elif value is None:
						value = "null"
					fout.write("{0}\"{1}\": {2}\n".format(indent*" ",key, value))
				fout.write("}")
		except Exception as e:
			logging.error("In JsonFlattener.flatten: {0}".format(str(e)))

	def _to_dict(flat_dict):
		original = {}
		current_level = None
		for key,value in flat_dict.items():
			separate_keys = key.split(".")
			current_level = original
			while separate_keys:
				top = separate_keys.pop(0)
				if not top in current_level and separate_keys:
					current_level[top] = {}
				if separate_keys:
					current_level = current_level[top]
				else:
					current_level[top] = value
		return original
