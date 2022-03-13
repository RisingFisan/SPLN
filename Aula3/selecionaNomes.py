import getopt
import os
import pickle
import re
import shutil
import sys

PATH = os.path.expanduser('~/.PLN')

opts, args = getopt.getopt(sys.argv[1:], "n")

if not os.path.isdir(PATH):
    try:
        original_umask = os.umask(0)
        os.makedirs(PATH, mode=0o777)
    finally:
        os.umask(original_umask)
    shutil.copy("nomes.pck",PATH)

FILE = None

print(opts, args)

if len(args) == 1:
    FILE = args[0]
elif len(args) > 1:
    print("Error - too many arguments")
    exit(127)
else:
    print("Error - file not specified")
    exit(127)

NORMAL_MODE = True

for f, a in opts:
    if f == '-n':
        NORMAL_MODE = False

with open(FILE, encoding='UTF-8') as f:
    text = f.read()

with open(PATH + "/nomes.pck","rb") as f:
    nomes = pickle.load(f)

# replaced_text = re.sub(fr"\b({'|'.join(nomes)})\b", r"@\1@", text)
fs = lambda m: f"@{m[1]}@" if m[1] in nomes else m[1]
replaced_text = re.sub(fr"\b([A-ZÂÁÓÉ]\w+)\b", fs, text)

replaced_text = re.sub(r"@\s*@", " ", replaced_text)

replaced_text = re.sub(r"@\s*(d(?:e|o|a)s?)\s*@", r" \1 ", replaced_text)

if NORMAL_MODE:
    print(replaced_text)
else:
    print(re.findall(r"@[\w\s]*@", replaced_text))