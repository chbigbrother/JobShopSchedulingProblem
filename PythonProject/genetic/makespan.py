from collections import Counter

def VG_transform(VG):
    VG_t = []
    for i in range(len(VG)):
        cnt = 0
        inner = []
        for j in range(len(VG[i])):
            inner += [cnt for k in range(VG[i][j][0])]
            cnt += 1
        VG_t.append(inner)
    return VG_t

# VG 별 machine 나누기
def split_by_machine(VG, param, jobDicts):
    (n, m) = param
    job_lists = []
    if (len(VG) > 0):
        cnt = 0
        later_list = []
        for i in range(len(VG)):
            for j in range(len(VG[i])):
                inner = []
                later = []
                h = 0
                for k in range(VG[i][j][0]):
                    if j > 0:
                        later.append(m[cnt])
                        h += 1
                    else:
                        inner.append(m[cnt])
                    cnt += 1

                if len(inner) > 0:
                    job_lists.append(inner)
                if len(later) > 0:
                    job_lists[i] += later
        job_lists += later_list
    else:
        current = 0
        for index, job in enumerate(jobDicts['jobs']):
            job_lists.append(m[current:current + len(job)])
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
            max_duration_list.append(job[3] + job[1])

        max_duration = max(max(max_duration_list), start_ctr) + duration

    machine_used = [True] * max_duration

    for job in machine_jobs:
        start = job[3]
        long = job[1]
        for k in range(start, start + long):
            machine_used[k] = False

    for k in range(start_ctr, len(machine_used)):
        if is_free(machine_used, k, duration):
            return k


def getMakespans(cpl, jobDicts, VG, machines):
    o = jobDicts['jobs']
    (n, m) = cpl
    max_machine = 1
    for i in machines:
        if max(i) > max_machine:
            max_machine = max(i)

    # 작업 별 사용하는 machine 분류
    m_splits = split_by_machine(VG, (n, m), jobDicts)
    # 각 작업 순서 기록
    outer_shell = [0] * len(m_splits)
    # 각 작업 별 시작 시간 기록
    str_time_task = [0] * len(m_splits)
    # 각 작업 별 종료 시간 기록
    end_time_task = [0] * len(m_splits)
    # 각 기계별 작업의 processing time 기록
    ops = [[] for i in range(max_machine)]

    vg_t = VG_transform(VG)
    vt = [0] * len(m_splits)
    for i in n:
        idx_m = m_splits[i][outer_shell[i]]
        # machine과 processing time 할당
        if (len(VG) > 0):
            machine = [o[i][outer_shell[i]][k]['machine'] for k in range(len(o[i][outer_shell[i]])) if
                       o[i][outer_shell[i]][k]['machine'] == idx_m][0]
            proc_t = [o[i][outer_shell[i]][k]['processingTime'] for k in range(len(o[i][outer_shell[i]])) if
                      o[i][outer_shell[i]][k]['machine'] == idx_m][0]
        else:
            machine = o[i][outer_shell[i]][idx_m]['machine']
            proc_t = o[i][outer_shell[i]][idx_m]['processingTime']

        start_t = str_time_task[i]

        start = find_first_proc_time(start_t, proc_t, ops[machine - 1])
        tag = "{}-{}".format(i + 1, vg_t[i][outer_shell[i]] + 1)

        counter = Counter(vg_t[i])

        if (len(ops[machine - 1]) > 0):
            if (vt[i] != vg_t[i][outer_shell[i]]):
                if counter[vg_t[i][outer_shell[i]]] - 1 == 0:
                    str_time_task[i] = (start + proc_t)
                else:
                    str_time_task[i] = start_t  # (start + proc_t)
                vt[i] = vg_t[i][outer_shell[i]]
            else:
                if (counter[vg_t[i][outer_shell[i]]] - 1) == outer_shell[i]:
                    str_time_task[i] = (start + proc_t)
                else:
                    str_time_task[i] = start_t  # (start + proc_t)
        else:
            if (end_time_task[i]) > (start + proc_t):
                str_time_task[i] = end_time_task[i]
            else:
                str_time_task[i] = start_t  # (start + proc_t)
            if vg_t[i][outer_shell[i]] == 0:
                start = 0

        if end_time_task[i] <= (start + proc_t):
            end_time_task[i] = (start + proc_t)

        ops[machine - 1].append((tag, proc_t, start_t, start))

        outer_shell[i] += 1

    data = []

    for idx, machine in enumerate(ops):
        operations = []
        for operation in machine:
            operations.append((operation[0], operation[3], operation[3] + operation[1]))
        data.append(operations)

    return data


