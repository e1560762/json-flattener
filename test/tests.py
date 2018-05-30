from flattener import JsonFlattener
from json import load
from os import listdir, getcwd
from os.path import isfile, join
import unittest

class TestJsonFlatter(unittest.TestCase):
	def setUp(self):
		self.CWD = getcwd()
		self.TEST_DIR = self.CWD + "/test/input/"

	def test_parse(self):
		onlyfiles = [join(self.TEST_DIR, f) for f in listdir(self.TEST_DIR) if isfile(join(self.TEST_DIR, f))]
		for f in onlyfiles:
			with open(f,"r") as fin:
				result = JsonFlattener._to_dict(JsonFlattener.parse(JsonFlattener.read(fin)))
				fin.seek(0)
				original = load(fin)
			self.assertEqual(result, original)
def main():
	suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonFlatter)
	unittest.TextTestRunner(verbosity=2).run(suite)