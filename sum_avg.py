def calculate_scores(scores):
    # Calculate sum of scores
    total = sum(scores)
    # Calculate average of scores
    average = total / len(scores)
    return total, average
# Main program
scores_list = [85, 90, 78, 92, 88]
total, avg = calculate_scores(scores_list)
print("Scores:", scores_list)
print("Sum of scores:", total)
print("Average of scores:",avg)