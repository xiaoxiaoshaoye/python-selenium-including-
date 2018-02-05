#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  yaml
import  os
from yaml import  load,dump

# aproject = {'name': 'Silenthand Olleander',
#                     'race': 'Human',
#                      'traits': ['ONE_HAND', 'ONE_EYE']
#                     }
#
#
# print (yaml.dump(aproject))

filename = os.path.join(os.path.dirname(__file__),'testyaml.yaml'.replace('\\','/'))
f = open(filename)
x = load(f)
print(x)
