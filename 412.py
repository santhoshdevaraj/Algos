# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output "Fizz" instead of the number and for the multiples of 
# five output "Buzz". For numbers which are multiples of both three and five output "FizzBuzz".

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def stringify(num):
            if num % 5 == 0 and num % 3 == 0:
                return 'FizzBuzz'
            elif num % 5 == 0:
                return 'Buzz'
            elif num % 3 == 0:
                return 'Fizz'
            return str(num)
        
        return map(lambda num: stringify(num), xrange(1, n+1))

print Solution().fizzBuzz(15)