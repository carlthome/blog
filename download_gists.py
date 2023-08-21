import os
import json
from urllib.request import urlopen, urlretrieve

import tqdm.auto as tqdm
from rake_nltk import Rake

USER = "carlthome"
OUTPUT_DIRECTORY = "posts"

# List all gists for the given USER.
with urlopen(f"https://api.github.com/users/{USER}/gists") as url:
    gists = json.loads(url.read().decode())

# Create output directory.
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

for gist in tqdm.tqdm(gists, desc="Downloading gists"):
    name, metadata = list(gist["files"].items())[0]
    title, extension = os.path.splitext(name)

    # Skip gists that are not Jupyter Notebooks.
    if extension != "ipynb":
        continue

    # Download notebook.
    urlretrieve(metadata["raw_url"], f"posts/{name}")

    # Collect post metadata.
    description = gist["description"]
    slug = title.replace(" ", "-").lower()
    metadata = f"{title}. {description}"

    # Extract keywords from metadata.
    r = Rake()
    r.extract_keywords_from_text(metadata)
    tags = ",".join(r.get_ranked_phrases()[:3])

    # Write post metadata file.
    with open(os.path.join(OUTPUT_DIRECTORY, title + ".meta"), "w") as f:
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
