# python main.py file_name inp out
# It is assumed that all the files in "test" end with .txt

from pathlib import Path
import os
import sys

if len(sys.argv) != 4:
    sys.exit("Please follow the input format: python main.py file_name inp out")
file_name, inp, out = sys.argv[1:]
if Path('./test/in').exists():
    for file in os.listdir('./test/in'):
        with open('./test/in/' + file, 'r') as f:
            contents = f.read()
        name = os.path.splitext(file)[0]
        Path('./result/' + name).mkdir(parents=True, exist_ok=True)
        with open('./result/' + name + '/' + file_name + '.' + inp, 'w') as f:
            f.write(contents)
else:
    sys.exit("There is no folder \'in\' inside \'test\'")

if Path('./test/out').exists():
    for file in os.listdir('./test/out'):
        with open('./test/out/' + file, 'r') as f:
            contents = f.read()
        name = os.path.splitext(file)[0]
        Path('./result/' + name).mkdir(parents=True, exist_ok=True)
        with open('./result/' + name + '/' + file_name + '.' + out, 'w') as f:
            f.write(contents)
else:
    sys.exit("There is no folder \'out\' inside \'test\'")