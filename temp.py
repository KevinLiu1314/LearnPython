from time import time
t1=time()
def factors(n):
   i=1
   while i*i<=n:
      if not n%i:
         yield i
         yield n//i
      i+=1
   if i*i==n:
      yield i

def isAbundant(n):
   return sum(set(factors(n)))>2*n

b=list()
for i in xrange(28124):
   if isAbundant(i):
      b.append(i)


w=list()
for i in xrange(len(b)):
   for j in xrange(i,len(b)):
      tmp=b[i]+b[j]
      if tmp>28123:
         break
      w.append(tmp)


print sum(set(range(28123))-set(w)),time()-t1