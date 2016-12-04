#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 3:
    print "gentopo_bcube.py n k"
    sys.exit(1)

n= int(sys.argv[1])
k= int(sys.argv[2])
ServerNum = n**(k+1)
SwitchNumPerLevel = n**k

#f_path = "D:\\simulation_code\\tagging_algorithm_input\\topo_bcube.txt"
#out = open(f_path, "w")

for server in range(ServerNum):
	sys.stdout.write(str(server))
	for dim in range(k+1):
		base = n**dim
		orderinsubcube =server % base
		subcube = server/(base*n)
		targetswitch = ServerNum + SwitchNumPerLevel*dim + subcube*base + orderinsubcube
		sys.stdout.write(" " + str(targetswitch))
	sys.stdout.write("\n")

	
for dim in range(k+1):
	for currentswitch in range(SwitchNumPerLevel):
		sys.stdout.write(str(ServerNum + SwitchNumPerLevel*dim + currentswitch))
		base = n**dim
		orderinsubcube = currentswitch % base
		subcube = currentswitch/base
		temp = subcube*base*n + orderinsubcube
		for valueofdim in range(n):
			server = temp + valueofdim*base
			sys.stdout.write(" " + str(server))
		sys.stdout.write("\n")
	
#out.close()
