import random
from itertools import permutations

def re_arrange_jobdict(VG, jobDicts):
    for i in range(len(VG)):
        cnt = 0
        for j in VG[i]:
            if j[0] > 1:
                for k in range(j[0]):
                    if k > 0:
                        jobDicts['jobs'][i].insert(cnt, jobDicts['jobs'][i][cnt])
                        cnt += 1
            cnt += 1
    return jobDicts

def perm_tables(VG, machines):
    VG_tables = []
    perm = []
    cnt = 0
    for j in VG:
        if len(j) > 1:
            for k in j:
                perm.append(k[0])
        else:
            perm.append(j[0][0])

    for i in perm:
        per_list = []
        for k in permutations(machines[cnt], i):
            if (len(machines[cnt]) == i) or i == 1:
                continue;
            per_list.append(list(k))
        if (len(machines[cnt]) == i) or i == 1:
            per_list[:0] = machines[cnt]
        VG_tables.append(per_list)
        cnt += 1
    return VG_tables

def generateN(jobDicts, VG):
    if len(VG) > 0:
        N = []
        jobs = jobDicts['jobs']
        n_dict = {}
        os = []
        i = 0
        for v in VG:
            p = len(VG) - 1
            cnt = 0
            for j in v:
                NN = []
                cnt += 1
                if cnt > 1:
                    [NN.append(i) for k in range(j[0])]
                    try:
                        n_dict[cnt] += NN
                    except:
                        n_dict[cnt] = NN
                    random.shuffle(n_dict[cnt])
                else:
                    [N.append(i) for k in range(j[0])]
                    n_dict[cnt] = N
            i += 1
        random.shuffle(N)
        for i in n_dict.values():
            os += i
        N = os
    else:
        N = []

        jobs = jobDicts['jobs']
        i = 0
        for job in jobs:
            for op in job:
                N.append(i)
            i = i + 1
        random.shuffle(N)
    return N

def generateM(jobDicts, VG, machines):
    M = []
    perm_table = perm_tables(VG, machines)
    if (len(VG) > 0):
        cnt = 0
        for v in VG:
            j = 0
            for k in v:
                if j > 0:
                    # M.append([])
                    cnt += 1
                if (len(perm_table[cnt]) > v[j][0]):
                    random.shuffle(perm_table[cnt])
                    if (type(perm_table[cnt][0]) != int):
                        M = M + perm_table[cnt][0]
                    else:
                        M.append(perm_table[cnt][0])
                else:
                    if (type(perm_table[cnt]) != int):
                        M = M + perm_table[cnt]
                    else:
                        M.append(perm_table[cnt])
                j += 1
            cnt += 1
    else:
        jobs = jobDicts['jobs']
        cnt = 0
        for job in jobs:
            for op in job:
                cnt += 1
                randomMachine = random.randint(0, len(op) - 1)
                M.append(randomMachine)
    return M

def initial_generation(popSize, jobDicts, VG, machines):
    pop_gen = []
    jobDicts = re_arrange_jobdict(VG, jobDicts)
    for i in range(popSize):
        NS = generateN(jobDicts, VG)
        MS = generateM(jobDicts, VG, machines)
        pop_gen.append((NS, MS))

    return pop_gen