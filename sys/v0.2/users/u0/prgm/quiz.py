def main():
    import userlib
    import guilib as gui
    import random
    import json
    def quizQuestion(question,correct,wrong):
        if random.randint(0,1):
            return not gui.ask(question, wrong, correct)
        else:
            return gui.ask(question, correct, wrong)
    def quiz(quizQuestion,lifes,quizlist):
        points = 0
        for i in range(maxq):
            if quizQuestion(f"points: {points}\nquestion: {i}/{maxq}\n     {quizlist[i][0]}",quizlist[i][1],quizlist[i][2]):
                points += 1
            else:
                lifes -=1
                if lifes == 0:
                    gui.splash("game over, ran out of lifes!")
                    break
                gui.splash("question wrong!")
                gui.splash("lifes left:" + str(lifes))
        gui.splash("points: "+str(points))
    while 1:
        ans = gui.menu("Quiz!","Built-in","Custom","Quiz Builder","Exit")
        if ans == 1:
            quizlist = [["what is 1+1?","2","3"],["What year did the Titanic sink?","1912","1922"],["What is the name of the biggest technology company in South Korea?","samsung","LG"],["What is the world’s smallest bird?","bee hummingbird","java finch"]]
            maxq = len(quizlist)
            lifes = 1
            doQuiz = 1
            quiz(quizQuestion,lifes,quizlist)
        elif ans == 2:
            temp = userlib.user(userlib.cUser)
            quizfile = gui.file("pick quiz json",temp.getDir())
            del temp
            with open(quizfile,"r") as f:
                data = f.read()
                jsdata = json.loads(data)
                questions = jsdata["questions"]
                quizlist = []
                inMenu = 1
                doQuiz = 0
                while inMenu:
                    ans = gui.menu(str(jsdata["name"]),"stat quiz","description")
                    if ans == 1:
                        gui.splash("welcome to "+str(jsdata["name"]),1)
                        lifes = jsdata["lives"]
                        for i in range(len(questions)):
                            quizlist.append([questions[i]["question"],questions[i]["correct_answer"],questions[i]["incorrect_answer"]])
                        maxq = len(quizlist)
                        inMenu = 0
                        doQuiz = 1
                        quiz(quizQuestion,lifes,quizlist)
                    elif ans == 2:
                        gui.splash(jsdata["desc"],1)
                        gui.splash("author: "+jsdata["author"],1)
                        gui.splash("lifes: " + str(jsdata["lives"]),1)
        elif ans == 3:
            quiz = {
        "name": gui.osk("Enter a name: "),
        "questions": [
            {
                "question": gui.osk("Enter a question "),
                "correct_answer": gui.osk("Enter the correct answer "),
                "wrong_answer": gui.osk("Enter wrong answer ")
            }
        ]
    }
            addingquestion = True
            while addingquestion:
                if gui.ask("do what?","add question", "save and exit"):
                    new_question = {
            "question": gui.osk("Enter a question: "),
            "correct_answer": gui.osk("Enter the correct answer: "),
            "wrong_answer": gui.osk("Enter wrong answer: ")
                }
                    quiz["questions"].append(new_question)
                else:
                    addingquestion = False
        else:
            break
main()
