from src.cpu import CPU
from src.scheduler import Scheduler
from src.simulation import Simulation
from src.ui import SimulationUI
import time


def main():
    # Initialize UI
    ui = SimulationUI()

    # Setup simulation components
    cpus = [CPU(cpu_id=i) for i in range(3)]
    scheduler = Scheduler(cpus)
    sim = Simulation(cpus, scheduler, duration=50)

    print("=== Workload Scheduler Simulation Started ===\n")

    # Run simulation step-by-step
    for _ in range(50):
        sim.tick()
        # # ---------- TERMINAL PRINTING ----------
        # print(f"\n--- Time Step: {sim.time} ---")

        # # Print CPU queues & workload
        # for cpu in cpus:
        #     print(
        #         f"CPU {cpu.id}: Queue = {[p.pid for p in cpu.queue]}, "
        #         f"Current Load = {cpu.total_load()}, Busy Time = {cpu.busy_time}"
        #     )

        # # Print completed processes for this tick
        # if sim.completed:
        #     print("\nCompleted this tick:")
        #     for p in sim.completed:
        #         print(
        #             f"PID {p.pid} | Arrival {p.arrival_time} | "
        #             f"Burst {p.burst} | Finished at {p.finish_time}"
        #         )
        # else:
        #     print("\nNo processes completed this tick.")

        # ---------- UI UPDATES ----------
        ui.update_cpu_info(cpus)
        for p in sim.completed:
            ui.add_completed_process(p)

        # Clear completed list after UI + terminal log
        sim.completed.clear()

        # Slow down for visibility
        # time.sleep(0.2)

    print("\n=== Simulation Completed ===")
    ui.start()


if __name__ == "__main__":
    main()
