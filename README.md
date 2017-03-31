# pi-aircrack-batch 

This directory contains scripts for collecting data from the wifi interface in batches. 
These scripts primarily rely on aircrack and its built-in wifi parsing
capabilities. Aircrack is the easiest tool to use, but this can also be done with scapy.

## AircrackIntervals.py

Script `AircrackIntervals.py`:
* Collects data from wifi interface and dumps to CSV files at specified intervals
* New files are created at specified time intervals.
* Total number of files collected is specified. 

