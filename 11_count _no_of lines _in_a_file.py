##Write a program to count number of lines in a file

count = 0
with open('earlier_date.py') as fp:
    for line in fp:
        if line.strip():
            count += 1

print('number of non-blank lines', count)
