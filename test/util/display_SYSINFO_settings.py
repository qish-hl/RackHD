# Copyright 2016, EMC, Inc.

"""
  Purpose:
  This script will generate a list of discovered nodes and display the system information for the nodes 
"""

import fit_path  # NOQA: unused import
import os
import sys
import subprocess

import fit_common
import test_api_utils


class display_sysinfo(fit_common.unittest.TestCase):
    def test_01_get_product_info(self):
        print "============== Displaying Product Info"
        nodes = test_api_utils.monorail_get_node_list(fit_common.fitargs()['ora'])
        if len(nodes) == 0:
            print "No Nodes found on Onrack server "+ fit_common.fitargs()['ora']
        else:
            inode=0
            while inode<len(nodes):
                nn=nodes[inode]
                print "Node: "+nn
                monurl = "/api/1.1/nodes/"+nn+"/catalogs/dmi"
                mondata = fit_common.rackhdapi(monurl)
                catalog = mondata['json']
                result = mondata['status']

                if result != 200:
                    print "Error on catalog/dmi command"
                else:
                    # Check BMC IP vs OBM IP setting
                    print " ID: "+catalog["id"]
                    print " Product Name : "+catalog["data"]["System Information"]["Product Name"]
                    print " Serial Number: "+catalog["data"]["System Information"]["Serial Number"]
                    print " UUID         : "+catalog["data"]["System Information"]["UUID"]
                inode +=1

    def test_02_get_catalog_source(self):
        print "============== Displaying Catalog Sources"
        nodes = test_api_utils.monorail_get_node_list(fit_common.fitargs()['ora'])
        if len(nodes) == 0:
            print "No Nodes found on Onrack server "+ fit_common.fitargs()['ora']
        else:
            inode=0
            while inode<len(nodes):
                print("")
                nn=nodes[inode]
                print "Node: "+nn

                monurl = "/api/1.1/nodes/"+nn+"/catalogs"
                mondata = fit_common.rackhdapi(monurl)
                catalog = mondata['json']
                result = mondata['status']

                if result != 200:
                    print "Error: failed catalog request"
                else:
                    i = 0
                    while i<len(catalog):
                        print "Source: "+catalog[i]["source"]
                        i +=1
                inode +=1

if __name__ == '__main__':
    fit_common.unittest.main()
