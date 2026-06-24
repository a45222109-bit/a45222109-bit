def calculate_percentage(your_score, total_score):
    percentage = (your_score / total_score)*100
    return percentage
my_score = float(input("Enter_your_total_score:"))
max_score = float(input("Enter_max_score:"))
result = calculate_percentage(my_score,max_score)
print ("-----final result-----")
print("your_score_is",result," \ ")
