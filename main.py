# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import webbrowser
import os

import easygui

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

#if __name__ == '__main__':
    #app = Fullscreen_Example()
image1 = "image_1copy.jpeg"
image2 = "Slide2.jpeg"
image3 = "Slide3.jpeg"
image4 = "Slide4.jpeg"
image5 = "Slide5.jpeg"
image6 = "Slide6.jpeg"
image7 = "Slide7.jpeg"
image8 = "Slide8.jpeg"
image9 = "Slide9.jpeg"
image10 = "Slide10.jpeg"
return_dict = {}
user_id = "0"


def initial_instructions():
    global user_id
    user_id = easygui.enterbox("What is your subject id?", "Pacman")
    easygui.ccbox("", "Pacman", image=image1)
    easygui.ccbox("", "Pacman", image=image2)
    easygui.ccbox("", "Pacman", image=image3)
    easygui.ccbox("", "Pacman", image=image4)
    easygui.ccbox("", "Pacman", image=image5)
    easygui.ccbox("", "Pacman", image=image6)
    easygui.ccbox("", "Pacman", image=image7)
    easygui.ccbox("", "Pacman", image=image8)
    easygui.ccbox("", "Pacman", image=image9)
    easygui.ccbox("", "Pacman", image=image10)

def game_questions():
    global return_dict
    easygui.ccbox("Thank you for playing the game! This is a pilot study and we value your feedback very much! First, some questions about the game itself", "Pacman")
    if easygui.choicebox("Did the sound work well?", "Game Questions", ["Yes", "No"]) == "No":
        return_dict["Did the sound work well?"] = "No"
        easygui.enterbox("Please explain what happened with the game sound", "Game Questions")
    else:
        return_dict["Did the sound work well?"] = "Yes"
    if easygui.choicebox("Were there any glitches?", "Game Questions", ["Yes", "No"]) == "Yes":
        return_dict["Were there any glitches"] = "Yes"
        easygui.enterbox("Please explain what glitches arose", "Game Questions")
    else:
        return_dict["Were there any glitches"] = "No"
    return_dict["On a scale of 1 to 5, how engaging was the game?"] = easygui.choicebox("On a scale of 1 to 5, how engaging was the game?", "Game Questions", ["1", "2", "3", "4", "5"])
    if easygui.choicebox("Did you have a specific strategy during the game?", "Game Questions", ["Yes", "No"]) == "Yes":
        easygui.enterbox("Please explain your strategy", "Game Questions")
        return_dict["Did you have a specific strategy during the game?"] = "Yes"
    else:
        return_dict["Did you have a specific strategy during the game?"] = "No"
    return_dict["What did you experience when the ghost was close to catching you?"] = easygui.multchoicebox("What did you experience when the ghost was close to catching you? You may select multiple answers.", "Game Questions", ["Stress", "Hope", "Boredom", "Excitement", "Anxiety", "Disinterest"])
    return_dict["Did you feel stressed or nervous at all while playing this game?"] = easygui.choicebox("Did you feel stressed or nervous at all while playing this game? If so, when?", "Game Questions", ["Yes, when I got close to the ghost", "Yes when the ghost was chasing me", "Yes (other)", "No"])
    return_dict["Is there anything you would change to make the game better or run more smoothly?"] = easygui.enterbox("Is there anything you would change to make the game better or run more smoothly?")
    return_dict["Have you ever played a Pacman game before?"] = easygui.choicebox("Have you ever played a Pacman game before?", "Game Questions", ["Yes", "No"])

def research_questions():
    global return_dict
    return_dict["The following items ask about anxiety and fear. For each item, select the number for the answer that best describes your experience over the past week."] = easygui.ccbox("The following items ask about anxiety and fear. For each item, select the number for the answer that best describes your experience over the past week.", "Research Questions")
    return_dict["In the past week, how often have you felt anxious?"] = easygui.choicebox("In the past week, how often have you felt anxious?", "Research Questions", ["0 = No anxiety in the past week.", "1 = Infrequent anxiety. Felt anxious a few times", "2 = Occasional anxiety. Felt anxious as much of the time as not. It was hard to relax", "3 = Frequent anxiety. Felt anxious most of the time. It was very difficult to relax.", "4 = Constant anxiety. Felt anxious all of the time and never really relaxed."])
    return_dict["In the past week, when you have felt anxious, how intense or severe was your anxiety?"] = easygui.choicebox("In the past week, when you have felt anxious, how intense or severe was your anxiety?", "Research Questions", ["0 = Little or None: Anxiety was absent or barely noticeable", "1 = Mild: Anxiety was at a low level. It was possible to relax when I tried. Physical symptoms were only slightly uncomfortable.", "2 = Moderate: Anxiety was distressing at times. It was hard to relax or concentrate, but I could do it if I tried. Physical symptoms were uncomfortable.", "3 = Severe: Anxiety was intense much of the time. It was very difficult to relax or focus on anything else. Physical symptoms were extremely uncomfortable.", "4 = Extreme: Anxiety was overwhelming. It was impossible to relax at all. Physical symptoms were unbearable"])
    return_dict["In the past week, how often did you avoid situations, places, objects, or activities because of anxiety or fear?"] = easygui.choicebox("In the past week, how often did you avoid situations, places, objects, or activities because of anxiety or fear?", "Research Questions", ["0 = None: I do not avoid places, situations, activities, or things because of fear", "1 = Infrequent: I avoid something once in a while, but will usually face the situation or confront the object. My lifestyle is not affected.", "2 = Occasional: I have some fear of certain situations, places, or objects, but it is still manageable. My lifestyle has only changed in minor ways. I always or almost always avoid the things I fear when I’m alone, but can handle them if someone comes with me.", "3 = Frequent: I have considerable fear and really try to avoid the things that frighten me. I have made signifi cant changes in my lifestyle to avoid the object, situation, activity, or place.", "4 = All the Time: Avoiding objects, situations, activities, or places has taken over my life. My lifestyle has been extensively affected and I no longer do things that I used to enjoy"])
    return_dict["In the past week, how much did your anxiety interfere with your ability to do the things you needed to do at work, at school, or at home?"] = easygui.choicebox("In the past week, how much did your anxiety interfere with your ability to do the things you needed to do at work, at school, or at home?", "Research Questions", ["0 = None: No interference at work/home/school from anxiety", "1 = Mild: My anxiety has caused some interference at work/home/school. Things are more difficult, but everything that needs to be done is still getting done.", "2 = Moderate: My anxiety definitely interferes with tasks. Most things are still getting done, but few things are being done as well as in the past.", "3 = Severe: My anxiety has really changed my ability to get things done. Some tasks are still being done, but many things are not. My performance has definitely suffered.", "4 = Extreme: My anxiety has become incapacitating. I am unable to complete tasks and have had to leave school, have quit or been fired from my job, or have been unable to complete tasks at home and have faced consequences like bill collectors, eviction, etc."])
    return_dict["In the past week, how much has anxiety interfered with your social life and relationships?"] = easygui.choicebox("In the past week, how much has anxiety interfered with your social life and relationships?", "Research Questions", ["0 = None: My anxiety doesn’t affect my relationships.", "1 = Mild: My anxiety slightly interferes with my relationships. Some of my friendships and other relationships have suffered, but, overall, my social life is still fulfilling.", "2 = Moderate: I have experienced some interference with my social life, but I still have a few close relationships. I don’t spend as much time with others as in the past, but I still socialize sometimes.", "3 = Severe: My friendships and other relationships have suffered a lot because of anxiety. I do not enjoy social activities. I socialize very little.", "4 = Extreme: My anxiety has completely disrupted my social activities. All of my relationships have suffered or ended. My family life is extremely strained."])

def comp_questions():
    num_correct = 0
    questions = 5
    while questions > 0:
        if easygui.choicebox("How/when does a trial end?", "Comprehension Questions", ["Only when Pacman has been eaten by the ghost.", "When Pacman moves to one of the ends in the corridor or has been eaten by the ghost."]) == "When Pacman moves to one of the ends in the corridor or has been eaten by the ghost.":
            num_correct += 1
            questions -= 1
            print(num_correct)
        if easygui.choicebox("The chance that the ghost chases you is determined by", "Comprehension Questions", ["The distance between you and the ghost", "The time spent in the trial", "How many points you have earned"]) == "The distance between you and the ghost":
            num_correct += 1
            questions -= 1
            print(num_correct)
        if easygui.choicebox("True or False: I must collect all dots before exiting the trial", "Comprehension Questions", ["True", "False"]) == "False":
            num_correct += 1
            questions -= 1
            print(num_correct)
        if easygui.choicebox("When you are caught by the ghost, you lose one life and ___. ", "Comprehension Questions", ["The points you scored on that trial", "50 points", "150 points"]) == "The points you scored on that trial":
            num_correct += 1
            questions -= 1
            print(num_correct)
        if easygui.choicebox("When you lose all three lives, ___.", "Comprehension Questions", ["Your score is reset to 0 and you must begin a new game", "The experiment ends"]) == "Your score is reset to 0 and you must begin a new game":
            num_correct += 1
            questions -= 1
            print(num_correct)
        if num_correct > 2:
            easygui.ccbox("Great job! Now you will play four practice trials to help you understand the game. Try to get as high a score as you can, without being eaten by the ghost. Press continue and the practice trials will open in Chrome.", "Pacman")
            break
        else:
            easygui.ccbox("It looks like some of those questions weren't answered quite correctly. Let's try again!")
            num_correct = 0
            questions = 5

def ready_for_game():
    easygui.ccbox("When you finish the practice trials, please click continue on this window and the real trials will automatically open!", "Pacman")

def first_message():
    return "Welcome to Pacman!\n \nYou are going to play a simplified version of the game Pac-Man. This is not the classic arcade game so please read the instructions carefully and make sure you understand the game."


def second_message():
    return "At beginning of each round, Pac-Man will be placed somewhere along a horizontal corridor. Somewhere else along this corridor, a single ghost will appear. You must avoid the ghost, or you will lose one of your three lives as well as all the points you earned on that trial. When you lose all three lives, you lose the game and your score is reset to 0. You can see how many lives you have remaining by looking at the bottom center of the screen." \
           "\n\nAdditionally, there will be 5 dots of different sizes placed between you and the ghost. Your job is to use the left and right arrow keys to collect as many dots as you can. The more dots you collect, the higher your score will be. Larger dots are worth 20 points and smaller dots are worth 10 points. You can see your total score across trials by looking at the bottom left of your screen."

def third_message():
    return "Here is an example of how a typical trial would begin.\n"

def fourth_message():
    return "Importantly, as you move the Pac-Man to collect dots, you will have to move closer to the ghost. The closer you move to the ghost the higher the chance that the ghost will start to chase you.  If the ghost begins to chase you and you are caught, you will lose a life. The ghost's speed during the chase is random-- sometimes, if you move away quickly you will be able to escape, but sometimes, if you are too close, the ghost will be too fast for you to avoid.  The color of the ghost can help you understand how likely it is that the ghost will begin a chase. When the ghost is pink, the probability that the ghost will chase you is low. When the ghost is red, the probability the ghost will chase you is high. The closer you get to the ghost, the darker shade of red the ghost will be."

def fifth_message():
    return "You can exit the trial by exiting the corridor. For example, on a trial where the ghost was to the left of Pac-Man, you can exit the trial by moving the Pac-Man all the way to the right."

def sixth_message_one():
    return "If the ghost is to the right of Pac-Man, you would exit the trial by moving all the way to the left. You can exit the trial without collecting all the dots. If the remaining dots are too close to the ghost, you can exit the trial and a new trial will begin."

def sixth_message():
    return "Leaving dots can increase the chance that you will not lose all your lives, resulting in a higher score, but leaving too many dots too frequently, will also result in a lower score. To achieve the highest possible score, you need to balance the risks of being caught by the ghost and the rewards of getting as many dots as possible. \n\nYour average score across all the games you play will determine your bonus. Scores are reset every 20 trials. Therefore, the maximum score is 3000, which corresponds to a bonus of $9. If you receive a score of 500 or less, you will not receive a bonus. However, most players putting in a reasonable effort can expect to have a score higher than 1200, but less than 2700, corresponding to a bonus between $4.00 and $7.00."

def seventh_message():
    return "Finally, occasionally you will see some trials where the ghost is missing.\n\nWhen the ghost is missing, you may collect all the dots without any risk."

def eighth_message():
    return "To start the experiment, you may need to click into the box at the beginning of the experiement. At the end of the experiment, please wait a moment and the task will continue.\n\nThere will be sounds in this experiment. Please adjust the volume to your convenience now."

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initial_instructions()
    #comp_questions()
    webbrowser.open("file://" + os.path.realpath("main_practice.html"))
    ready_for_game()
    webbrowser.open("file://" + os.path.realpath("index.html"))
    game_questions()
    research_questions()
    sys.stdout = open(user_id + ".txt", "w")
    print(return_dict)
    sys.stdout.close()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
