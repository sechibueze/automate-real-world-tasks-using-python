#!/usr/bin/bash

# Create an empty file to contain all old references to "jane"
> oldFiles.txt

# Retrieve files from list with jane
files=$(grep  ' jane '  ./list.txt | cut -d " " -f 3)
echo "$files"
for  i in $files; do echo "hey $i";
    if test -e "$i";
        then echo "$i" ;#>> oldFiles.txt;
    else echo "Not founf $i"; 
    fi
done
# echo "$files"