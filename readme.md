# Gitopen

This is a convenience script to open one of your remote URL's in your default
browser.

### Usage

From anywhere in a Git repo:

```bash
$ git remote -v | grep push
origin	git@github.com:kevinburke/gitopen.git (push)

$ gitopen origin
```

Will open `https://github.com/kevinburke/gitopen` in your browser.

### Features

* Works with URL's behind the firewall (eg private installs)
* Works with SSH and git-read-only URL's
