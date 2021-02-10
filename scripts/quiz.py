#!/usr/bin/python
from Question import Question

question_prompts = [
            "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
            "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
            "What color are Straberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
            "What color are Oranges?\n(a) Orange\n(b) Red\n(c) Blue\n\n",
            "What color are Grapes ?\n(a) Orange\n(b) Purple\n(c) Blue\n\n",
            "What color are Pamgrenet?\n(a) Orange\n(b) Red\n(c) Red\n\n",
            "What color are Pear?\n(a) Orange\n(b) Green\n(c) Blue\n\n",
            "What color are Melon?\n(a) Green\n(b) Red\n(c) Blue\n\n"
]

questions = [
           Question(question_prompts[0], "a"),
           Question(question_prompts[1], "c"),
           Question(question_prompts[2], "b"),
           Question(question_prompts[3], "a"),
           Question(question_prompts[4], "b"),
           Question(question_prompts[5], "b"),
           Question(question_prompts[6], "b"),
           Question(question_prompts[7], "a"),
]
def run_test(questions):
      score = 0
      for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
             score += 1
      print("You got  " + str(score) + " / " + str(len(questions)) + "  correct")

run_test(questions)            
