i = 0
Value_One = 0
Value_Two = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = Value_One + Value_Two
                      Value_One = Value_Two
                      Value_Two = Next
           print(Next)
           i = i + 1