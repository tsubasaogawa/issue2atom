# issue2atom action

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

#### Inputs

|key|description|required|default|
|---|-----------|--------|-------|
|user|Target GitHub user name|true|octocat|
|repo|Target GitHub repository name|true|hello-world|
|max_issue_num|The number of issues included in Atom|false|10|
|per_page|The number of request issues|false|30|
|allow_pr|Allow pull request or not|false|false|

#### Outputs

|key|description|
|---|-----------|
|status_code|Status code from Github API|
|atom_file_path|ATOM file path|
|atom_file_size|ATOM file size|

#### Example

```yaml
# Generate atom feed in an instance by GitHub Actions
uses: tsubasaogawa/issue2atom-action@v1
with:
    user: "octocat"
    repo: "hello-world"
    max_issue_num: 10
```

### (b) Run on local machine

1. Set up new python virtual environment. The script requires Python 3.8.
1. `pip install -r requirements.txt`
1. `USER=<target_user> REPO=<target_repo> python ./main.py`
1. main.py generates atom feed to `<target_user>/<target_repo>/atom.xml`

## Development

See Usage (b).
