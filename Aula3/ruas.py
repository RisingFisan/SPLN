from dataclasses import replace
import pickle
import re

with open("ruasBraga_v1") as f:
    text = f.read()

with open("nomes.pck","rb") as f:
    nomes = pickle.load(f)

# replaced_text = re.sub(fr"\b({'|'.join(nomes)})\b", r"@\1@", text)
fs = lambda m: f"@{m[1]}@" if m[1] in nomes else m[1]
replaced_text = re.sub(fr"\b([A-ZÂÁÓÉ]\w+)\b", fs, text)

replaced_text = re.sub(r"@\s*@", " ", replaced_text)

replaced_text = re.sub(r"@\s*(d(?:e|o|a)s?)\s*@", r" \1 ", replaced_text)

print(replaced_text)