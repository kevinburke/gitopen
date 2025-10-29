import importlib.util
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
gitopen_path = os.path.join(directory, 'gitopen')

# Read and compile the gitopen file directly since it has no .py extension
with open(gitopen_path, 'r') as f:
    gitopen_code = f.read()

# Create a module and execute the code in its namespace
import types
gitopen = types.ModuleType('gitopen')
exec(compile(gitopen_code, gitopen_path, 'exec'), gitopen.__dict__)

def test_raw_host():
    assert 'github.com' == gitopen._get_host('github.com-kevinburke')
    assert 'github.com' == gitopen._get_host('github.com')

def test_parse():
    assert gitopen._parse_git_remote_url('https://go.googlesource.com/go')
    assert gitopen._parse_git_remote_url('git@github.com-kevinburkeshyp:Shyp/rickover.git')
    assert gitopen._parse_git_remote_url('ssh://git@bitbucket.org/kevinburke/small-dotfiles.git')
    assert gitopen._parse_git_remote_url('https://git.heroku.com/pure-taiga-6832.git')
    assert None == gitopen._parse_git_remote_url('blah')

if __name__ == '__main__':
    # Simple test runner
    tests = [test_raw_host, test_parse]
    failed = 0
    passed = 0

    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1

    print(f"\n{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)
