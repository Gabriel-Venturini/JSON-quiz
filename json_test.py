import json

with open("myquestions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
user_score = 0
questions_ammount = 0
# you just need to change .json file

for question in data:
    questions_ammount += 1
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer
    if question["user_answer"] == question["correct_answer"]:
        user_score += 1

print(f"You got {user_score}/{questions_ammount} answers right!")
