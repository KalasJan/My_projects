# Cilem je vytvorit test o 5 otazkach s vyberem ABCD. Na zaver vypocita vysledne skore

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

# otazky
question_prompts = [
     "1) Hlavní město ČR je?\n(a) Praha\n(b) Brno\n(c) Plzeň\n(d) Ostrava",
     "2) Součet úhlů trojúhelníku (ve stupních) je?\n(a) 90\n(b) 180\n(c) 270\n(d) 360",
     "3) Kolik metrů měří maraton?\n(a) 5000\n(b) 10000\n(c) 21097\n(d) 42195",
     "4) Které z následujících slov neznamená 'ne'?\n(a) no \n(b) yes\n(c) non\n(d) nět",
     "5) Která z uvedených možností není psí rasa?\n(a) Bígl\n(b) Husky\n(c) Sphynx\n(d) Retrívr"
]

# jednotlive spravne odpovedi    
questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "d"),
     Question(question_prompts[3], "b"),
     Question(question_prompts[4], "c"),
     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("Získal jsi", score, "bodů, z celkových", len(questions),"možných. Tvá procentuální úspěšnost je", int(score/len(questions) * 100), "%.")

run_quiz(questions)