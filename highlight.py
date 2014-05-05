#!/usr/bin/python

import json
import sys

j = json.load(open('cop_fiber_hut_cand_sts_wgs84.geojson'))
#print j
print >> sys.stderr, "starting with %g features" % len(j['features'])

for n,feature in enumerate(j['features']):
  v = feature['properties']['Viability']
  if v == 'Not Viable':
    # we'll strip these later
    pass
  elif v == 'Viable':
    fc = feature['properties']['Fiber_Clas']
    if fc == 'High Review':
      feature['properties']['fill'] = '#ff710d'
      feature['properties']['stroke-width'] = 1
    elif fc == 'Medium Review':
      feature['properties']['fill'] = '#ff9326'
      feature['properties']['stroke-width'] = 0
    elif fc == 'Low Review':
      feature['properties']['fill'] = '#ffbf40'
      feature['properties']['stroke-width'] = 0

j['features'] = [x for x in j['features'] if x['properties']['Viability'] == 'Viable']

print >> sys.stderr, "finished with %g features" % len(j['features'])
print json.dumps(j, indent=1)
