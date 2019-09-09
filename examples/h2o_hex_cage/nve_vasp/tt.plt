#! /usr/bin/gnuplot

# Functions (1/0 means not defined)
a = 0.9
f(x) = abs(x)<2*pi ? a*sin(x)           : 1/0
g(x) = abs(x)<2*pi ? a*sin(x+pi/2)      : 1/0
h(x) = abs(x)<2*pi ? a*sin(x+pi)        : 1/0
k(x) = abs(x)<2*pi ? a*sin(x+3.0/2*pi)  : 1/0

### Start multiplot (2x2 layout)
set multiplot layout 2,2 rowsfirst
# --- GRAPH a
set label 1 'a' at graph 0.92,0.9 font ',8'
plot f(x) with lines ls 1
# --- GRAPH b
set label 1 'b' at graph 0.92,0.9 font ',8'
plot g(x) with lines ls 1
# --- GRAPH c
set label 1 'c' at graph 0.92,0.9 font ',8'
plot h(x) with lines ls 1
# --- GRAPH d
set label 1 'd' at graph 0.92,0.9 font ',8'
plot k(x) with lines ls 1
unset multiplot

pause mouse
