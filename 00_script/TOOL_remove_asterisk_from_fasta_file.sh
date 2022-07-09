#!/bin/bash

#Sweep the dust off

echo ""
echo "    ||                              "
echo "    ||                              "
echo "    ||                              "
echo "    ||                              "
echo "    ||                              "
echo "    ||                              "
echo "    ||     Sweeping the asterisk off"
echo "    ||                              "
echo "   /||\                             "
echo "  /||||\                            "
echo "  ======         __|__              "
echo "  ||||||        / ~@~ \             "
echo "  ||||||       |-------|            "
echo "  ||||||       |_______|            "
echo ""
echo "The asterisks will be removed by all the following *.fasta file:"
find .. -type f -name '*.fasta' -printf "   - %f\n"
echo ""
echo "This operation will OVERWRITE the original files."
read -r -p "Are you sure that you want to proceed? [y/N] " response
case "$response" in
    [yY][eE][sS]|[yY])
        echo ""
        find .. -type f -name "*.fasta" -exec sed -i 's/*//g' {} ';'
        echo "Done."
        ;;
    *)
        echo "Nothing has be done."
        echo ""
        ;;
esac

echo""
echo "Have a beutiful day!"
echo ""