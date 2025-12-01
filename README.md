
Workload Scheduler Simulation

This project simulates how an operating system distributes processes across multiple processors.
The goal is to balance the load so no single CPU gets overloaded.

What this project does

Creates multiple virtual CPUs

Generates random processes

Assigns each process to the CPU with the least load

Runs a time-based simulation

Shows how many processes were completed and how busy each CPU was

Files
main.py                 → runs the simulation
src/process.py          → process structure
src/cpu.py              → CPU model
src/scheduler.py        → scheduling logic
src/simulation.py       → simulation loop

How to run
python main.py

Output

You will see:

total processes completed

CPU busy time

basic info about completed processes
