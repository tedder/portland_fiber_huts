#!/usr/bin/python

import json

j = json.load(open('cop_fiber_hut_cand_sts_wgs84.geojson'))
#print j
for n,feature in enumerate(j['features']):
  v = feature['properties']['Viability']
  if v == 'Not Viable':
    feature['properties']['fill'] = '#f00 xx %s' % str(n)
    del j['features'][n]
  elif v == 'Viable':
    fc = feature['properties']['Fiber_Clas']
    if fc == 'High Review':
      feature['properties']['fill'] = '#0f0'
    elif fc == 'Medium Review':
      feature['properties']['fill'] = '#0b0'
    elif fc == 'Low Review':
      feature['properties']['fill'] = '#090'

print json.dumps(j, indent=1)
