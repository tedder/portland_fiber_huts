#!/usr/bin/python

import shapefile

sf = shapefile.Reader("cop_fiber_hut_cand_sts.shp")
shapes = sf.shapes()
print "shape fields: %s" % sf.fields
for shape in shapes:
  print "shape: %s" % shape
  break
