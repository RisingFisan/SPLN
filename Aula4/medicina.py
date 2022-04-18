import re

from black import mask_cell

with open("medicina.xml") as f:
    content = f.read()

# remover elementos vazios
content = re.sub(r"<(\w+)>\s+</\1>","",content)

# remover páginas desnecessárias
content = re.sub(r".*<page number=\"20\" [^>]*>","",content,flags=re.S,count=1)
content = re.sub(r"<page number=\"544\".*","",content,flags=re.S,count=1)

content = re.sub(r'<text top=\"862\"[^>]*>.*?</text>',"",content)

content = re.sub(r"<text[^>]*>(.*?)</text>",r"\1",content,flags=re.S)

content = re.sub(r"<page[^>]*>","",content)
content = re.sub(r"</page>","",content)
content = re.sub(r"<fontspec[^>]*>","",content)

content = re.sub(r"\n[ \t]*\n","\n",content)
content = re.sub(r"V\nocabulario","",content)

def processEntry(entry : str):
    c = re.split(r'</b>',entry,maxsplit=1)
    m = re.fullmatch("\s*(\d+)\s*(.*?)\s*(\w+)", c[0])
    if m:
        print(m.groups())
    else:
        print(c[0].strip())

for entry in re.split(r'<b>', content)[1:]:
    processEntry(entry)


"""1  á    f</b>
<i>  Anatomía</i>
   es 
<i>ala</i>
   en 
<i>wing</i>
    pt 
<i>asa</i>
    la 
<i>ala</i>
"""