def sum_of_number(sub1,sub2,sub3,sub4,sub5):
    return sub1+sub2+sub3+sub4+sub5

def max_score():
    return 500


sub1=int(input("Enter a score of english: "))
sub2=int(input("Enter a score of science: "))
sub3=int(input("Enter a score of social: "))
sub4=int(input("Enter a score of math: "))
sub5=int(input("Enter a score of nepali: "))

total_obtained = sum_of_number(sub1, sub2, sub3, sub4, sub5)
percentage=(total_obtained/max_score())*100


print(f"The student got {round(percentage, 2)}% in exam")
    
    
    
    
    


