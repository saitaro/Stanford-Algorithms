from heapq import *
from collections import Counter

low		= []
high	= []
medians = Counter()

with open('C:/Users/NewVici/Dropbox/[Current Project]/_Median.txt') as file:
	for row in file: # file [1,2,3,4,5,6] [1,-2,3,4,5,-6]
		new = int(row)
		if not low or new < -low[0]:
			heappush(low, -new)
		else:
			heappush(high, new)
		if len(low) > len(high) + 1:
			heappush(high, -heappop(low))
		elif len(high) > len(low) + 1:
			heappush(low, -heappop(high))
		length = len(low) + len(high)
		if not low or not high:
			medians[high[0] if not low else -low[0]] += 1
		elif length % 2:
			medians[high[0] if len(high) > len(low) else -low[0]] += 1
		else:
			medians[-low[0]] += 1
		# print sorted([-x for x in low] + high), medians[-1]

# print len(high) + len(low), count
# print 'ANSWER', medians
print sum([item[0] * item[1] for item in medians.items()]) % 10000, #help(Counter)