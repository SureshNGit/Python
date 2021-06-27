#!/usr/bin/env python3

import shutil
import psutil

def checkDiskUsage(disk):
    du=shutil.disk_usage(disk)
    free=(du.free/du.total)*100
    return free>20

def checkCpuUsage():
    return psutil.cpu_percent(0.1)<75

if not checkDiskUsage("/") or not checkCpuUsage():
    print("ERROR!!!!")
else:
    print("Everything is Okay!!!")
