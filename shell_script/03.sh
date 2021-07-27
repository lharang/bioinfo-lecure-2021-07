#!/bin/bash

src="/home/ubuntu/shell_script"

for gene in `cat ${src}/genelist.txt`
do
	python3 ${src}/02.py ${gene}
done

