#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <source_dir> <dest_dir>"
  exit 1
fi

SRC_DIR=$1
DEST_DIR=$2

if [ ! -d "$SRC_DIR" ]; then
  echo "Error: source directory '$SRC_DIR' does not exist."
  exit 1
fi

mkdir -p "$DEST_DIR"

MINIFY_OPTS=(
  --remove-literal-statements   # ドキュメンテーション文字列やリテラル単独文を削除
  --remove-asserts               # assert 文を削除
  --remove-debug                 # __debug__ チェックを含む条件文を削除
  --remove-class-attribute-annotations # クラス変数のアノテーションを削除
  --no-preserve-shebang          # shebang 行を削除
)

find "$SRC_DIR" -type f -name "*.py" | while IFS= read -r SRC_FILE; do
  REL_PATH="${SRC_FILE#$SRC_DIR/}"
  DEST_FILE="$DEST_DIR/$REL_PATH"
  mkdir -p "$(dirname "$DEST_FILE")"

  TMP1=$(mktemp)
  TMP2=$(mktemp)

  sed -E 's/([0-9])(else|for|and|or)/\1 \2/g' "$SRC_FILE" | sed -E 's/(else|for|and|or)([0-9])/\1 \2/g' > "$TMP1"

  if ! python3 rename_minifier.py "$TMP1" > "$TMP2"; then
    echo "Warning: rename_minifier.py failed for $SRC_FILE, using sed-only output."
    mv "$TMP1" "$TMP2"
  else
    rm "$TMP1"
  fi

  if ! pyminify "${MINIFY_OPTS[@]}" "$TMP2" > "$DEST_FILE"; then
    echo "Warning: pyminify failed for $SRC_FILE, skipping."
    rm -f "$TMP2"
    continue
  fi
  rm -f "$TMP2"

  echo "Minified: $SRC_FILE → $DEST_FILE"
done
