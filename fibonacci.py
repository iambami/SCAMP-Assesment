Number = int(input("\nPlease Enter the Range Number: "))
i = 0
Value_One = 0
Value_Two = 1
           
# Find & Displaying Fibonacci series
while(i < Number):
           if(i <= 1):
                      Value = i
           else:
                      Value = Value_One + Value_Two
                      Value_One = Value_Two
                      Value_Two = Value
           print(Value)
           i = i + 1
