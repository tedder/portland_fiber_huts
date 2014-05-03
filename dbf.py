#!/usr/bin/python

from dbfpy import dbf

fh = open("cop_fiber_hut_cand_sts.dbf")
fc = []
for rec in dbf.Dbf(fh):
  print rec
  break
  f['type'] = 'Point'
  f['geometry'] = { 'type': 'Point', coordinates:[x, y] }
  f['properties'] =  {'x':'y'}

  owner = "\n".join( (rec['OWNER1'], rec['OWNER2'], rec['OWNER3') )
  txt = """Owner: %s
Department: %s
Review: %s (%s)
Viable? %s (%s)
ID: %s
""" % (owner, rec['CITY_BUREA'], rec['REVIEW_CLA'], rec['REVIEW_REA'], rec['VIABILITY'], rec['VIABILITY_'], rec['STATE_ID'])
  fc.append(f)


output['type'] = 'FeatureCollection'
output['features'] = fc
