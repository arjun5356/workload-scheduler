# src/scheduler.py

class Scheduler:
    """
    Basic dynamic load balancer.
    Assigns processes to whichever CPU currently has the lowest total load.
    """

    def __init__(self, cpus):
        # cpus = list of CPU objects
        self.cpus = cpus

    def choose_cpu(self):
        """
        Return the CPU object with the least total load.
        """
        return min(self.cpus, key=lambda cpu: cpu.total_load())

    def assign(self, process):
        """
        Assign the given process to the least-loaded CPU.
        """
        cpu = self.choose_cpu()
        cpu.add_process(process)
        return cpu.id

    def rebalance(self, threshold=5):
        """
        Migrate processes from overloaded CPUs to underloaded ones.
        threshold = max difference allowed between CPU loads.
        """
        loads = [cpu.total_load() for cpu in self.cpus]
        max_load = max(loads)
        min_load = min(loads)

        # Only rebalance if difference is too big
        if max_load - min_load < threshold:
            return

        # Find the overloaded and underloaded CPUs
        overloaded = [cpu for cpu in self.cpus if cpu.total_load() == max_load]
        underloaded = [cpu for cpu in self.cpus if cpu.total_load() == min_load]

        # Take one process from overloaded CPU and give it to an underloaded CPU
        for high in overloaded:
            migrating = high.migrate_out(count=1)
            if not migrating:
                continue
            for proc in migrating:
                low = underloaded[0]
                low.add_process(proc)


