import os
import kaggle
import tqdm.auto as tqdm

USER = "carlthome"
OUTPUT_DIRECTORY = "posts"

kernels = kaggle.api.kernels_list(user=USER)


for kernel in tqdm.tqdm(kernels, desc="Downloading Kaggle kernels"):
    if kernel.isPrivate:
        continue

    # Collect metadata.
    title = kernel.title.replace("/", "|")
    description = kernel.title  # TODO
    slug = kernel.ref.replace(f"{USER}/", "")
    updated_at = kernel.lastRunTime
    created_at = updated_at  # TODO
    guid = kernel.ref
    link = f"https://kaggle.com/{kernel.ref}"
    tags = ""  # TODO

    # Download notebook.
    kaggle.api.kernels_pull(kernel.ref, OUTPUT_DIRECTORY)

    # Write post metadata.
    with open(os.path.join(OUTPUT_DIRECTORY, slug + ".meta"), "w") as f:
        f.write(
            f"""\
.. title: {title}
.. slug: {slug}
.. date: {created_at}
.. updated: {updated_at}
.. description: {description}
.. guid: {guid}
.. link: {link}
.. tags: {tags}"""
        )
