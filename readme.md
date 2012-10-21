# Gitopen

This is a convenience script to open the repo corresponding to a Git remote
URL in your default browser.

### Usage

From anywhere in a Git repo:

```bash
$ git remote -v | grep push
origin	git@github.com:kevinburke/gitopen.git (push)

$ gitopen origin
```

Will open `https://github.com/kevinburke/gitopen` in your browser.

### Installation

1. Clone this repository
2. Place the `gitopen` executable somewhere on your PATH, possibly like this:

    ln -s gitopen /usr/local/bin

### Features

* Works with URL's behind the firewall (eg private installs)
* Works with SSH and git-read-only URL's
