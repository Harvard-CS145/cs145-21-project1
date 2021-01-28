import sys

template = '''{
  "program": "p4src/l2fwd.p4",
  "switch": "simple_switch",
  "compiler": "p4c",
  "options": "--target bmv2 --arch v1model --std p4-16",
  "switch_cli": "simple_switch_CLI",
  "cli": true,
  "pcap_dump": true,
  "enable_log": true,
  "topo_module": {
    "file_path": "",
    "module_name": "p4utils.mininetlib.apptopo",
    "object_name": "AppTopoStrategies"
  },
  "controller_module": null,
  "topodb_module": {
    "file_path": "",
    "module_name": "p4utils.utils.topology",
    "object_name": "Topology"
  },
  "mininet_module": {
    "file_path": "",
    "module_name": "p4utils.mininetlib.p4net",
    "object_name": "P4Mininet"
  },
  "topology": {
    "assignment_strategy": "l2",
    "links": [%s],
    "hosts": {
%s
    },
    "switches": {
%s
    }
  }
}
'''

k = int(sys.argv[1])
print(k)
half_k = k // 2
host_num = k * k * k // 4
tor_num = k * k // 2
agg_num = k * k // 2
core_num = k * k // 4

hosts = ''
# TODO
# print hosts

switches = ''
# TODO
# print switches

links = ''
# TODO
# print links

f = open("./topology/p4app_fat.json", "w")
f.write(template % (links, hosts, switches))
