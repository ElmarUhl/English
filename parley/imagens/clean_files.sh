#!/bin/bash
# Removing original files and renaming the modified files with original files names
# Elmar Uhl - 2024

echo Removing the original files...
rm *[^.2].jpg
rm *.png
echo Files removed

files=$(ls *.2.jpg)

echo Renaming modified files...
for file in $files
do
  name=$(basename $file .2.jpg)
  mv $name.2.jpg $name.jpg
done

exit