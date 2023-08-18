#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    TotalWeight = 0
    TotalScore = 0
    if len(my_list) <= 0:
        return 0
    for item in my_list:
        score, weight = item
        TotalWeight = TotalWeight + weight
        TotalScore = TotalScore + score * weight
    return TotalScore / TotalWeight
    
