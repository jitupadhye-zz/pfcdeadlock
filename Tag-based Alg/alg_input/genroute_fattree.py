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

f_path = "D:\\simulation_code\\tagging_algorithm_input\\route_fattree.txt"
out = open(f_path, "w")

#print intro pod paths
for pod in range(k):
	firstserver = SwitchNum + pod*k*k/4
	lastserver = firstserver + k*k/4
	firstleaf = TorNum + pod*k/2
	lastleaf = firstleaf + k/2
	for server1 in range(firstserver, lastserver):
		for server2 in range(firstserver, lastserver):
			if server1 != server2:
				tor1 = (server1-SwitchNum)*2/k
				tor2 = (server2-SwitchNum)*2/k
				if tor1 == tor2:
					out.write(str(server1) + " " + str(tor1) + " " + str(server2))
					out.write("\n")
				else:
					for leaf in range (firstleaf, lastleaf):
						out.write(str(server1) + " " + str(tor1) + " " + str(leaf) + " " + str(tor2) + " " + str(server2))
						out.write("\n")


						
#print inter pod paths
for pod1 in range(k):
	for pod2 in range(k):
		if pod1 != pod2:	
			firstserver1 = SwitchNum + pod1*k*k/4
			lastserver1 = firstserver1 + k*k/4
			firstleaf1 = TorNum + pod1*k/2
			lastleaf1 = firstleaf1 + k/2
			
			firstserver2 = SwitchNum + pod2*k*k/4
			lastserver2 = firstserver2 + k*k/4
			
			for server1 in range(firstserver1, lastserver1):
				for server2 in range(firstserver2, lastserver2):
					tor1 = (server1-SwitchNum)*2/k
					tor2 = (server2-SwitchNum)*2/k
					for leaf1 in range(firstleaf1, lastleaf1):
						firstspine = TorNum+LeafNum + (leaf1-firstleaf1)*k/2
						lastspine = firstspine + k/2
						for spine in range(firstspine, lastspine):
							leaf2 = TorNum + pod2*k/2 + leaf1 - firstleaf1
							out.write(str(server1) + " " + str(tor1) + " " + str(leaf1) + " " + str(spine) + " " + str(leaf2) + " " + str(tor2) + " " + str(server2))
							out.write("\n")
		