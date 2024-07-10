#!/usr/bin/env bash
#
# Remove text that's

HEADER="---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.2
kernelspec:
  display_name: python3
  language: python
  name: python3
---
"
# \-escape the newlines for use in Sed.
HEADER=${HEADER//$'\n'/\\$'\n'}

for f in docs/source/*md; do

    # don't do this on index or if we've already removed text
    if [[ "$f" =~ "index" || "$f" =~ "stripped" ]]; then
        continue
    fi

    out_f="${f/.md/-stripped.md}"
    TITLE="$(grep '^# ' $f | head -1)"
    sed -E -n -e '/^#/p' -e '/\{code-cell\}|:::/,/```|:::/p' "$f" > "$out_f"
    sed -i "s/${TITLE}/${TITLE}, Text Removed\n/g" "$out_f"
    sed -i "1s/^/${HEADER}/g" "$out_f"

done
