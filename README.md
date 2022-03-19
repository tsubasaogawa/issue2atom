# issue2atom

## Overview

This script generates Atom feed from GitHub Issues.

## Usage

### (a) Use GitHub Actions

1. Copy this repository to your account using template.
1. Fix issue2atom/.github/workflows/sample.yml
  - `on.schedule[0].cron`
  - `jobs.<job_name>.steps[2].with`
1. Run this workflow manually
1. Publish GitHub Pages with `gh-pages` branch
1. Browse https://<your_account>.github.io/<copied_repo_name>/<target_user>/<target_repo>/atom.xml

NOTE: sample.yml overwrites (i.e. force pushes) `gh-pages` branch. 

### (b) Run on local machine

1. Set up new python virtual environment. The script requires Python 3.8.
1. `pip install -r requirements.txt`
1. `USER=<target_user> REPO=<target_repo> python ./main.py`
1. main.py generates atom feed to `<target_user>/<target_repo>/atom.xml`

## Development

See Usage (b).
