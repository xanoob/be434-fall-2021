""" Tests for product.py """

import os
from subprocess import getstatusoutput

PRG = './product.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_no_args():
    """ Dies with no arguments """

    rv, out = getstatusoutput(f'{PRG}')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test_dies_not_numbers():
    """ Dies with non-number arguments """

    rv, out = getstatusoutput(f'{PRG} foo bar')
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def test1():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 0')
    assert rv == 0
    assert out.strip() == '0 = 0'


# --------------------------------------------------
def test2():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 1')
    assert rv == 0
    assert out.strip() == '1 = 1'


# --------------------------------------------------
def test3():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 0 1')
    assert rv == 0
    assert out.strip() == '0 * 1 = 0'


# --------------------------------------------------
def test4():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} 1 2 3')
    assert rv == 0
    assert out.strip() == '1 * 2 * 3 = 6'


# --------------------------------------------------
def test5():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} -2 3 4')
    assert rv == 0
    assert out.strip() == '-2 * 3 * 4 = -24'
