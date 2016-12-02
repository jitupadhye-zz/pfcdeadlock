import sys
import os
from itertools import permutations

n= int(sys.argv[1])
k= int(sys.argv[2])
ServerNum = n**(k+1)
SwitchNumPerLevel = n**k

f_path = "D:\\simulation_code\\tagging_algorithm_input\\route_bcube.txt"
out = open(f_path, "w")

for server1 in range(ServerNum):
	for server2 in range(ServerNum):
		if server1 != server2:
			for dimorder in permutations(list(range(k+1)), k+1):
				#out.write("\n")
				#out.write(str(server1)+" --> " + str(server2) + " via " + str(dimorder) + "\n")
				out.write(str(server1))
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
						
						out.write(" " + str(intermediaswitch) + " " + str(nexthopserver))
						currenthopserver = nexthopserver
						
					
				out.write("\n")

out.close()
