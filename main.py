import os
import sys

root_dir = "./test"
if len(sys.argv) != 3:
    sys.exit("Please specify input file extension and output file extension!! Ex: python main.py inp out")
inp_extension = '.' + sys.argv[1]
out_extension = '.' + sys.argv[2]
ucode_testcases = []
for folder in os.listdir(root_dir):
    if os.path.isdir(os.path.join(root_dir, folder)):
        have_inp_and_out = 0
        for file_name in os.listdir(os.path.join(root_dir, folder)):
            if file_name.endswith(inp_extension):
                have_inp_and_out += 1
                with open(os.path.join(root_dir, folder, file_name), 'r') as file:
                    input_content = file.read()
            if file_name.endswith(out_extension):
                have_inp_and_out += 1
                with open(os.path.join(root_dir, folder, file_name), 'r') as file:
                    output_content = file.read()
        if have_inp_and_out != 2:
            continue
        testcase_index = str(len(ucode_testcases) + 1).zfill(2)
        next_testcase = "### Test #" + testcase_index + '\n' \
                        + input_content.rstrip() + '\n' \
                        + '---\n' \
                        + output_content.rstrip() + '\n'
        ucode_testcases.append(next_testcase)
with open('./testcases.txt', 'w') as file:
    file.write(''.join(ucode_testcases))
