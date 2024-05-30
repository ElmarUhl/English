#!/bin/bash
# Converts png files to jpg files with size of 300x300px for use in parley
# Elmar - 2024

files=$(ls *.png)

for file in $files
do
  name=$(basename $file .png)
  convert $name.png -resize 300x300 -alpha remove $name.2.jpg
done

exit