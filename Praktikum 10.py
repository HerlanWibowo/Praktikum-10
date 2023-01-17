txt = 'Hello World'

print(len(txt))
print(txt[-1])
print(txt[2:5])
print(txt.replace(txt[5], ""))
print(txt.upper())
print(txt.lower())
print(txt.replace("H","J"))


umur = 24
txt2 = 'Hello, nama saya john, dan umur saya adalah {} tahun'

print(txt2.format(umur))