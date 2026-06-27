def recommend_ai_path(available_hours):
    if available_hours < 5:
        recommendation = "ai_path"
    else :
        recommendation = "Great time! We recommend the 'Full Python & AI Basics Course' to build real projects."
        return recommendation
hours = float(input("How many hours do you have available weekly for learning?"))

result_path = recommended_ai_path(hours)
print("----Smart_path_recommendndation------")
print("Result: ",result_path)
