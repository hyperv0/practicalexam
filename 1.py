line = input('Enter the line: ')

numupper = numlower = numalpha = numdigits = numsymbols = 0

for i in line:
    if i.isalpha():
        numalpha += 1
        if i.islower():
            numlower += 1
        elif i.isupper():
            numupper += 1
    elif i.isdigit():
        numdigits += 1
    else:
        if i != ' ':
            numsymbols += 1

print(f'Alphabets: {numalpha}')
print(f'Lowercase: {numlower}')
print(f'Uppercase: {numupper}')
print(f'Digits: {numdigits}')
print(f'Number of symbols: {numsymbols}')
    
