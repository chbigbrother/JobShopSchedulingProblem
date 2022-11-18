# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import sys
from utils import readFile
from genetic.population import initial_generation
from genetic.fjspGA import calculateMakespan
from genetic.makespan import getMakespans
from genetic.fjspGA import plotChart

popSize = 400
maxGen = 200
pr = 0.005
pc = 0.8
pm = 0.1

latex_export = True
t0 = time.time()
jobs, VG, machines, processing_time, jobDicts = readFile("./cases/test_data.txt")


parameter = initial_generation(popSize, jobDicts, VG, machines) # NS MS

gen = 1

sortedPop = sorted(parameter, key=lambda cpl: calculateMakespan(cpl, jobDicts, VG))
gantt = getMakespans((sortedPop[0][0], sortedPop[0][1]), jobDicts, VG)
plotChart(gantt)