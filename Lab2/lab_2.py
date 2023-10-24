import matplotlib.pyplot as plt

red = "\u001b[41m   \u001b[0m"
white = "\u001b[7m   \u001b[0m"
blue = "\u001b[48;5;18m   \u001b[0m"
flag = str(input("List of available country flags: Netherlands \n\nPlease write the name of the country to print it\'s flag \nPrint the flag of:"))

space = "\u001b[40m "
square = "\u001b[48;5;28m "
end_color = "\u001b[0m"

#(1)
def print_flag(): 
 if flag == "Netherlands":
  print("\n")
  print(red*6) 
  print(red*6)
  print(white*6)
  print(white*6)
  print(blue*6)
  print(blue*6)
  print("\n")
 else:
     print("\nCountry not found! \nPlease insert the name of an available country\n")

print_flag() #add the thing of try again

#(2)
print(square,space*5,square,space*5,square,end_color)
print(space,square,space,square,space,square,space,square,space,end_color)
print(space*3,square,space*5,square,space*3)
print(space,square,space,square,space,square,space,square,space,end_color)
print(square,space*5,square,space*5,square,end_color)
print("\n")

#(3)
green = "\u001b[38;5;28m"
plot_point = f'{green}+{end_color}'

for i in range(10):
    print(f'{" "*(i>5)}{20 - 2*i}{" . "*((9 - i)//2)}{f" {plot_point} " if (i%2 == 0) else " . "}{" . "*((10 + i)//2)}')
print(" 0 2  4  6  8 10 12 14 16 18 20")
print("\n")

#(4)
with open("sequence.txt") as file:
    lines = file.readlines()
    list_numbers = [float (i) for i in lines]
    #print(list_numbers)
    num_lines = len(list_numbers)
    sum_all_numbers = sum(list_numbers)
    
    def Sum_Even_Odd_num (a, num_lines):
        even = 0
        odd = 0
        
        for i in range(num_lines):
            if i % 2 == 0:
                even += a[i]
            else:
                odd =+ a[i]
        
        relation_odd_total = (odd*-1)/sum_all_numbers
        relation_even_total = even/sum_all_numbers
        percentage_odd = f"{relation_odd_total:0%}"
        percentage_even = f"{relation_even_total:0%}"
                
        print("Sum of numbers in even rows:", even)
        print("Sum of numbers in odd rows:", odd)
        print("Sum of all the numbers in list:", sum_all_numbers)
        print("\n")
        print("Percentage of odd:", percentage_odd)
        print("Percentage of even:", percentage_even)
        
        left = [1,2]
        height = [percentage_odd, percentage_even]
        tick_label = ["'%' sum of n in odd rows", "'%' sum of n in even rows"]
    
        plt.bar(left, height, tick_label = tick_label, width = 1, color = ["red", "green"])
        plt.xlabel("Percentage with respect to the sum of all n in the list")
        plt.ylabel("Percentage")
        plt.title("Percentage of the sum of numbers located in even and odd rows")
        plt.show()
       
    Sum_Even_Odd_num(list_numbers, num_lines)

    
            
    
    
        
        
                
            
        
    






