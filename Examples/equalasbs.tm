# Specification of a Turing machine that checks
# if its input has same number of a's and b's
# Made by Howard Straubing
0 c 0 c R
0 B -1 B R
0 a 2 c R
0 b 1 c R
1 b 1 b R
1 c 1 c R
1 a 3 c L
2 b 3 c L
2 c 2 c R
2 a 2 a R
3 a 3 a L
3 b 3 b L
3 c 3 c L
3 B 0 B R
