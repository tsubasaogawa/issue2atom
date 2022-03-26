# issue2atom action

## Overview

This script generates Atom feed from GitHub Issues.

### Generated Atom feed sample

Target issue is [octocat/hello-world](https://github.com/octocat/hello-world/issues)

```xml
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
    <id>tag:issue2atom,2006-01-02:/octocat/hello-world/issues</id>
    <title>octocat/hello-world - GitHub Issues</title>
    <updated>2022-03-26T15:02:35.517122+00:00</updated>
    <author>
        <name>octocat</name>
    </author>
    <link href="https://github.com/octocat/hello-world/issues" rel="alternate" />
    <generator uri="https://lkiesow.github.io/python-feedgen" version="0.9.0">python-feedgen</generator>
    <subtitle>GitHub Issues of octocat/hello-world</subtitle>
    <entry>
        <id>tag:issue2atom,2006-01-02:/octocat/hello-world/issues/2237</id>
        <title>Check This out</title>
        <updated>2022-03-25T05:46:38+00:00</updated>
        <content type="html">&lt;p&gt;This is a test body&lt;/p&gt;</content>
        <link href="https://github.com/octocat/Hello-World/issues/2237" rel="alternate" />
        <summary>This is a test body...</summary>
        <published>2022-03-25T05:45:05+00:00</published>
    </entry>
    :
</feed>
```

## Usage

### (a) Use GitHub Actions

See also [sample.yml](https://github.com/tsubasaogawa/issue2atom/.github/workflows/sample.yml)

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
|shorten_length|Length of &lt;summary&gt; section|100|
|atom_base_url|Parent URL of atom file. ex) https://foo.github.io/issue2atom if atom URL of octocat/hello-world is https://foo.github.io/issue2atom/octocat/hello-world/atom.xml|''|
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
