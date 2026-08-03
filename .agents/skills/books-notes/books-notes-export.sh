#!/bin/bash
# books-notes-export.sh
#
# Reads Apple Books' local SQLite databases and outputs JSON.
# Requires the running terminal to have Full Disk Access
# (System Settings > Privacy & Security > Full Disk Access).
#
# Usage:
#   books-notes-export.sh list
#       Lists books that have at least one highlight, with asset_id,
#       title, author, and highlight_count.
#
#   books-notes-export.sh export <asset_id>
#       Outputs all highlights/notes for one book, ordered by
#       physical location, as JSON: text, note, cfi, location.

set -euo pipefail

LIB_DIR="$HOME/Library/Containers/com.apple.iBooksX/Data/Documents/BKLibrary"
ANN_DIR="$HOME/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation"

LIB_DB=$(ls -t "$LIB_DIR"/BKLibrary*.sqlite 2>/dev/null | head -n1 || true)
ANN_DB=$(ls -t "$ANN_DIR"/AEAnnotation*.sqlite 2>/dev/null | head -n1 || true)

if [[ -z "$LIB_DB" || -z "$ANN_DB" ]]; then
  echo "Could not locate the Apple Books databases under $LIB_DIR or $ANN_DIR." >&2
  echo "Check that Books.app has been opened at least once on this Mac, and that" >&2
  echo "this terminal application has Full Disk Access." >&2
  exit 1
fi

MODE="${1:-}"

case "$MODE" in
  list)
    sqlite3 -json "$LIB_DB" "
      ATTACH DATABASE '$ANN_DB' AS ann;
      SELECT b.ZASSETID AS asset_id,
             COALESCE(b.ZTITLE, b.ZSORTTITLE) AS title,
             COALESCE(b.ZAUTHOR, b.ZSORTAUTHOR) AS author,
             COUNT(a.Z_PK) AS highlight_count
      FROM ZBKLIBRARYASSET b
      LEFT JOIN ann.ZAEANNOTATION a
        ON a.ZANNOTATIONASSETID = b.ZASSETID
        AND a.ZANNOTATIONSELECTEDTEXT IS NOT NULL
        AND a.ZANNOTATIONSELECTEDTEXT != ''
      GROUP BY b.ZASSETID
      HAVING highlight_count > 0
      ORDER BY author, title;
    "
    ;;
  export)
    ASSET_ID="${2:-}"
    if [[ -z "$ASSET_ID" ]]; then
      echo "Usage: $0 export <asset_id>" >&2
      exit 1
    fi
    sqlite3 -json "$ANN_DB" "
      SELECT ZANNOTATIONSELECTEDTEXT AS text,
             ZANNOTATIONNOTE AS note,
             ZANNOTATIONLOCATION AS cfi,
             ZFUTUREPROOFING5 AS chapter,
             COALESCE(NULLIF(ZPLABSOLUTEPHYSICALLOCATION, 0),
                      ZPLLOCATIONRANGESTART) AS location
      FROM ZAEANNOTATION
      WHERE ZANNOTATIONASSETID = '$ASSET_ID'
        AND ZANNOTATIONSELECTEDTEXT IS NOT NULL
        AND ZANNOTATIONSELECTEDTEXT != ''
      ORDER BY COALESCE(NULLIF(ZPLABSOLUTEPHYSICALLOCATION, 0),
                        ZPLLOCATIONRANGESTART),
               ZANNOTATIONCREATIONDATE;
    "
    ;;
  *)
    echo "Usage: $0 {list|export <asset_id>}" >&2
    exit 1
    ;;
esac
