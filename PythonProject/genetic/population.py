import random

def generateN(jobDicts, VG):
    N = []
    job_n = 0
    if (len(VG) > 0):    
        for v in VG:
            for i in range(v):
                N.append(job_n)
            job_n += 1

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
    if(len(VG) > 0):
        cnt = 0
        for v in VG:
            for i in range(v):
                random.shuffle(machines[cnt])
                M.append(machines[cnt][i])
            cnt += 1
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