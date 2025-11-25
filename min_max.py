def process_scores(scores):
    # Calculate sum, average, min, and max
    total = sum(scores)
    average = total / len(scores)
    minimum = min(scores)
    maximum = max(scores)
    return total, average, minimum, maximum
# Main program
scores_list = [80, 95, 70, 88, 92]
total, avg, min_score, max_score = process_scores(scores_list)
print("Scores:", scores_list)
print("Sum of scores:", total)
print("Average score:", avg)
print("Minimum score:", min_score)
print("Maximum score:", max_score)