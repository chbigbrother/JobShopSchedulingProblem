#!/usr/bin/env python
from .makespan import getMakespans
import matplotlib.pyplot as plt
import random
import datetime

def calculateMakespan(cpl, jobDicts, VG, machines):
    times_taken = getMakespans(cpl, jobDicts, VG, machines)

    max_per_machine = []
    for machine in times_taken:
        max_d = 0
        for job in machine:
            end = job[2]
            if end > max_d:
                max_d = end
        max_per_machine.append(max_d)
    print(max(max_per_machine))
    return max(max_per_machine)

def selection(population, parameter, VG, machines):
    keptPopSize = int(0.005 * len(population))
    sortedPop = sorted(population, key=lambda cpl: calculateMakespan(cpl, parameter, VG, machines))

    return sortedPop[:keptPopSize]

def plotChart(gantt):
    colorbox = ['yellow', 'whitesmoke', 'lightyellow',
                'khaki', 'silver', 'pink', 'lightgreen', 'orange', 'grey', '#8ca8df', 'brown']

    for i in range(100):
        colorArr = ['1', '2', '3', '4', '5', '6', '7',
                    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        colorbox.append("#" + color)

    zzl = plt.figure(figsize=(12, 4))

    mcnt = 0
    for i in gantt:
        for j in i:
            mText = mcnt + 1.5
            mPoint1 = j[1]
            mPoint2 = j[2]
            Word = j[0]
            x1 = mPoint1
            y1 = mText - 0.8
            x2 = mPoint2
            y2 = mText - 0.8
            x3 = mPoint2
            y3 = mText
            x4 = mPoint1
            y4 = mText

            color_per_job = int(j[0][:j[0].find('-')])
            plt.fill([x1, x2, x3, x4], [y1, y2, y3, y4],
                     color=colorbox[color_per_job])
            plt.text(0.5 * mPoint1 + 0.5 * mPoint2 - 3, mText - 0.5, Word)

        mcnt += 1

    plt.xlabel('Time')
    plt.ylabel('Machine')
    plt.tight_layout()
    plt.show()
