import os
import json
from urllib.request import urlopen, urlretrieve

from rake_nltk import Rake

with open("gists.txt") as f:
    gist_ids = f.read().split()

with urlopen("https://api.github.com/users/carlthome/gists") as url:
    gists = json.loads(url.read().decode())

os.makedirs("posts", exist_ok=True)
for gist in gists:
    if gist["id"] not in gist_ids:
        continue

    name, metadata = list(gist["files"].items())[0]
    urlretrieve(metadata["raw_url"], f"posts/{name}")

    title = os.path.splitext(name)[0]
    description = gist["description"]
    slug = title.replace(" ", "-").lower()

    r = Rake()
    r.extract_keywords_from_text(f"{title}. {description}")
    tags = ",".join(r.get_ranked_phrases()[:3])

    with open(os.path.join("posts", title + ".meta"), "w") as f:
        f.write(
            f"""\
.. title: {title}
.. slug: {slug}
.. date: {gist['created_at']}
.. updated: {gist['updated_at']}
.. description: {description}
.. guid: {gist['id']}
.. link: {gist['html_url']}
.. tags: {tags}"""
        )
