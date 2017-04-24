for d in `ssh comet 'ls -d /home/kyu2/_/scratch/Bullet/*/'`;\
do (echo "$d"; rsync -avzP comet:"$d"/post ./$(basename "$d")/ ;\
); done
