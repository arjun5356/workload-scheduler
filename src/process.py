# src/process.py
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Process:
    """
    A minimal, clear representation of a process / task in the simulation.
    - pid: unique integer id
    - arrival_time: time (int) when the process arrives to the system
    - burst: total CPU time required
    - remaining: remaining CPU time (counts down)
    - start_time: when it first got CPU (None until it starts)
    - finish_time: when it completed (None until finished)
    - assigned_cpu: (optional) the id of CPU it's assigned to
    """
    pid: int
    arrival_time: int
    burst: int
    remaining: int = field(init=False)
    start_time: Optional[int] = None
    finish_time: Optional[int] = None
    assigned_cpu: Optional[int] = None

    def __post_init__(self):
        # initialize remaining to burst
        self.remaining = int(self.burst)

    def is_finished(self) -> bool:
        return self.remaining <= 0

    def run_for(self, ticks: int = 1):
        """
        Simulate running this process for `ticks` time units.
        Decrements remaining time but doesn't go below zero.
        """
        self.remaining = max(0, self.remaining - ticks)

    def wait_time(self, current_time: int) -> int:
        """
        Simple calculation: how long the process waited before starting.
        If not started yet, waiting is current_time - arrival_time.
        If already started, waiting is start_time - arrival_time.
        """
        if self.start_time is None:
            return current_time - self.arrival_time
        return self.start_time - self.arrival_time
