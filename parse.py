#!/usr/bin/env python
#-*-coding: utf-8-*-

import sys

if len(sys.argv) <2:
    print("{sys.argv[0]} READ_FILE_PATH")
    sys.exit(1)

path = sys.argv[1]
print(f"READ FILE {sys.argv[1]} ")

result_file = "./parse_result.csv"

target_1_name = "trade_id"
target_1_start=9
target_1_end=14

target_2_name ="value"
target_2_start=16
target_2_end=24

target_3_name ="req_flag"
target_3_start=14
target_3_end=15


line_cnt=1
with open(result_file,mode="w") as wf:
    with open(path) as rf:
        for line in rf:
            line = line.strip()
            #ヘッダスキップ
            if line_cnt == 1:
                line_cnt+=1
                print(f"{line}")
                continue
            print(f"{line}")
            target_1 = line[target_1_start:target_1_end]
            print(f"{target_1_name}:{target_1}")
            target_2 = line[target_2_start:target_2_end]
            print(f"{target_2_name}:{target_2}")
            target_3 = line[target_3_start:target_3_end]
            print(f"{target_3_name}:{target_3}")
            #フラグが立っていれば、-1で掛け算
            hosei = 1 if int(target_3) == 0 else -1

            calc = int(target_2)*hosei
            result_line =str(target_1) + "," + str(calc) + "\n"
            wf.write(result_line)