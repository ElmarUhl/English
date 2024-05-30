# CSV to KVTML file converter
# Author: Elmar Uhl - 2024

# Reading the input file
def readfile(file):
    text = []
    fi = open(input_name, 'r')
    text = fi.readlines()
    fi.close()
    
    n = len(text)
    for i in range(0,n):
        text[i] = text[i].replace('\n','') # Remove \n from strings
    print(text)
    return text

# Function to convert the file
def convert(txt):
    from datetime import date
    
    # File header
    texto = ['<?xml version="1.0" encoding="UTF-8"?>','<!DOCTYPE kvtml PUBLIC "kvtml2.dtd" "http://edu.kde.org/kvtml/kvtml2.dtd">','<kvtml version="2.0">','  <information>','    <generator>csv2kvtml</generator>']
    
    # Get user information
    title = input('Type title of colection: ')
    author = input('Type the author: ')
    license = input('Type the license: ')
    comment = input('Type a comment: ')
    category = input('Type a category: ')
    
    texto.append(f'    <title>{title}</title>')
    texto.append(f'    <author>{author}</author>')
    texto.append(f'    <license>{license}</license>')
    texto.append(f'    <comment>{comment}</comment>')
    texto.append(f'    <date>{date.today()}</date>')
    texto.append(f'    <category>{category}</category>')
    
    texto = texto + ['  </information>','  <identifiers>','    <identifier id="0">','      <name>English (world)</name>','      <locale>en_001</locale>','    </identifier>','    <identifier id="1">','      <name>português (Brasil)</name>','      <locale>pt_BR</locale>','    </identifier>','  </identifiers>']

    n = len(txt) # Length of list argument
    # The for below introduces:
    #<entries>
    #  <entry id="0">
    #    <translation id="0">
    #      <text>English</text>
    #    </translation>
    #    <translation id="1">
    #      <text>Portuguese</text>
    #    </translation>
    #  </entry>
    # (...)
    #</entries>
    texto.append('  <entries>')
    for i in range(0, n): 
        texto.append(f'    <entry id=\"{i}\">')
        entry = txt[i].split(sep='\t')
        for ii in range(0,2):
            texto.append(f'      <translation id=\"{ii}\">')
            texto.append(f'        <text>{entry[ii]}</text>')
            texto.append('      </translation>')
        texto.append('    </entry>')
    texto.append('  </entries>')
    
    #<lessons>
    #  <container>
    #    <name>Vocabulary</name>
    #    <inpractice>true</inpractice>
    #    <entry id="0"/>
    # (...)
    #  </container>
    #</lessons>
    texto.append('  <lessons>')
    texto.append('    <container>')
    texto.append('      <name>Vocabulary</name>')
    texto.append('      <inpractice>true</inpractice>')
    for i in range(0, n):
        texto.append(f'      <entry id=\"{i}\"/>')
    texto.append('    </container>')
    texto.append('  </lessons>')

    # Tag to end file        
    texto.append('</kvtml>')
    
    return texto


def save_file(txt):
    print('-'*50)
    output_name = input('Type the output file name: ')
    f = open(output_name, 'w')
    for i in txt:
        f.write(f'{i}\n')
    f.close()
    
def show_screen (txt):
    for i in txt:
        print(i)    
    

# MAIN PROGRAM
print('-'*50)
input_name = input('Type input file name: ')
texto = readfile(input_name) # Reading csv file 
texto = convert(texto) # Converting to kvtml format
save_file(texto)
#show_screen(texto) # Show in screen the kvtml file
