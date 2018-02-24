#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import subprocess
import csv

def main():
    with open('LADailyNewsReport.csv', 'w', newline='') as csvfile:
        tiffwriter = csv.writer(csvfile, delimiter=',')
        tiffwriter.writerow(('FileName','Status','Error Message'))

        f = open('C:\jhove\images.txt')
        for imageName in f:
            cmd = subprocess.Popen(r'C:\jhove\jhove.bat -m TIFF-hul {}'.format(imageName.rstrip()), stdout=subprocess.PIPE, universal_newlines=True)

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


if __name__ == '__main__': main()
