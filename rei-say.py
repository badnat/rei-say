import os
import sys
def textBubble():
    l = ""
    longest = 0
    lines = []
    for line in sys.stdin:
        lines = lines + [line.rstrip().replace("\t", "    ")]
        if(len(line.replace("\t", "    ")) > longest):
            longest = len(line.replace("\t", "    "))
    for line in lines:
        l = l + "| " + line + " " * (longest - len(line)) + "|" + "\n"
    l = " " + "_" * (longest) +"\n" + l + " " + "_" * (longest) + "\n"
    l = l + "   \  |" + "\n" + "    \ |" + "\n" + "     \|"
    return l

print(textBubble())
f = open(os.path.expanduser('~/rei-say/reiText'))
rei = f.read()
os.system(rei)
f.close()
