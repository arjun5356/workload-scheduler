from src.cpu import CPU
from src.scheduler import Scheduler
from src.simulation import Simulation

def main():
    # Create 3 CPUs
    cpus = [CPU(cpu_id=i) for i in range(3)]

    # Create scheduler
    scheduler = Scheduler(cpus)

    # Create simulation (50 time units)
    sim = Simulation(cpus, scheduler, duration=50)

    # Run simulation
    completed = sim.run()

    # Print summary
    print("\n=== SIMULATION COMPLETE ===")
    print(f"Total processes completed: {len(completed)}")

    for i, cpu in enumerate(cpus):
        print(f"CPU {i} busy time: {cpu.busy_time}")

    print("\nCompleted Processes:")
    for p in completed:  # print first 10 only
        print(f"PID {p.pid} | Arrival {p.arrival_time} | Burst {p.burst} | Finished at {p.finish_time}")

if __name__ == "__main__":
    main()
