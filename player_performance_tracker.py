def analyeze_player_performance(player_name,goals,assists):
    total_contributions = assists+goals
    return total_contributions
name = input("Enter_player_name: ")
player_goals=int(input("Enter_player_goals: "))
player_assists=int(input("Enter_player_assistant: "))
contributions = analyeze_player_performance(name,player_assists,player_goals)
print (" ----total_player_contribution----- ")
print("player",name)
print("total_contributions(goals+assists):",contributions)
