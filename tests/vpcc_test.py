import unittest

import vpcc

class TestCase1(unittest.TestCase):
    def test_01(self):
        """ Test creation to ensure it only allows valid schemes
            and co-ordinates.
        """
        totry = (
            ('abc', False, 123),
            ('gridref', True, 'TG123456'),
            ('gridref', True, 'TG 123 456'),
            ('osref', False, 651409, 'abc'),
            ('osref', False, 651409),
            ('osref', False, 65, 1234),
            ('osref', True, 651409, 313177),
            ('osreference', False, 651409, 313177),
            ('osgb36', True, [50.00, -2.00]),
            ('wgs84', True, 52.70925049775599, -3.2865464818856553),
            ('wgs84', False, 92.1, 100.0),
            ('wgs84', False, 89.1, -190.0),
            ('airy1830', False)
        )
        for t in totry:
            try:
                pt = vpcc.Point(t[0], *t[2:])
                ck = True
            except (vpcc.InvalidScheme, vpcc.ConversionError):
                ck = False
            self.assertEqual(ck, t[1])

    def test_02(self):
        """ Check conversions using trusted values.
        """
        totry = (
            (('wgs84', 52.70925049775599, -3.2865464818856553),
             ('gridref', 'SJ1317613176'),
             ('osref', 313176, 313176)
            ),
            (('gridref', 'TG 51409 13177'),
             ('gridref', 'TG5140913177'),
             ('osref', 651409, 313177),
             ('osgb36', 52.708926, -3.285261),
             ('wgs84', 52.70925049775599, -3.2865464818856553)
            ),

        )
        for t in totry:
            try:
                pt = vpcc.Point(t[0][0], *t[0][1:])
            except (vpcc.InvalidScheme, vpcc.ConversionError):
                self.fail("Invalid point creation")
            for ck in t[1:]:
                val = pt[ck[0]]
                if type(val) is list:
                    if len(val) != len(ck[1:]):
                        self.fail("Didn't get expected style of value")
                    for i in range(len(val)):
                        if val[i] != ck[i + 1]:
                            self.fail("Returned value %d didn't match (%d vs %s)" % (i, val[i], ck[i+1]))
                elif val != ck[1]:
                    self.fail("Returned value didn't match expected")


def test_suite():
    return unittest.makeSuite(TestCase1)
