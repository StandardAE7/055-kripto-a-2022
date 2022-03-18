from pwn import xor

str = "label"
result = ""

for c in str:
    result += chr(ord(c)^13)

print(f"crypto{{{result}}}")