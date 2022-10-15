class SecurityQuestions:
  question1 = "In what city were you born?"
  question2 = "What is the name of your favorite pet?"
  question3 = "What is your mother's maiden name?"
  question4 = "What high school did you attend?"
  question5 = "What was the name of your elementary school?"
  question6 = "What was the make of your first car?"
  question7 = "What was your favorite food as a child?"
  question8 = "Where did you meet your spouse?"
  question9 = "What year was your father (or mother) born?"
  questionList = [question1, question2, question3, question4, question5, question6, question7, question8, question9]

  def __init__(self, userId, questionStringA, questionStringB, answerStringA, answerStringB):
    self.__userId = userId
    self.__questionString = self.combineAandB(questionStringA,questionStringB) #2 questions delimited via commas
    self.__answerString = self.combineAandB(answerStringA,answerStringB) #2 answers delimited via commas
    self.sendDataToSQL(questionString)
    self.sendDataToSQL(answerString)

  def sendDataToSQL(data: str):
    return  #temp for when I get with someone to send data to the SQL server

  def combineAandB(stringA: str, stringB: str):
    return stringA + "," + stringB

for i in range(0, len(SecurityQuestions.questionList)):
  answer = SecurityQuestions.questionList[i]
  print(SecurityQuestions.combineAandB(str(i) , answer))