import sys
import os

k= int(sys.argv[1])
TorNum = k*k/2
LeafNum = k*k/2
SpineNum = k*k/4
ServerPerTor = k/2
SwitchNum = TorNum + LeafNum + SpineNum
ServerNum = ServerPerTor*TorNum
LinkNum = ServerNum + LeafNum*k

f_path = "D:\\simulation_code\\tagging_algorithm_input\\topo_fattree.txt"
out = open(f_path, "w")

#print links of ToRs
for tor in range(TorNum):
	out.write(str(tor))
	#print links to servers
	for i in range(ServerPerTor):
		out.write(" " + str(SwitchNum+tor*ServerPerTor+i))
	#print links to Leafs
	for i in range(k/2):
		pod = tor*2/k
		out.write(" " + str(TorNum+pod*k/2+i))
	out.write("\n")
	
#print links of Leafs
for leaf in range(LeafNum):
	out.write(str(TorNum+leaf))
	#print links to ToRs
	for i in range(k/2):
		pod = leaf*2/k
		out.write(" " + str(pod*k/2+i))
	#print links to Spines
	orderinpod = leaf%(k/2)
	firstspine = orderinpod*k/2
	lastspine = firstspine + k/2 - 1
	for spine in range(firstspine, lastspine+1):
		out.write(" " + str(TorNum+LeafNum+spine))
	out.write("\n")
	
#print links of Spines
for spine in range(SpineNum):
	out.write(str(TorNum+LeafNum+spine))
	orderinpod = spine*2/k
	for pod in range(k):
		out.write(" " + str(TorNum+pod*k/2+orderinpod))
	out.write("\n")
	
#print links of Servers
for server in range(ServerNum-1):
	out.write(str(SwitchNum + server))
	tor = server/ServerPerTor
	out.write(" " + str(tor))
	out.write("\n")
out.write(str(SwitchNum + ServerNum-1) + " " + str(TorNum-1))

out.close()