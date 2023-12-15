# Hi.

This little ditty will pull all published pages from a WordPress site and spit out the relative paths to the console.

I use this when I need to generate a list of redirects after replacing an old site with a new one.

### Install

`poetry install` to install dependencies

`poetry run python3 main.py somewordpresssite.com`

Replace `somewordpresssite.com` with the site you want to query.
