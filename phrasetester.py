#!/usr/bin/env python3

import os
import sys
import random

class Phrase:
  def __init__(self, line):
    tokens = line.split(',')
    self.source_language = tokens[0]
    self.target_language = tokens[1]
    self.source = tokens[2]
    self.target = tokens[3]

words = [Phrase(x.strip()) for x in open('phrasebook.csv').readlines()]

print('DB contains: %u words' % len(words))

while 1:
  random.shuffle(words)

  candidates = words[:3]
  item = candidates[0]
  random.shuffle(candidates)

  print(item.source)

  for i, c in enumerate(candidates):
    print('%u:%s ' % (i + 1, c.target), end = '')

  print()

  line = sys.stdin.readline().strip()

  if line == '':
    break

  if len(line) == 1 and line[0].isdigit():
    line = candidates[int(line) - 1].target

  if line == item.target:
    print('SUCCESS')
  else:
    print('WRONG (right answer: %s)' % item.target)

  print()
  item = random.choice(words)
