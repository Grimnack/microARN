set terminal png
set autoscale
set output 'occurencesARNKMP.png'
plot "occurencesARNKMP.dat" using 1:2
