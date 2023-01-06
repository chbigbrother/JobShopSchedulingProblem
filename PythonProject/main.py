# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import sys
from utils import readFile
from genetic.population import initial_generation
from genetic.fjspGA import calculateMakespan, plotChart, selection
from genetic.makespan import getMakespans

popSize = 400
maxGen = 200
pr = 0.005
pc = 0.8
pm = 0.1

latex_export = True
t0 = time.time()
jobs, VG, machines, processing_time, jobDicts = readFile("./cases/test_data.txt")
parameter = jobDicts

population = initial_generation(popSize, jobDicts, VG, machines) # NS MS
print(population)
# selection(population, parameter, VG, machines)


gen = 1

# makespan 결과 값을 기준으로 오름차순 정렬
sortedPop = sorted(population, key=lambda cpl: calculateMakespan(cpl, jobDicts, VG, machines))
gantt = getMakespans((sortedPop[0][0], sortedPop[0][1]), jobDicts, VG, machines)
plotChart(gantt)