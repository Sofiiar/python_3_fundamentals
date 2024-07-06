def assign_rating(input):
    if 0 <= input < 580:
        output_rating = "Poor"
    elif 580 <= input < 670:
        output_rating = "Fair"
    elif 670 <= input < 740:
        output_rating = "Good"
    elif 740 <= input < 800:
        output_rating = "Very Good"
    elif 800 <= input <= 850:
        output_rating = "Excellent"
    else:
        output_rating = "Invalid score"
    return output_rating


score = 760
rating = assign_rating(score)
print(rating)  # Output: Very Good

score = 675
rating = assign_rating(score)
print(rating)  # Output: Good

score = 850
rating = assign_rating(score)
print(rating)  # Output: Excellent

score = 900
rating = assign_rating(score)
print(rating)  # Output: Invalid score
