#! /usr/bin/env python3

import sys,json

data = sys.stdin.read()

data=data.replace('\n}\n{\n', '\n},\n{\n')

data = '[\n'+data
data = data+'\n]'

print(json.loads(json.dumps(data)))
