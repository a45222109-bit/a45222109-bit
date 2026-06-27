def Check_player_fitness(running_minutes):
    if running_minutes < 60:
        evaluation = "you need to improve_stamina.best_way.super_sub"
    else:
        evaluation = "Great_stamina.you will_start_main"
        
    return evaluation

minutes = float(input("How many minutes can you run at full speed? "))

fitness_result = Check_player_fitness(minutes)

print("----your fitness----")
print("evaluation:", fitness_result)
