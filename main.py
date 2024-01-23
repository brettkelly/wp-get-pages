#!/usr/bin/env python3

import requests
import sys

def get_published_pages(domain, cpt):
    api_base = f"http://{domain}/wp-json/wp/v2/{cpt}"
    params = {
        'status': 'publish',
        'per_page': 100,
        'page': 1
    }
    all_pages = []

    headers = {
        'Content-type': 'application/json',
        'User-agent': 'brettkelly.org' # we can't use the requests UA because stupid WPE rejects it
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

if(len(sys.argv) == 3):
    domain = sys.argv[1].strip()
    cpt = sys.argv[2].strip()
    published_pages = get_published_pages(domain, cpt)
    for url in published_pages:
        print(url)
else:
    usage = """
Usage:
    poetry run python3 main.py domain.com cpt_slug
"""
    print(usage)