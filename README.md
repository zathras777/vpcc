vpcc
====

Variable Pitch Co-ordinate Converter

This class allows for simple conversion between geographic
co-ordinate schemes commonly used in the UK. At present it
provides conversion between OS Grid References (either as
a single identifier or an Easting/Northing pair), OS Grid
latitude/longitude and WGS84 latitude/longitude.

History
-------

This module was written to solve a need for the Variable Pitch
 http://www.variablepitch.co.uk/ website and will be used there
 for co-ordinate transformations.

 It's intended to be very lightweight and dependency free.

Example
-------

```
>>> import vpcc
>>> pt = vpcc.Point('gridref', 'TG 51409 13177')
>>> print pt['wgs84']
[52.70925049775599, -3.2865464818856553]
>>> pt.pretty_string('wgs84')
['N52 42 33.3018', 'E003 17 11.5673']
>>> pt.dump()
  UK Grid Reference (alphanmueric): ['TG5140913177']
  OSGB36 latitide/longitude: ['N52 42 32.1336', 'E003 17 06.9396']
  UK Grid Reference (numeric E/N): [651409, 313177]
  WGS84 latitude/longitude: ['N52 42 33.3018', 'E003 17 11.5673']
```

Development
-----------

This is an initial release of the code and there are bound to be bugs.
The maths involved can probably be improved, but the results produced are
very close to the javascript versions they are based on. Improvements are
welcome.

Presently this module only exposes the Point class as I have no current need
for more advanced shapes or structures, but adding other shapes/structures
should be easy enough.
