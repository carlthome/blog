#!/usr/bin/env bash
set -e

# TODO https://github.com/jupyter/nbconvert/issues/1731

find . -type f -name "*.ipynb" -print0 | while IFS= read -r -d '' post; do
    echo "Stripping widgets from $post"
    jq -M 'del(.metadata.widgets)' "$post" > "$post.tmp"
    mv "$post.tmp" "$post"
done
