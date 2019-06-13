import gaussSolver as gs
import math
import subprocess
from time import time as epochTime
import sys


def func(x):
    x = 0.5*x + 0.5
    return math.pow(x, 3) * math.cos(math.pow(x, 2)) / (x + 1)


n = int(sys.argv[1])

start = epochTime()
aSolver = gs.CGaussSolver(func, 0, 1, n)
aSolver.exec()
print("Python n = {}: {:.20f}".format(n, aSolver.getResult()))
print("python seconds: {:.4f}ms".format((epochTime() - start) * 1000))
start = epochTime()
subprocess.call(['./main', '{}'.format(n)])
print("took {:.4f} ms".format((epochTime() - start) * 1000))

pythonTime = []
cTime = []
inputList = range(1, n + 1)
for i in inputList:
    start = epochTime()
    aSolver = gs.CGaussSolver(func, 0, 1, i)
    aSolver.exec()
    pythonTime.append((epochTime() - start) * 1000)
    print("Result of Python code (n = {}) : {:.20f}".format(i, aSolver.getResult()))
    start = epochTime()
    subprocess.call(['./main', '{}'.format(i)])
    cTime.append((epochTime() - start) * 1000)

