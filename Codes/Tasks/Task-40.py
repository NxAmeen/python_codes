# Original list of tuples
subject_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list by the second element (the scores) using a lambda function
sorted_subject_scores = sorted(subject_scores, key=lambda x: x[1])

# Print the sorted list
print("Sorted list of tuples:", sorted_subject_scores)
