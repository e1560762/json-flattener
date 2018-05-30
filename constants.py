class Application:
	NAME = "flattener.py"
	class Arguments:
		INPUT = "--input"
		OUTPUT = "--output"
		HELP = "-h"
		INDENTATION = "--indent"
		TEST = "--test"

class Message:
	class Error:
		def no_input_file():
			return "Please identify an input file."
	class Informative:
		def usage():
			return "Usage: python {0} {1} INPUT_FILE [{2} OUTPUT_FILE] [{3} NUMBER_OF_SPACES]".format(
				Application.NAME, Application.Arguments.INPUT,
				Application.Arguments.OUTPUT, Application.Arguments.INDENTATION
				)
		def app_description(): return "Returns path to every terminal value in a JSON structure."
		def input_description(): return "Path to file that includes the JSON structure."
		def output_description(): return "Path to file that includes the processed JSON structure."
		def indent_description(): return "Number of spaces that will be printed in front of each \
		entry. Can be 2,4 or 8"