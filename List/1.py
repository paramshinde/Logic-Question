'''Create a list of 10 numbers.
Print the sum of all numbers
Print the largest and smallest number'''
class Lists:
    def __init__(self,num_list):
        self.num_list=num_list
    
    def find_sum(self):
        total=0
        for i in self.num_list:
            total=total+i
        return total
    
    def find_largest(self):
        largest=self.num_list[0]
        for i in self.num_list:
            if i>largest:
                largest=i
        return largest
    
    def find_smallest(self):
        smallest=self.num_list[0]
        for i in self.num_list:
            if i<smallest:
                smallest=i
        return smallest
    
    def count_even_number(self):
        count=0
        for i in self.num_list:
            if i%2==0:
                count+=1
        return count
    
    def count_odd_number(self):
        count=0
        for i in self.num_list:
            if i%2!=0:
                count+=1
        return count

numbers=[1,2,3,100,5]
obj=Lists(numbers)
print("Sum: ",obj.find_sum())
print("Largest: ",obj.find_largest())
print("Smallest: ",obj.find_smallest())
print("Even count: ",obj.count_even_number())
print("Odd Count: ",obj.count_odd_number())