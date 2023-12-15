#!/usr/bin/env python3

import requests
import sys

def get_published_pages(domain):
    api_base = f"http://{domain}/wp-json/wp/v2/pages"
    params = {
        'status': 'publish',
        'per_page': 100,
        'page': 1
    }
    all_pages = []

    headers = {
        'Content-type': 'application/json',
        'User-agent': 'brettkelly.org' # we can't use the requests UA because WPE rejects it
    }
    while True:
        response = requests.get(api_base, params=params, headers=headers)
        if response.status_code != 200:
            break

        pages = response.json()
        if not pages:
            break

        for page in pages:
            lpath = page['link'].replace(f'https://{domain}','')
            all_pages.append(lpath)

        params['page'] += 1

    return all_pages

if(len(sys.argv) == 2):
    published_pages = get_published_pages(sys.argv[1].strip())
    for url in published_pages:
        print(url)