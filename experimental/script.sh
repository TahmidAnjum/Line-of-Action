mkfifo pipe
g++ one.cpp -o one
python3 two.py < pipe | ./one | tee pipe
#python3 two.py < pipe | ./one > pipe  # using this instead will not show output in the terminal
#./one < pipe | python3 two.py | tee pipe  
rm pipe