import tkinter as tk
from tkinter import ttk


class SimulationUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Workload Scheduler Simulation")

        # Increase window size
        self.root.geometry("900x600")

        # Big frame for CPUs
        cpu_frame = tk.LabelFrame(self.root, text="CPU Status", padx=10, pady=10)
        cpu_frame.pack(fill="x", padx=10, pady=10)

        self.cpu_labels = []
        for i in range(3):
            lbl = tk.Label(cpu_frame, text=f"CPU {i}: Ready", font=("Segoe UI", 12))
            lbl.pack(anchor="w", pady=5)
            self.cpu_labels.append(lbl)

        # Big frame for completed process list
        proc_frame = tk.LabelFrame(
            self.root, text="Completed Processes", padx=10, pady=10
        )
        proc_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Increase width & height (previously small)
        self.process_list = tk.Listbox(
            proc_frame, width=80, height=20, font=("Segoe UI", 11)
        )
        self.process_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(proc_frame)
        scrollbar.pack(side="right", fill="y")

        self.process_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.process_list.yview)

    # ----------- Update CPU Info -----------
    def update_cpu_info(self, cpus):
        for cpu in cpus:
            self.cpu_labels[cpu.id].config(
                text=f"CPU {cpu.id}: {len(cpu.queue)} process(es) | Busy Time: {cpu.busy_time}"
            )
        self.root.update()

    # ----------- Add Completed Process -----------
    def add_completed_process(self, process):
        self.process_list.insert(
            tk.END,
            f"PID {process.pid} | Arrival {process.arrival_time} | Burst {process.burst} | Finish {process.finish_time}",
        )
        self.root.update()

    # ----------- Start UI Loop -----------
    def start(self):
        self.root.mainloop()
