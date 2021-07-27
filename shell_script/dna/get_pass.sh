#!/bin/bash

cat ${vcf_file} | grep -v "^#" | grep "PASS" | cut -f7 | uniq -c
#grep -v "^#" ${vcf_file} | grep "PASS" | cut -f7 | uniq -c
