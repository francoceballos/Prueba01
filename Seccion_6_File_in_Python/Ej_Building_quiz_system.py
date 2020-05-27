"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:


fd_question = open('questions.txt', 'r')
list_qa = fd_question.readlines()
fd_question.close()

n_answer = 0

for row in list_qa:
    question, result=row.strip().split('=')
    answer = int(input(question+'='))

    if (answer==int(result)):
        n_answer+=1


fd_result = open('result.txt', 'w')
fd_result.write("Your final score is "+ str(n_answer) + "/" +str(len(list_qa))+".")
fd_result.close()

#print(f"Your final score is {n_answer}/{len(list_qa)}.")