# CMS to Themis
# main.py file_name orig_inp orig_out ret_inp ret_out
# From a folder named "test" which include all the input and output files in CMS format
# -> Generate a folder named "result", inside "result" is the tests in Themis format

import os
import sys
from pathlib import Path

if len(sys.argv) != 6:
    sys.exit("Please follow the input format: main.py file_name orig_inp orig_out ret_inp ret_out")

file_name, orig_inp, orig_out, ret_inp, ret_out = sys.argv[1:]
if orig_inp == '0':
    orig_inp = ''
root = './test'
for file in os.listdir(root):
    if os.path.isdir(file):
        continue
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext != orig_inp and ext != orig_out:
        continue
    with open('./test/' + file, 'r') as f:
        contents = f.read()
    Path('./result/' + name).mkdir(parents=True, exist_ok=True)
    if ext == orig_inp:
        ret = ret_inp
    else:
        ret = ret_out
    with open('./result/' + name + '/' + file_name + '.' + ret, 'w') as f:
        f.write(contents)
