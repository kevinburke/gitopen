import imp
import os

from nose.tools import assert_equal

directory = os.path.dirname(os.path.realpath(__file__))
gitopen = imp.load_source('gitopen', os.path.join(directory, 'gitopen'))

def test_raw_host():
    assert_equal('github.com', gitopen._get_host('github.com-kevinburke'))
    assert_equal('github.com', gitopen._get_host('github.com'))
