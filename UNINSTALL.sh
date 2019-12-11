#! /bin/bash
#This just removes the MatooL dir located by default on ~/.matool-documents
echo "This will remove the files generated in the MatooL generated directory, like the notes file."
echo "Are you sure you want to uninstall MatooL-Framework? [YES/NO]"
read answer
if [[$answer == "YES"]]; then
    echo "Okay..."
    rm -r ~/.matool-documents
else; then
    echo "Aborting..."
fi