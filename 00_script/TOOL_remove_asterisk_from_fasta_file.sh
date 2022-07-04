#!/bin/bash


echo ""
echo "Attention!"
echo ""

read -r -p "This operation will overwrite the original files. Are you sure that you want to proceed? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY])
        echo ""
        find .. -type f -name '*.fasta' -exec sed -i 's/*//g' {} \;
        echo "Well, now it's done. Nice choice."
        echo "Have a beutiful day!"
        echo ""
        ;;
    *)
        echo "no"
        ;;
esac