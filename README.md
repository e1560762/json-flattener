# Json Flattener
Returns path to every terminal value in a JSON structure.

## Installing / Getting started
Compatible with Python 3.5

For installing instructions, please look at https://www.python.org/downloads/

After installing Python 3.5. You can either clone the code,

```shell
mkdir <FOLDER>
cd <FOLDER>
git clone https://github.com/e1560762/json-flattener.git --branch master
```

or download as a zip file and extract the content to a specific folder.
After downloading the source code, you can run the code from command line,

```shell
cd <FOLDER>/json-flattener
python run.py --input <path to input file> [--output <path to output file>] [--indent <number of spaces>]
```

## Features
* Converts nested json objects to single level json objects and writes to a file.
* Merges keys in a branch using ".". For example {"1":{"2":{"3":none}}} is transformed to {"1.2.3": none}
* Does not parse array objects.

### Parameters
* --input: (Required) Path to file that includes the JSON structure.
* --output: (Optional) Path to file that includes the processed JSON structure.
* --indent: (Optional) Number of spaces that will be printed in front of each entry. Can be 2,4 or 8.
