import time

number = int(raw_input())

for k in range(number):
    time.sleep(1)
    print 'tick', k+1
print 'boom!'

