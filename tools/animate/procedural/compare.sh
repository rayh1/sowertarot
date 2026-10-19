#!/bin/bash
# compare.sh AI.mp4 CODE.mp4 OUT.mp4 [seconds]  -> side by side (AI left, code right), both 896 px high, looping
set -e
LA=${5:-AI clip}; LB=${6:-code clip}
F=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
D=${4:-12}
lab() { echo "drawtext=fontfile=$F:text='$1':x=14:y=14:fontsize=30:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=8"; }
ffmpeg -y -loglevel error -stream_loop -1 -i "$1" -stream_loop -1 -i "$2" -filter_complex \
 "[0:v]scale=-2:896,setsar=1,$(lab "$LA")[l];[1:v]scale=-2:896,setsar=1,$(lab "$LB")[r];[l][r]hstack=inputs=2,format=yuv420p[v]" \
 -map "[v]" -t "$D" -r 24 -c:v libx264 -crf 18 -movflags +faststart "$3"
