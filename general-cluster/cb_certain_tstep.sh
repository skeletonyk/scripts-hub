for d in `ssh comet 'ls -d /home/kyu2/_/scratch/Bullet/AIAA/Re800.0'`;\
do ( \
mkdir "$(basename "$d")";\
mkdir "$(basename "$d")/outputs";\
echo "$d"; rsync -avzP comet:"$d"/outputs/flow/tstep-0000006144 ./$(basename "$d")/outputs/flow ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/flow/ini* ./$(basename "$d")/outputs/flow ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/flow/last* ./$(basename "$d")/outputs/flow ;\

echo "$d"; rsync -avzP comet:"$d"/outputs/body/tstep-0000006144 ./$(basename "$d")/outputs/body ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/body/ini* ./$(basename "$d")/outputs/body ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/body/last* ./$(basename "$d")/outputs/body ;\

echo "$d"; rsync -avzP comet:"$d"/outputs/grid/tstep-0000006144 ./$(basename "$d")/outputs/grid ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/grid/ini* ./$(basename "$d")/outputs/grid ;\
echo "$d"; rsync -avzP comet:"$d"/outputs/grid/last* ./$(basename "$d")/outputs/grid ;\
); done
