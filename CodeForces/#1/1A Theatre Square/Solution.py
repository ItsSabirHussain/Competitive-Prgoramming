#The constraint that edges of each flagstone much be parralel to edges of the square allows to analyze X and Y axes separately,
# that is, how many segments of length 'a' are needed to cover segment of length 'm' and 'n' -- and take product of these two
# quantities. Answer = ceil(m/a) * ceil(n/a), where ceil(x) is the least integer which is above or equal to x. Using integers
# only, it is usually written as ((m+a-1)/a)*((n+a-1)/a). Note that answer may be as large as 10^18, which does not fit in 32-bit
# integer.
#Most difficulties, if any, contestants had with data types and operator priority, which are highly dependant on language
# used, so they are not covered here.


import math; n, m, a = map(int, input().split(" ")); print(math.ceil(m/a) * math.ceil(n/a))
