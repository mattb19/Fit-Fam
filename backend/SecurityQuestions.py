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

  def __init__(self, userId, questionString, answerString):
    self.__userId = userId
    self.__questionString = questionString #2 questions delimited via commas
    self.__answerString = answerString #2 answers delimited via commas

  def comQAndA(self, selectedQuestionNum: int, answer: str):
    return selectedQuestionNum + "," + answer