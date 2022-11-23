import random
from itertools import permutations

def perm_table(VG, machines):
    VG_tables = []
    k = 0
    for i in machines:
        cnt = []
        per_list = []
        for j in i:
            cnt.append(j)
        for j in permutations(i, VG[k]):
            if(len(i) == VG[k]) or VG[k]==1:
                continue;
            per_list.append(list(j))
        if(len(i) == VG[k]) or VG[k]==1:
            per_list[:0] = cnt
        VG_tables.append(per_list)
        k += 1
    return VG_tables

def generateN(jobDicts, VG):
    N = []

    if (len(VG) > 0):
        for v in range(len(jobDicts['jobs'])):
            N.append(v)
        random.shuffle(N)
    else:
        jobs = jobDicts['jobs']
        i = 0
        for job in jobs:
            for op in job:
                N.append(i)
            i = i+1

        random.shuffle(N)
    return N

def generateM(jobDicts, VG, machines):
    M = []
    p_table = perm_table(VG, machines)

    if (len(VG) > 0):
        cnt = 0
        for v in range(len(VG)):
            if (len(p_table[v]) > VG[v]):
                random.shuffle(p_table[v])
                if (type(p_table[v][0]) != int):
                    M = M + p_table[v][0]
                else:
                    M.append(p_table[v][0])
            else:
                if (type(p_table[v]) != int):
                    M = M + p_table[v]
                else:
                    M.append(p_table[v])
    else:
        jobs = jobDicts['jobs']
        cnt = 0
        for job in jobs:
            for op in job:
                cnt += 1
                randomMachine = random.randint(0, len(op)-1)
                M.append(randomMachine)
    return M

def initial_generation(popSize, jobDicts, VG, machines):
    pop_gen = []
    for i in range(popSize):
        NS = generateN(jobDicts, VG)
        MS = generateM(jobDicts, VG, machines)
        pop_gen.append((NS, MS))

    return pop_gen