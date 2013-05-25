def fibonacci(n):
  #print "n",n
  if n == 0:
    #print "n =0 "
    return 0
  elif n==1 :
    #print "n=1"
    return 1
  else:
    return (fibonacci(n-1)+fibonacci(n-2))
  #print "this sucks!!", n

print "hello fibonacci"
print fibonacci(6)
    
