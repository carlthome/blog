# Blog

My personal blog, powered by [Nikola](https://getnikola.com/).

## Install

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Use

Add new post with

```
nikola new_post -f markdown
```

or new page with

```
nikola new_page -f markdown
```

Build the site into a static release with

```
nikola build
```

The output in `output/` can be served by any web server.

## Develop

Start a local web server with hot reloading by

```
nikola auto
```
