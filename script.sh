mkfifo pipe
g++ main.cpp -o main
#python3 main.py < pipe | ./main | tee pipe
python3 main.py < pipe | ./main > pipe  # using this instead will not show output in the terminal
#./main < pipe | python3 main.py | tee pipe  
rm pipe