#! /bin/bash
#This uninstalls MatooL. Please dont :(
del_matool(){
    echo "Uninstalling MatooL..."
    sudo rm -r /bin/matool
    sudo rm -r ~/.matool-documents
    echo "Done. You made me cry..."
}

#This is the main program. This just asks you if you really wanna uninstall this awesome script.
echo "Are you sure you want to uninstall this awesome tool? [Y/N]"
read answer
if [$answer=="Y"]; then
    del_matool()
elif [$answer=="y"]; then
    del_matool()
elif [$answer=="yes"]; then
    del_matool()
elif [$answer=="YES"]; then
    del_matool()
else
    echo "Phew. Aborting..."