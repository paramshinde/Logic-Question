'''Create a list of 10 numbers.
Print the sum of all numbers
Print the largest and smallest number'''
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list

    def find_sum(self):
        total=0
        for num in self.num_list:
            total+=num
        return total
    
    def find_largest(self):
        largest=self.num_list[0]
        for num in self.num_list:
            if num>largest:
                largest=num
        return largest

    def find_smallest(self):
        smallest=self.num_list[0]
        for num in self.num_list:
            if num<smallest:
                smallest=num
        return smallest
    
    def count_even_number(self):
        count=0
        for num in self.num_list:
            if num%2==0:
                count+=1
        return count
    
    def count_odd_number(self):
        count=0
        for num in self.num_list:
            if num%2!=0:
                count+=1
        return count

numbers=[10, 4, 7, 22, 5, 1, 9, 15, 3, 8]
obj=Lists(numbers)
print("Sum: ",obj.find_sum())
print("Largest: ",obj.find_largest())
print("Smallest: ",obj.find_smallest())
print("Even count: ",obj.count_even_number())
print("Odd Count: ",obj.count_odd_number())