

# VG 별 machine 나누기
def split_by_machine(VG, param, jobDicts):
    (n,m) = param
    job_lists = []
    current = 0
    if(len(VG) > 0):
        for v in VG:
            append_l = []
            for i in range(v):
                append_l.append(m[current])
                current += 1
            job_lists.append(append_l)
    else:
        current = 0
        for index, job in enumerate(jobDicts['jobs']):
            job_lists.append(m[current:current+len(job)])
            current += len(job)

    return job_lists

def is_free(tab, start, duration):
    for k in range(start, start+duration):
        if not tab[k]:
            return False
    return True

def find_first_proc_time(start_ctr, duration, machine_jobs):
    max_duration_list = []
    max_duration = start_ctr + duration

    if machine_jobs:
        for job in machine_jobs:
            max_duration_list.append(job[2] + job[1])

        max_duration = max(max(max_duration_list), start_ctr) + duration

    machine_used = [True] * max_duration

    for job in machine_jobs:
        start = job[2]
        long = job[1]
        for k in range(start, start + long):
            machine_used[k] = False

    for k in range(start_ctr, len(machine_used)):
        if is_free(machine_used, k, duration):
            return k


def getMakespans(cpl, jobDicts, VG):
    o = jobDicts['jobs']
    (n, m) = cpl

    cnt = 0
    ops = [[] for i in range(jobDicts['machineCnt'])]
    time_taken = [[] for i in range(jobDicts['machineCnt'])]
    m_splits = split_by_machine(VG, (n, m), jobDicts)

    outer_shell = [0] * len(m_splits)
    time_outer_shell = [0] * len(m_splits)

    for i in n:
        idx_m = m_splits[i][outer_shell[i]]
        idx_m = idx_m - 1

        if (len(VG) > 0):
            machine = [i['machine'] for i in o[i][0] if i['machine'] == idx_m + 1][0]
            proc_t = [i['processingTime'] for i in o[i][0] if i['machine'] == idx_m + 1][0]
        else:
            machine = o[i][outer_shell[i]][idx_m]['machine']
            proc_t = o[i][outer_shell[i]][idx_m]['processingTime']
        start_t = time_outer_shell[i]

        outer_shell[i] += 1
        tag = "{}-{}".format(i, outer_shell[i] + 1)
        if (len(time_taken[machine - 1]) > 0):
            time = (start_t + proc_t)
            lng = len(time_taken[machine - 1]) - 1
            time = time_taken[machine - 1][lng] + time
            time_taken[machine - 1].append(time)
            ops[machine - 1].append((tag, time_taken[machine - 1][lng], time))
        else:
            time_taken[machine - 1].append((start_t + proc_t))
            ops[machine - 1].append((tag, start_t, (start_t + proc_t)))

    # calc = calculateMakespan(ops)

    return ops


