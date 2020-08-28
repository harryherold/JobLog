import unittest
import json
import schedule_info
from schedule_info import *


class ScheduleInfoTest(unittest.TestCase):
    def setUp(self):
        with open('/home/jan/JobLog/example_log.json') as f:
            self.step = json.load(f)

    def test_add_step(self):
        step = schedule_info.Step(self.step.get('jobID'), self.step.get('jobName'), self.step.get('startTime'), self.step.get('endTime'), self.step.get('submitTime'), self.step.get('numNodes'), self.step.get('numCPUs'), self.step.get('numTasks'),
                                  self.step.get('exitCode'),
                                  self.step.get('nodeList'))
        self.assertEqual(schedule_info.Job.add_step(self.step, step))

    def test_job_has_steps(self):
        pass


if __name__ == '__main__':
    unittest.main()


class Job(ScheduleInfo):
    def __init__(self, jobID, jobName, startTime, endTime, submitTime, numNodes, numCPUs, numTasks, exitCode,
                 dependency):
        super().__init__(jobID, jobName, startTime, endTime, submitTime, numNodes, numCPUs, numTasks, exitCode)
        self.dependency = dependency
        self.steps = []
        self.step = Step(jobID, jobName, startTime, endTime, submitTime, numNodes, numCPUs, numTasks, exitCode,
                         nodeList)
