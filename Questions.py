class Question:
    def __init__(self, question, answer,userAnswer):
        self.question=question
        self.answer=answer
        self.userAnswer=userAnswer
    
class QuestionsList:
    question = [Question("select the even number: a.3  b.2  c.9    d.11","b","")
                ,Question("select the odd number: a.3  b.2  c.6   d.13","a","")
                ,Question("select the biggest number: a.3  b.2  c.6   d.13","d","")
                ,Question("select the smallest number: a.8  b.0  c.-5   d.13","c","")]
 
    
