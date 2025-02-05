from quizFx import init_quiz
from quizFx import print_quiz 
from quizFx import play_quiz
from quizFx import quiz_add


selection = int(input(""" 
                *****************  PYTHON QUIZ V 1.0  *************************** 
                *                                                               * 
                *  Digit 1 and press enter to start a test                      * 
                *  Digit 2 and press enter to print a paper test                * 
                *  Digit 3 to add questions to the test database                * 
                *                                                               * 
                *****************************************************************\n
                """
                ))

if selection == 1:
    txt_file = init_quiz()  # read the Q&A file

    lenght = len(txt_file)  # read the file lenght
    answers = txt_file [lenght // 2 : lenght]  # extrapolate answers the second half of the file
    questions = txt_file [0 : lenght // 2]     # extrapolate questions from first half of the file

    play_quiz (questions,answers,lenght)

if selection == 2:
    txt_file = init_quiz()  # read the Q&A file

    lenght = len(txt_file)  # read the file lenght
 
    questions = txt_file [0 : lenght // 2]     # extrapolate questions from first half of the file

    print_quiz(questions)

if selection == 3:
   quiz_add()
       