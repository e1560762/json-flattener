from json import load

class JsonFlattener:
	DEFAULT_OUTPUT = "flattened_json.txt"

	def parse(json_obj):
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

		return result

	def read(fp):
		return load(fp)

	def flatten(input_path, indent=4, output_path=DEFAULT_OUTPUT):
		result = {}
		with open(input_path, "r") as fin:
			result = JsonFlattener.parse(JsonFlattener.read(fin))

		with open(output_path, "w") as fout:
			fout.write("{\n")
			for key, value in result.items():
				fout.write("{0}{1}: {2}\n".format(indent*" ",key, value))
			fout.write("}")