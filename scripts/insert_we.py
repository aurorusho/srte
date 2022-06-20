import re
from written_expression.models import (
    WrittenExpressionQuestions as WE_Questions,
    WrittenExpressionAns as WE_Ans,
    WrittenExpressionCorrectAns as WE_Corans,
)


def get_abcd(we_question):
    lst = []
    for i in range(4):
        ans = (re.findall(r'_[\S]+_', we_question))[i]
        ans = ans.replace('#',' ').replace('_','')
        lst += [ans]
    return lst


def join2lines(text) -> list:
    split_text = text.split('\n')
    lst = []
    for i in range(0, len(split_text), 2):
        item = '\n'.join(split_text[i : i + 2])
        lst.append(item)
    return lst

wriexp_txt = 'scripts/wriexp.txt'

def run():
    # Read the file
    with open(wriexp_txt, 'r', encoding='utf8') as f:
        # Get the different questions and their answers
        splited_text = join2lines(f.read())
        
        for i in splited_text:
            question, answer = i.split('\n')
            a, b, c, d = get_abcd(question)

            # Django code starts here

            # Correct anwer
            we_corans = WE_Corans(answer = answer)
            we_corans.save()
            # Answers
            we_ans = WE_Ans(a = a, b = b, c = c, d = d, correct = we_corans)
            we_ans.save()
            # Question
            we_questions = WE_Questions(question = question, answers = we_ans)
            we_questions.save()