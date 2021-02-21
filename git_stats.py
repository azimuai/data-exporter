#! /usr/bin/env python3

import sys
import json

data = sys.stdin.read()
data = [k.split('\n\n') for k in [i.strip() for i in data.split('COMMITBEGIN')] if k]
stats = {}
for i in data:
    if len(i) == 1:
        stats[i[0]] = {}
    else:
        inner_stats = []
        for stat in i[1].split('\n'):
            stat = stat.split('\t')
            inner_stats.append({'insertions':stat[0], 'deletions':stat[1],'path':stat[2]})
        stats[i[0]] = inner_stats

print(json.dumps(stats))
