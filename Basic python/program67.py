#import the 'collections'module,which provides the 'counter'class.
import collections
num=[2,2,4,6,6,6,8,10,4]
result=sum(collections.Counter(num).values())
print(result)