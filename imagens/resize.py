# Author: Elmar Uhl
# Locate and resize all files in a directory with size bigger than 300x300

import glob, os

diretorio = './'

padrao = ['*.jpg', '*.png']
#padrao = '*.jpg'
#padrao = '*.png'

size = int(600)

for p in padrao:
    print(f'Searching for {p} files')
    files = glob.glob(os.path.join(diretorio, p))
    filesInfo = []

    for file in files:
        command = 'identify -format \"%[fx:w] %[fx:h]\" ' + '\'' + file + '\''
        fileInfo = os.popen(command).read().split()
        temp = {'file' : file, 'width' : fileInfo[0], 'height' : fileInfo[1]}
        filesInfo.append(temp)

    #print(filesInfo)

    #for i in filesInfo:
    #    print(f'{i["file"]} {i["width"]} {i["height"]}')

    for i in filesInfo:
        if int(i['width']) > size or int(i['height']) > size:
            print(f'File {i["file"]} width = {i["width"]} height = {i["height"]}')
            command = f"convert \'{i['file']}\' -resize {size}x{size} \'{i['file'][2:-4]}.resized.jpg\'"
            os.system(command)
            print(f'File {i["file"]} resized to {size}x{size}')
