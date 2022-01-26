#!/bin/env python
# -*- coding: utf-8 -*-
from pymisp import ExpandedPyMISP
import pandas as pd
import os
EB=False
class key:
    misp_url = 'https://192.168.0.201/'
    misp_key = 'NLxMxFKOHrH219RQKxWY9adx2Kl7VKz7r1IkMje3'
    misp_verifycert = False

#pymisp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert, debug=True)

class misp:
    pymisp = ExpandedPyMISP(key.misp_url, key.misp_key, key.misp_verifycert)

    def valid_id_cve(cve):
        if (cve[0:3] == 'CVE'):
                x = cve.split(' ')
                x = x[0]
                x = 'CVE-' + x[4:8] + '-' + x[9:]
                return x
        else:
            return False

    def clean_id_cve(cve):
        cve_limp = []
        temp = 'temp.csv'
        with open(temp, 'w') as f:
            f.write(cve)
        cve = pd.read_csv(temp)
        cve = cve['value']
        for x in cve:
            if valid_id_cve(x) != False:
                if x not in cve_limp:
                    cve_limp.append(x)
        os.system('rm ' + temp)
        cve_limp = sorted(cve_limp)
        return cve_limp
