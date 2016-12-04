#!/usr/bin/env python

import sys
import os
from random import randint

if len(sys.argv) < 4:
    print "gentopo_jellyfish.py switch_num switch_degree switch_degree_to_switch"
    sys.exit(1)

N= int(sys.argv[1])
k= int(sys.argv[2])
r= int(sys.argv[3])
serverperswitch = k-r

ServerNum = N*serverperswitch
degree = [0]*N

edgehashtable = [[0 for x in range(N)] for y in range(N)]

#f_path = os.getcwd()+"/topo_jellyfish.txt"
#out = open(f_path, "w")

#create a ring to ensure the network is connected
for switch in range(N):
    connectedswitch = (switch+1) % N
    edgehashtable[switch][connectedswitch] = 1
    edgehashtable[connectedswitch][switch] = 1
    degree[switch] += 1
    degree[connectedswitch] += 1

#create r random edges between switches
for switch in range(N):
    for round in range(r-degree[switch]):
        connectedswitch = randint(0,N-1)
        trycount = 0
        found = 1
        while connectedswitch == switch or edgehashtable[switch][connectedswitch] == 1 or degree[connectedswitch]>= r :
            trycount += 1
            if trycount == N:
                found = 0
                break
            connectedswitch = (connectedswitch+1) % N
        if found == 1:
                edgehashtable[switch][connectedswitch] = 1
                edgehashtable[connectedswitch][switch] = 1
                degree[switch] += 1
                degree[connectedswitch] += 1


for switch in range(N):
    sys.stdout.write(" " + str(switch))
    #print connected servers
    for server in range(switch*serverperswitch, (switch+1)*serverperswitch):
        sys.stdout.write(" " + str(N+server))
    
    #print connected switches
    for connectedswitch in range(N):
        if edgehashtable[switch][connectedswitch] == 1:
            sys.stdout.write(" " + str(connectedswitch))
    sys.stdout.write("\n")

for server in range(ServerNum):
    sys.stdout.write(" " + str(N + server))
    switch = server/(serverperswitch)
    sys.stdout.write(" " + str(switch) + "\n")

#out.close()











