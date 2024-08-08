# Write a program to search a word in a file and replace with another word.
file="file1.txt"
w1='welcome'
w2='hai'
with open(file,'r') as source:
    f1=source.read()
    content=f1.replace(w1,w2)
with open(file,'w') as source:
    source.write(content)
print(f"content of file {file} is replaced")
print(content)
