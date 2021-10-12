# Testcase-Themis-to-Ucode
A python file to read the testcase of Themis and convert to Ucode (testcases.txt)

# How to use
1. Download **main.py** file.

2. Copy the testcase of the problem in Themis format to your current working directory (location of your **main.py** file). Rename the folder to **test**. 
(inside **test** there will be multiple testcase folder, each folder contains an INPUT file and an OUTPUT file. (Usually with ``.inp`` and ``.out`` extension)

3. Run the main.py file from command line with 2 additional arguments specify the INPUT file extension and the OUTPUT file extension. 

4. The problem will generate a **testcases.txt** file (or replace existing one) at your working folder.

# Example

We're at directory ``D:/Projects/Themis to Ucode``.

In the directory we will have these files:

![](./example_pics/exam1.png)

When we run the main.py file with ``inp`` and ``out`` extension at the same directory (Depend on the extension you can change: ``inp`` and ``ans``, ``in`` and ``ok``, ...):

```
python main.py inp out
```
![](./example_pics/exam2.png)

There will be a **testcases.txt** file generated with Ucode testcase format:

![](./example_pics/exam3.png)

Copy **testcases.txt** to where you need to put it. <3