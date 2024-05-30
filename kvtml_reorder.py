# Reorder entry indexes in kvtml files
# Elmar Uhl - 2024

# Reading input file
def readFile(fileName):
    text = []
    #fi = open('modulo-1.kvtml','r')
    fi = open(fileName,'r')
    text = fi.readlines()
    fi.close()
    return text

# Change and replace values
def changeValues(lower, upper, new_lower, text):
    # Creates a list with all entry to be changes
    old_limits = []
    for n in range(lower, upper + 1):
        old_limits.append(f'entry id=\"{n}\"')

    # Creates a list with all entry changed
    new_upper = (upper - lower + 1) + new_lower
    new_limits = []
    for n in range(new_lower, new_upper):
        new_limits.append(f'entry id=\"{n}\"')

    # Creates a list flag to identify if a line was changed
    changed = []
    for n in range(0,len(text)):
        changed.append(0)

    # Read list with input file lines and change the lines
    for nStd in range(0, len(old_limits)):
        for nlT in range(0, len(text)):
            if text[nlT].find(old_limits[nStd]) != -1 and changed[nlT] == 0:
                text[nlT] = text[nlT].replace(old_limits[nStd],new_limits[nStd])
                changed[nlT] = 1
            
    return text

def saveFile(text):
    outputFile = input('Type the name of output file: ')
    fo = open(outputFile, 'a')
    
    for l in text:
        fo.write(l)
    fo.close()
    

# PROGRAMA PRINCIPAL
print('-'*60)
inputFile = input('Type filename of the kvtml input file: ')
text = readFile(inputFile)

lower_limit = int(input('Type the number of lower entry index in input file: '))
upper_limit = int(input('Type the number of upper entry index in input file: '))
new_lower_limit = int(input('Type the new lower number entry index: '))

text = changeValues(lower_limit,upper_limit, new_lower_limit, text)
saveFile(text)

for i in text:
    print(i,end='')