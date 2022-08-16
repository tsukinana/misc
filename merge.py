#!/usr/bin/env python
#-*-coding: utf-8-*-

import sys

if len(sys.argv) <2:
    print("{sys.argv[0]} READ_FILE_PATH")
    sys.exit(1)

path = sys.argv[1]
print(f"READ FILE {sys.argv[1]} ")

result_file = "./merge_result.csv"

id = ""
before_id = ""
point_temp = 0
line_cnt = 0

with open(result_file,mode="w") as wf:
    with open(path) as rf:
        for line in rf:
            line_cnt +=1
            
            line = line.strip().split()
            id=line[0]
            point_value = int(line[1])
            
            if line_cnt == 1:
                before_id = id
                point_temp = int(point_value)
                continue
                       
            if id == before_id:
                point_temp += int(point_value)
            else:
                result_line=str(before_id) + "," + str(point_temp) + "\n"
                wf.write(result_line)
                
                before_id = id
                point_temp = int(point_value)
        result_line=str(before_id) + "," + str(point_temp) + "\n"
        wf.write(result_line)
      