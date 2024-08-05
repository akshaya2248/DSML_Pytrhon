source_file="file1.txt"
dest_file="file3.txt"
with open(source_file,'r')as source,open (dest_file,'w') as dest:
    content+source.read()
    dest.write(content)
print(f"content of '{source_file}' have been copied to '{dest_file}' ")
