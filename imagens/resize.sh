#!/bin/bash
# Format the size of image to 300x300px to use in parley
# Elmar - 2024

files=$(ls *.jpg)

for i in $files
do
  name=$(basename $i .jpg)
  convert $name.jpg -resize 300x300 $name.2.jpg
done

exit