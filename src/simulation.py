# src/simulation.py

import random
from src.process import Process

class Simulation:
    """
    Runs time-stepped simulation of processes arriving,
    CPU executing, scheduler balancing.
    """

    def __init__(self, cpus, scheduler, duration=50):
        self.cpus = cpus
        self.scheduler = scheduler
        self.time = 0
        self.duration = duration
        self.next_pid = 1
        self.completed = []

    def generate_process(self):
        """
        Randomly generate processes every few time steps.
        40% chance of process arrival.
        """
        if random.random() < 0.4:
            burst = random.randint(2, 10)
            p = Process(
                pid=self.next_pid,
                arrival_time=self.time,
                burst=burst
            )
            self.next_pid += 1
            return p
        return None

    def tick(self):
        """
        One unit of simulation time.
        - generate a process
        - scheduler assigns it
        - CPUs run
        - collect completed tasks
        - rebalance if needed
        """
        # 1. maybe new process
        p = self.generate_process()
        if p:
            self.scheduler.assign(p)

        # 2. CPU execution
        for cpu in self.cpus:
            finished = cpu.tick(self.time)
            self.completed.extend(finished)

        # 3. rebalance occasionally
        if self.time % 5 == 0:
            self.scheduler.rebalance()

        self.time += 1

    def run(self):
        """
        Run the entire simulation.
        """
        for _ in range(self.duration):
            self.tick()

        return self.completed
