from flattener import JsonFlattener
from sys import argv
import argparse
import constants

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=constants.Message.Informative.app_description())
	parser.add_argument(constants.Application.Arguments.INPUT, help=constants.Message.Informative.input_description(), dest="path_to_input")
	parser.add_argument(constants.Application.Arguments.OUTPUT, help=constants.Message.Informative.output_description(), dest="path_to_output", default=JsonFlattener.DEFAULT_OUTPUT)
	parser.add_argument(constants.Application.Arguments.INDENTATION, help=constants.Message.Informative.output_description(), dest="indent", default=4, type=int, choices=[2,4,8])
	parser.add_argument(constants.Application.Arguments.TEST)
	parsed = parser.parse_args()
	if constants.Application.Arguments.TEST in argv:
		try:
			from test.tests import main as test_main
			test_main()
		except Exception as e:
			print(str(e))
	elif len(argv) < 2 or constants.Application.Arguments.HELP in argv:
		print(constants.Message.Informative.usage())
	elif not parsed.path_to_input:
		print(constants.Message.Error.no_input_file())
		print(constants.Message.Informative.usage())
	else:
		JsonFlattener.flatten(parsed.path_to_input, parsed.path_to_output, parsed.indent)