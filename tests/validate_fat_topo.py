#!/usr/bin/python3
import json
import os
import sys

def test_bin_tree(k):
    print("Testing fat tree for k =", k)

    k_info = {}
    k_info[4] = { 'links' : 48, 'switches' : 20, 'hosts' : 16 }
    k_info[6] = { 'links' : 162, 'switches' : 45, 'hosts' : 54 }
    k_info[8] = { 'links' : 384, 'switches' : 80, 'hosts' : 128 }

    print("Topology Unit Tests")
    with open("./topology/p4app_fat.json") as f:
        print("Unit Test 1: Link Count")
        topo = json.load(f)
        assert len(topo['topology']['links']) == k_info[k]['links']
        print("Test passed")

        print("Unit Test 2: Switch Count")
        assert (len(topo['topology']['switches'])) == k_info[k]['switches']
        print("Test passed")

        print("Unit Test 3: Host Count")
        assert len(topo['topology']['hosts']) == k_info[k]['hosts']
        print("Test passed")

    print("Controller Unit Tests")
    host_ips = []
    hosts = []
    for i in range(1, k_info[k]['hosts'] + 1):
        hosts += ['h{0}'.format(i)]
        host_ips += ['10.0.0.{0}'.format(i)]

    print("Unit Test 4: Ping mesh")
    print("(might take a while)")
    c = 0
    for h in hosts:
        for ip in host_ips:
            assert ("0% packet loss" in os.popen('mx {0} ping -c 1 {1}'.format(h, ip)).read())
            c += 1
            print(int(c * 100.0 / (k_info[k]['hosts']**2)), '% complete.', end='\r', flush=True)
    
    print("")
    print("Test passed")
if __name__ == '__main__':
    k = int(sys.argv[1])
    test_bin_tree(k)
