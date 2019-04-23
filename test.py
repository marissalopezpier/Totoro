# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:04:52 2019

@author: Marissa
"""

import re
import random
import hashlib
import os
from subprocess import getstatusoutput, getoutput

prg = './mileage.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_badinputs1():
    expected = "Miles must be greater than zero"
    rv, out = getstatusoutput('{} -2 2'.format(prg))
    assert rv > 0
    assert out == expected


# --------------------------------------------------
def test_badinputs2():
    expected = "Gallons must be greater than zero"
    rv, out = getstatusoutput('{} 2 -2'.format(prg))
    assert rv > 0
    assert out == expected


# --------------------------------------------------
def test_badinputs3():
    expected = "Miles and gallons must be greater than zero"
    rv, out = getstatusoutput('{} -2 -2'.format(prg))
    assert rv > 0
    assert out == expected


# --------------------------------------------------
def test_badinputs4():
    expected = "Date must have month, day, and year specified ordered(yearmonthday): i.e. 190422"
    rv, out = getstatusoutput('{} 2 2 -d 190245'.format(prg))
    assert rv > 0
    assert out == expected


# --------------------------------------------------
def test_one():
    expected = "Old Average MPG: 21.074074074074073\nNew MPG added: 17.727272727272727\nNew Average MPG: 20.237373737373737"
    f = 'mpg1.csv'
    os.system('rm {}'.format(f))
    for m, g, d in zip([200,210,200,195],[10,10,9,11],[190410,190411,190412,190413]):   
        rv, out = getstatusoutput('{} {} {} -d {} -f {}'.format(prg,m,g,d,f))
        assert rv == 0
    assert out == expected