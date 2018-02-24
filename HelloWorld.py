#!/usr/bin/env python3

import subprocess


cmd = subprocess.Popen(r'C:\jhove\jhove.bat -m TIFF-hul '.format(imageName.rstrip()), stdout=subprocess.PIPE, universal_newlines=True)

rowList = []

for line in cmd.stdout:
    if 'RepresentationInformation' in line:
        # print(line.partition(':')[2])
        rowList.append(line.partition(':')[2])
    elif 'Status' in line:
        rowList.append(line.partition(':')[2])
    elif 'ErrorMessage' in line:
        print(line)
        rowList.append(line.partition(':')[2])
rowTuple = tuple(rowList)
tiffwriter.writerow(rowTuple)