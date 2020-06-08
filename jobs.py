

def job_exists(jobid: int):
    cmd = "scontrol show jobid {}".format(jobid)
    with Popen(cmd, shell=True, stdout=PIPE) as proc:
        proc.wait()
        return proc.returncode == 0

def job_has_steps(jobid: int) -> bool:
    cmd = "sacct -j {} --format=JobID --nohead".format(jobid)
    regex = r"[0-9]+\.[0-9]+"
    with Popen(cmd, shell=True, stdout=PIPE) as proc:
        proc.wait()
        data = proc.stdout.read().decode("utf-8")
        return re.search(regex, data) != None

def job_active(jobid: int) -> bool:
    cmd = "sacct -j {} --format=State --nohead".format(jobid)
    with Popen(cmd, shell=True, stdout=PIPE) as proc:
        proc.wait()
        state = proc.stdout.read().decode("utf-8").rstrip()
        return state in ACTIVE_STATES

def job_deps(jobid: int) -> str:
    cmd = "scontrol show jobid -dd {}".format(jobid)
    with Popen(cmd, shell=True, stdout=PIPE) as proc:
        for line in proc.stdout:
            l = line.decode("utf-8").rstrip()
            fields = [opts.split('=') for opts in l.split(' ') if opts != '']
            for field in fields:
                if field[0] == "Dependency":
                    return field[1]

def job_info(jobid: int) -> dict:
    job_info = dict()
    job_info["steps"] = dict()
    cmd = "sacct -n -P -j {} --format={}".format(jobid, ','.join(JOB_STEPS_FIELDS))
    with Popen(cmd, shell=True, stdout=PIPE) as proc:
        for line in proc.stdout:
            fields = line.decode("utf-8").rstrip().split('|')
            # Add job info
            if fields[0].isdecimal():
                for k, v in zip(JOB_STEPS_FIELDS, fields):
                    if (k == 'Start' or k == 'End' or k == 'Submit'):
                        try:
                            job_info[k] = convert_timestamp(v)
                        except ValueError:
                            job_info[k] = None
                    else:
                        job_info[k] = v
            # Add job step info
            if contains_step_id(fields[0]):
                job_info["steps"][fields[0]] = dict()
                for k, v in zip(JOB_STEPS_FIELDS[1:], fields[1:]):
                    if k == "Submit":
                        continue
                    if k == 'Start' or k == 'End':
                        v = convert_timestamp(v)
                    job_info["steps"][fields[0]][k] = v
    # Create Queue Time
    if 'Start' in job_info and 'Submit' in job_info:
        start_time = output_datetime(job_info['Start'])
        submit_time = output_datetime(job_info['Submit'])
        job_info['QueueTime'] = str(start_time - submit_time)

    # Add steps if there no one
    if not job_info["steps"]:
        virt_step = {k : job_info[k] for k in JOB_STEPS_FIELDS[1:]}
        if not virt_step['End']:
            e = datetime.strptime(job_info['Elapsed'], '%H:%M:%S')
            dt = timedelta(seconds=e.second, minutes=e.minute, hours=e.hour)
            start = output_datetime(virt_step['Start'])
            virt_step['End'] = str(start + dt)
            job_info['End'] = virt_step['End']
        # TODO elif not job_info['End']: update job_info['End'] by counting elapsed times over all steps
        job_info["steps"][job_info['JobID']] = virt_step

    return job_info
