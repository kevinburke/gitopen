import imp
import os

from nose.tools import assert_equal

directory = os.path.dirname(os.path.realpath(__file__))
gitopen = imp.load_source('gitopen', os.path.join(directory, 'gitopen'))

def test_raw_host():
    assert_equal('github.com', gitopen._get_host('github.com-kevinburke'))
    assert_equal('github.com', gitopen._get_host('github.com'))

def test_parse():
    assert(gitopen._parse_git_remote_url('https://go.googlesource.com/go'))
    assert(gitopen._parse_git_remote_url('git@github.com-kevinburkeshyp:Shyp/rickover.git'))
    assert(gitopen._parse_git_remote_url('ssh://git@bitbucket.org/kevinburke/small-dotfiles.git'))
    assert(gitopen._parse_git_remote_url('https://git.heroku.com/pure-taiga-6832.git'))
    assert_equal(None, gitopen._parse_git_remote_url('blah'))
