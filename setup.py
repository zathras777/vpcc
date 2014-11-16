#!/usr/bin/env python

import os
from distutils.core import setup
from distutils.cmd import Command
from unittest import TestLoader, TextTestRunner


class TestCommand(Command):
    """ Run module test suite """
    description="Run tests"
    user_options = []
    
    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass
        
    def run(self):
        testfiles = []
        for poss_fn in os.listdir(os.path.join(self._dir, 'tests')):
            if not poss_fn.endswith('_test.py'):
                continue
            testfiles.append('.'.join(['tests', 
                                       os.path.splitext(poss_fn)[0]]))
        tests = TestLoader().loadTestsFromNames(testfiles)
        t = TextTestRunner(verbosity=self.verbose)
        t.run(tests)


setup(
    name='vpcc',
    version='0.1',
    description='Python module to convert geographic co-ordinates for the UK',
    author='David Reid',
    py_modules=['vpcc'],
    author_email='zathrasorama@gmail.com',
    url='http://www.variablepitch.co.uk/vpcc/',
    cmdclass={'test': TestCommand}
)
