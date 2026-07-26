student1 ={"name": "Lisa", "score": 100}
student2 = {"name": "Rose", "score": 99}
student3 = {"name":"Jennie", "score": 98}
student4 = {"name": "Jisoo", "score": 97}
student5 = {"name": "Yui", "score": 95}

for student in {student1, student2, student3, student4, student5}:
    print("name and score of student1:", student["name"], student["score"])
    print("name and score of student2:", student["name"], student["score"])
    print("name and score of student3:", student["name"], student["score"])
    print("name and score of student4:", student["name"], student["score"])
    print("name and score of student5:", student["name"], student["score"])
student.max_score = max(student1["score"])
student.min_score = min(student5["score"])
user_input = input("Enter a student's name to find their score: ")
print("the score of the student is:", student[user_input]["score"])