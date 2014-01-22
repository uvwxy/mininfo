#!/usr/bin/python
import os
import commands

def run(cmd):
  return commands.getstatusoutput(cmd)

def diskUsage(path):
  st = os.statvfs(path)
  free = st.f_bavail * st.f_frsize
  total = st.f_blocks * st.f_frsize
  used = (st.f_blocks - st.f_bfree) * st.f_frsize
  return total,used,free

def top(numlines=20):
  code,result = run("top -b -n1")
  return "\n".join(result.split("\n")[0:numlines])

def hostInfo():
  code,result = run("hostname")
  cod2,resul2 = run("uname -r")
  print result
  print resul2
  return str(result)+" ("+str(resul2) + ")"
