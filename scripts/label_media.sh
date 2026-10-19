#!/bin/sh
# Write the reference-file label (decision 8 of the site plan) into card PNGs and clips, in place:
# IPTC digital source type "trainedAlgorithmicMedia" (made by a trained AI model), creator "Sower Tarot"
# and the CC BY-NC-SA 4.0 licence, as XMP. Pixels, frames and a PNG's tarot_render record are kept.
# Run it before computing checksums (scripts/checksums.py write): the label is part of the file.
#   scripts/label_media.sh content/media/card_<slug>.png content/media/<clip>.mp4 ...
[ $# -gt 0 ] || { echo "usage: $0 FILE..." >&2; exit 2; }
CC=https://creativecommons.org/licenses/by-nc-sa/4.0/
exec exiftool -q -overwrite_original \
  -XMP-iptcExt:DigitalSourceType=http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia \
  -XMP-dc:Creator="Sower Tarot" \
  -XMP-dc:Rights="© 2026 Sower Tarot. Licensed under CC BY-NC-SA 4.0, $CC" \
  -XMP-xmpRights:Marked=True -XMP-xmpRights:WebStatement="$CC" \
  -XMP-cc:License="$CC" -XMP-cc:AttributionName="Sower Tarot" \
  "$@"
