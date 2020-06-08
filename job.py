#!/usr/bin/env python3
import enum
import sys


class State(enum.Enum):
    BOOT_FAIL = 1
    CANCELLED = 2
    COMPLETED = 3
    CONFIGURING = 4
    COMPLETING = 5
    DEADLINE = 6
    FAILED = 7
    NODE_FAIL = 8
    OUT_OF_MEMORY = 9
    PENDING = 10
    PREEMPTED = 11
    RUNNING = 12
    RESV_DEL_HOLD = 13
    REQUEUE_FED = 14
    REQUEUE_HOLD = 15
    REQUEUED = 16
    RESIZING = 17
    REVOKED = 18
    SIGNALING = 19
    SPECIAL_EXIT = 20
    STAGE_OUT = 21
    STOPPED = 22
    SUSPENDED = 23
    TIMEOUT = 24


class Job:
    def __init__(self, jobid, jobname, starttime, endtime, submittime, numnodes, numcpus, numtasks, exitcode,
                 dependency):
        self.jobdesc = -1
        self._stepliste = []

        self._jobid = jobid
        self._jobname = jobname
        self._starttime = starttime
        self._endtime = endtime
        self._submittime = submittime
        self._numnodes = numnodes
        self._numcpus = numcpus
        self._numtasks = numtasks
        self._exitcode = exitcode

        self._dependency = dependency




    class Step():
        def __init__(self, jobid, jobname, starttime, endtime, submittime, numnodes, numcpus, numtasks, exitcode,
                     nodelist, state):
            self._jobid = jobid
            self._jobname = jobname
            self._starttime = starttime
            self._endtime = endtime
            self._submittime = submittime
            self._numnodes = numnodes
            self._numcpus = numcpus
            self._numtasks = numtasks
            self._exitcode = exitcode
            self._nodelist = nodelist
            self._state = state


    def add_step(self, jobid, jobname, starttime, endtime, submittime, numnodes, numcpus, numtasks, exitcode,
                     nodelist, state):
        x = self.Step(jobid, jobname, starttime, endtime, submittime, numnodes, numcpus, numtasks, exitcode,
                     nodelist, state)
        self._stepliste.append(x)

    def read_step(self):
        return self._stepliste
