#!/usr/bin/env python3
from enum import Enum


class State(Enum):
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


class ScheduleInfo:
    def __init__(self):
        self.jobID
        self.jobName
        self.startTime
        self.endTime
        self.submitTime
        self.numNodes
        self.numCPUs
        self.numTasks
        self.exitCode


class Job:
    def __init__(self, jobID, jobName, startTime, endTime, submitTime, numNodes, numCPUs, numTasks, exitCode):
        super().__init__(jobID, jobName, startTime, endTime, submitTime, numNodes, numCPUs, numTasks, exitCode)
        self.dependency
