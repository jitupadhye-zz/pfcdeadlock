#!/usr/bin/env python

import sys
import os
from itertools import permutations

if len(sys.argv) < 3:
    print "genroute_bcube.py n k"
    sys.exit(1)

n= int(sys.argv[1])
k= int(sys.argv[2])
ServerNum = n**(k+1)
SwitchNumPerLevel = n**k

#f_path = "D:\\simulation_code\\tagging_algorithm_input\\route_bcube.txt"
#out = open(f_path, "w")

for server1 in range(ServerNum):
	for server2 in range(ServerNum):
		if server1 != server2:
			for dimorder in permutations(list(range(k+1)), k+1):
				
				sys.stdout.write(str(server1))
				currenthopserver = server1
				for dim in dimorder:
					base = n**dim
					ceilingvalue1 = currenthopserver/base
					ceilingvalue2 = server2/base
					valueofdim1 = ceilingvalue1 % n
					valueofdim2 = ceilingvalue2 % n
					if valueofdim1 != valueofdim2:
						nexthopserver = currenthopserver + (valueofdim2 - valueofdim1)*base
						
						orderinsubcube =currenthopserver % base
						subcube = currenthopserver/(base*n)
						intermediaswitch = ServerNum + SwitchNumPerLevel*dim + subcube*base + orderinsubcube
						
						sys.stdout.write(" " + str(intermediaswitch) + " " + str(nexthopserver))
						currenthopserver = nexthopserver
						
					
				sys.stdout.write("\n")

#out.close()
