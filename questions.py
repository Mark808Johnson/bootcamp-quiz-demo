
import random

num_questions = 3
quiz_data = [
        {
            "q_id": 1,
            "question": "In which continent are Chile, Argentina and Brazil?",
            "options": ["North America", "South America", "Europe"],
            "answer": "South America"
        },
        {
            "q_id": 2,
            "question": "Which brand of soup featured in one of Andy Warhol's most famous pop art pieces?",
            "options": ["Heinz", "Campbell's", "Baxters"],
            "answer": "Campbell's"

        },
        {
            "q_id": 3,
            "question": "The Mad Hatter and the Cheshire Cat are characters in which famous book?",
            "options": ["Winne-the-Pooh", "Charlotte's Web", "Alice in Wonderland"],
            "answer": "Alice in Wonderland"
        },
        {
            "q_id": 4,
            "question": "What measurement scale is used to determine wind speed?",
            "options": ["Beaufort scale", "Richter scale", "Synoptic scale"],
            "answer": "Beaufort scale"
        },
        {
            "q_id": 5,
            "question": "In which city were the 1992 Summer Olympics held?",
            "options": ["Seoul", "Sydney", "Barcelona"],
            "answer": "Barcelona"
        }
    ]
    
def gen_quiz_data(data, num):
    """
    Produces random sample of data to be used in quiz
    """
    random.shuffle(data)
    selected_data = data[0:num]
    return selected_data

selected_quiz = gen_quiz_data(quiz_data, num_questions)