from feedgen.feed import FeedGenerator
import json
import os
import requests


REQUEST_HEADER = {
    'Accept': 'application/vnd.github.v3+json'
}

USER = os.environ['USER']
REPO = os.environ['REPO']

MAX_ISSUE_NUM = int(os.environ.get('MAX_ISSUE_NUM', '10'))
REQUEST_URI = f'https://api.github.com/repos/{USER}/{REPO}/issues?per_page={MAX_ISSUE_NUM}'


def main():
    response = requests.get(REQUEST_URI, headers=REQUEST_HEADER)
    issues = json.loads(response.text)
    feed_id = f'issue2atom_{USER}/{REPO}/issues'

    feed = FeedGenerator()

    feed.id(feed_id)
    feed.title(f'GitHub Issues {USER}/{REPO}')
    feed.author({'name': USER})
    feed.link(href=f'https://github.com/{USER}/{REPO}/issues', rel='alternate')
    # fg.logo('http://ex.com/logo.jpg')
    feed.subtitle(f'GitHub Issues of {USER}/{REPO}')
    # fg.link( href='http://larskiesow.de/test.atom', rel='self' )
    feed.language('en')

    target_issues = sorted(
        issues[0:MAX_ISSUE_NUM],
        key=lambda x: x['number'],
        reverse=False
    )
    for issue in target_issues:
        entry = feed.add_entry()
        entry.id(f'{feed_id}/{issue["number"]}')
        entry.title(issue['title'])
        entry.link(href=issue['html_url'], rel='alternate')
        entry.published(issue['created_at'])
        entry.updated(issue['updated_at'])
        entry.summary(issue['body'])

    save_dir = f'{USER}/{REPO}'
    atom_file = f'{save_dir}/atom.xml'

    os.makedirs(save_dir, exist_ok=True)
    feed.atom_file(atom_file)

    print(f"::set-output name=status_code::{response.status_code}")
    print(f"::set-output name=atom_file_path::{atom_file}")
    print(f"::set-output name=atom_file_size::{os.path.getsize(atom_file)}")


if __name__ == '__main__':
    main()
