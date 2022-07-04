#!/bin/bash

find .. -type f -name '*.fasta' -exec sed -i 's/*//g' {} \;

