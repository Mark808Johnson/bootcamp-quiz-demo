
import random

def random_questions(num):
    quiz_questions = [
        {
            "question": "In which continent are Chile, Argentina and Brazil?",
            "options": ["North America", "South America", "Europe"],
            "answer": "South America"
        },
        {
            "question": "Which brand of soup featured in one of Andy Warhol's most famous pop art pieces?",
            "options": ["Heinz", "Campbell's", "Baxters"],
            "answer": "Campbell's"

        },
        {
            "question": "The Mad Hatter and the Cheshire Cat are characters in which famous book?",
            "options": ["Winne-the-Pooh", "Charlotte's Web", "Alice in Wonderland"],
            "answer": "Alice in Wonderland"
        },
        {
            "question": "What measurement scale is used to determine wind speed?",
            "options": ["Beaufort scale", "Richter scale", "Synoptic scale"],
            "answer": "Beaufort scale"
        },
        {
            "question": "In which city were the 1992 Summer Olympics held?",
            "options": ["Seoul", "Sydney", "Barcelona"],
            "answer": "Barcelona"
        }
    ]
    random.shuffle(quiz_questions)
    return quiz_questions[0:num]
