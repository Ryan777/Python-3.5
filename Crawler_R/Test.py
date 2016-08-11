#coding=utf-8
import re
string = "rlive.live.media_hd_24_20160701131743.flv"

pattern = re.compile(r'\d{14}')
result = re.findall(pattern, string)
if int(result[0])>20160701000000:
    print("True")

print(result)


