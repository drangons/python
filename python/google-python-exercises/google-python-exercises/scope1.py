def foo(x):
  print 'point 2:', id(x)
  x.append(4)
  print 'point 3:', id(x)
def main():
  L = [1, 2, 3]
  print 'point 1:', id(L)
  foo(L)
  print 'point 4:', id(L)
  
if __name__ == '__main__':
  main()
