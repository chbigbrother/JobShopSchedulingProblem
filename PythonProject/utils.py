import numpy as np
import random
from itertools import permutations

def readFile(filePath):
    with open(filePath) as fp:
        line = fp.readline()
        nm = line.strip().split()
        machineCnt = nm[1]
        jobs = []
        machines = []
        processing_time = []
        VG = []

        for i in range(int(nm[0])):
            line = fp.readline()
            cv = list(map(int, line.split()))
            operations = []
            machine_l = []
            times = []
            j = 1
            while j < len(cv):
                # 각 op 별 machine, processing_time 할당
                k = cv[j]
                operation = []
                for kj in range(k):
                    j = j + 1
                    if (j >= len(cv)):
                        break;
                    # machine 할당
                    machine = cv[j]
                    j = j + 1
                    # processing_time 할당
                    processing_t = cv[j]
                    machine_l.append(machine)
                    processing_time.append(processing_t)
                    operation.append({'machine': machine, 'processingTime': processing_t})
                j = j + 1
                operations.append(operation)
            machines.append(machine_l)

            # VG 할당
            if (j > len(cv)):
                VG.append(int(cv[-1]))

            jobs.append(operations)
    return jobs, VG, machines, processing_time, {'machineCnt': int(machineCnt), 'jobs': jobs}
