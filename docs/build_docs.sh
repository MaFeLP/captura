#!/usr/bin/env bash
set -euo pipefail

baseurl="$1"

cd "$(dirname "$0")" || exit 1

# Generate python api documentation
sphinx-apidoc -o sphinx ../captura
sphinx-build -M markdown sphinx sphinx/_build
mv sphinx/_build/markdown/captura.md sphinx/_build/markdown/index.md

files=$(find 'sphinx/_build/markdown' -name '*.md')

mkdir -p _api

for file in ${files}; do
  title="$(grep '# ' "$file" | head -n 1)#"
  title="${title:2:-1}"
  echo "Processing file $(basename "$file") \"$title\""

  sed -i 's/.md/.html/g' "$file"
  sed -i 's/captura.html/index.html/g' "$file"
  cat > "_api/$(basename "$file")" <<EOF
---
title: '${title}'
layout: default
---
EOF

  echo "Appending $file to _api/$(basename "$file")..."
  cat "$file" >> "_api/$(basename "$file")"
done

sed -i "s/title: 'captura'/title: 'Module Information'/g" _api/modules.md
bundle exec jekyll serve --watch --baseurl "${baseurl}"

