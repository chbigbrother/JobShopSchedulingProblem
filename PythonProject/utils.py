import numpy as np
import random
from itertools import permutations

def readFile(filePath):
    with open(filePath) as fp:
        line = fp.readline()
        nm = line.strip().split()
        machineCnt = nm[1]
        vg_bool = False
        if nm[2] == 'v':
            vg_bool = True

        jobs = []
        machines = []
        processing_time = []
        multi_ops = []
        VG = []
        for i in range(int(nm[0])):
            line = fp.readline()
            cv = list(map(int, line.split()))
            operations = []
            times = []
            j = 0

            # 각 op 별 machine, processing_time 할당
            # operation 개수
            k = cv[j]

            for kj in range(k):
                operation = []
                machine_l = []
                j = j + 1
                end = (cv[j] * 2) + 1
                if kj > 0:
                    operation = []
                for h in range(cv[j]):
                    j += 1
                    machine = cv[j]
                    j += 1
                    if (j >= len(cv)):
                        continue;
                    # processing_time 할당
                    processing_t = cv[j]
                    machine_l.append(machine)
                    processing_time.append(processing_t)
                    operation.append({'machine': machine, 'processingTime': processing_t})
                operations.append(operation)
                machines.append(machine_l)

            if vg_bool == True:
                # VG 할당
                vgcnt = 0
                VG_L = [[] for i in range(cv[0])]

                for v in range(cv[0]):
                    vgcnt = (-v - 1)
                    VG_L[v].append(int(cv[vgcnt]))

                VG_L.reverse()
                VG.append(VG_L)

            if len(operations) > 1:
                for o in range(len(operations)):
                    if o > 0:
                        # multi_ops.append([operations[o]])
                        jobs[i] += [operations[o]]
                    else:
                        jobs.append([operations[o]])
            else:
                jobs.append(operations)
        # jobs += multi_ops
    return jobs, VG, machines, processing_time, {'machineCnt': int(machineCnt), 'jobs': jobs}
