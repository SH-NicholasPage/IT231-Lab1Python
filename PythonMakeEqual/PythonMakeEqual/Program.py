#DO NOT MODIFY THIS FILE

import os
from typing import Final

from Source import *

MAX_SCORE: Final[int] = 10

try:
    dirname = os.path.dirname(__file__)
    f = open(os.path.join(dirname, '../inputs.txt'), "r")
except:
    print("Unable to open the file!")

questions = 0
questionsCorrect = 0

for line in f:
    if line == "" or line == '\n':
        continue;

    questions += 1

    intList1 = list(map(int, line.split(' ')))
    intList2 = list(map(int, f.readline().strip().split(' ')))
    expectedAnswer = int(f.readline().strip())
    studentAnswer = makeEqual(intList1, intList2);

    if expectedAnswer == studentAnswer:
        questionsCorrect += 1
        print("Output #" + str(questions) + " is correct.")
    else:
        print("Output #" + str(questions) + " is incorrect.")

print('\n' + str(questionsCorrect) + "/" + str(questions) + " correct.")
print(str(round(questionsCorrect / questions * MAX_SCORE, 1)) + "/" + str(MAX_SCORE) + " points scored.")

f.close()