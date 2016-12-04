#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    print "gentopo_fattree.py k"
    sys.exit(1)

k= int(sys.argv[1])
TorNum = k*k/2
LeafNum = k*k/2
SpineNum = k*k/4
ServerPerTor = k/2
SwitchNum = TorNum + LeafNum + SpineNum
ServerNum = ServerPerTor*TorNum
LinkNum = ServerNum + LeafNum*k

#f_path = "D:\\simulation_code\\tagging_algorithm_input\\topo_fattree.txt"
#out = open(f_path, "w")

#print links of ToRs
for tor in range(TorNum):
	sys.stdout.write(str(tor))
	#print links to servers
	for i in range(ServerPerTor):
		sys.stdout.write(" " + str(SwitchNum+tor*ServerPerTor+i))
	#print links to Leafs
	for i in range(k/2):
		pod = tor*2/k
		sys.stdout.write(" " + str(TorNum+pod*k/2+i))
	sys.stdout.write("\n")
	
#print links of Leafs
for leaf in range(LeafNum):
	sys.stdout.write(str(TorNum+leaf))
	#print links to ToRs
	for i in range(k/2):
		pod = leaf*2/k
		sys.stdout.write(" " + str(pod*k/2+i))
	#print links to Spines
	orderinpod = leaf%(k/2)
	firstspine = orderinpod*k/2
	lastspine = firstspine + k/2 - 1
	for spine in range(firstspine, lastspine+1):
		sys.stdout.write(" " + str(TorNum+LeafNum+spine))
	sys.stdout.write("\n")
	
#print links of Spines
for spine in range(SpineNum):
	sys.stdout.write(str(TorNum+LeafNum+spine))
	orderinpod = spine*2/k
	for pod in range(k):
		sys.stdout.write(" " + str(TorNum+pod*k/2+orderinpod))
	sys.stdout.write("\n")
	
#print links of Servers
for server in range(ServerNum-1):
	sys.stdout.write(str(SwitchNum + server))
	tor = server/ServerPerTor
	sys.stdout.write(" " + str(tor))
	sys.stdout.write("\n")
sys.stdout.write(str(SwitchNum + ServerNum-1) + " " + str(TorNum-1))

#out.close()
