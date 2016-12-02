import sys
import os

n= int(sys.argv[1])
k= int(sys.argv[2])
ServerNum = n**(k+1)
SwitchNumPerLevel = n**k

f_path = "D:\\simulation_code\\tagging_algorithm_input\\topo_bcube.txt"
out = open(f_path, "w")

for server in range(ServerNum):
	out.write(str(server))
	for dim in range(k+1):
		base = n**dim
		orderinsubcube =server % base
		subcube = server/(base*n)
		targetswitch = ServerNum + SwitchNumPerLevel*dim + subcube*base + orderinsubcube
		out.write(" " + str(targetswitch))
	out.write("\n")

	
for dim in range(k+1):
	for currentswitch in range(SwitchNumPerLevel):
		out.write(str(ServerNum + SwitchNumPerLevel*dim + currentswitch))
		base = n**dim
		orderinsubcube = currentswitch % base
		subcube = currentswitch/base
		temp = subcube*base*n + orderinsubcube
		for valueofdim in range(n):
			server = temp + valueofdim*base
			out.write(" " + str(server))
		out.write("\n")
	
out.close()