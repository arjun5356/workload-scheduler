# src/cpu.py
from typing import List, Optional
from src.process import Process


class CPU:
    """
    Simple virtual CPU that executes processes in FIFO order from its queue.
    The class tracks the queue and provides ticking/updating behavior.
    """
    def __init__(self, cpu_id: int):
        self.id = cpu_id
        self.queue: List[Process] = []  # processes waiting or running, front is currently running
        self.busy_time = 0  # total time CPU spent doing work (for utilization)

    def total_load(self) -> int:
        """
        Return the total remaining CPU time queued on this CPU.
        Used by the scheduler to pick least-loaded CPU.
        """
        return sum(p.remaining for p in self.queue)

    def add_process(self, process: Process):
        """
        Append process to this CPU's queue; mark assigned CPU id.
        """
        process.assigned_cpu = self.id
        self.queue.append(process)

    def tick(self, current_time: int, time_slice: int = 1) -> List[Process]:
        """
        Advance CPU by `time_slice` units.
        - Runs the first process in the queue (if any).
        - Updates process start_time if it's the first time it runs.
        - Returns list of finished processes during this tick (usually 0 or 1).
        """
        finished = []
        if not self.queue:
            return finished

        proc = self.queue[0]
        # set start_time lazily
        if proc.start_time is None:
            proc.start_time = current_time

        # run process
        proc.run_for(time_slice)
        self.busy_time += time_slice

        if proc.is_finished():
            proc.finish_time = current_time + time_slice
            finished.append(proc)
            # pop finished process
            self.queue.pop(0)
        return finished

    def migrate_out(self, count: int = 1) -> List[Process]:
        """
        Remove up to `count` processes from the back (or could pick others) to migrate.
        This method is useful for rebalancing: take tasks that haven't started or are queued.
        We choose to migrate from the end to avoid removing currently running process.
        """
        migrating = []
        for _ in range(min(count, len(self.queue))):
            # don't remove the running process at index 0
            idx = len(self.queue) - 1
            if idx <= 0:
                break
            migrating.append(self.queue.pop(idx))
        return migrating
