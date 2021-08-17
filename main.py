# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

import easygui
from PIL import Image

import tkinter as tk

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
image1 = "../pacman_ui/image1.png"
image2 = "../pacman_ui/image2.png"
image3 = "../pacman_ui/image3.png"
image4 = "../pacman_ui/image4.png"

def initial_instructions():
    easygui.ccbox(first_message(), "Pacman")
    easygui.ccbox(second_message(), "Pacman")
    easygui.ccbox(third_message(), "Pacman", image=image1)
    easygui.ccbox(fourth_message(), "Pacman")
    easygui.ccbox(fifth_message(), "Pacman", image=image2)
    easygui.ccbox(sixth_message_one(), "Pacman", image=image3)
    easygui.ccbox(sixth_message(), "Pacman")
    easygui.ccbox(seventh_message(), "Pacman", image=image4)
    easygui.ccbox(eighth_message(), "Pacman")

def game_questions():
    easygui.ccbox("Thank you for playing the game! This is a pilot study and we value your feedback very much! First, some questions about the game itself", "Pacman")
    if easygui.choicebox("Did the sound work well?", "Game Questions", ["Yes", "No"]) == "No":
        easygui.enterbox("Please explain what happened with the game sound", "Game Questions")
    if easygui.choicebox("Were there any glitches?", "Game Questions", ["Yes", "No"]):
        easygui.enterbox("Please explain what glitches arose", "Game Questions")
    easygui.choicebox("On a scale of 1 to 5, how engaging was the game?", "Game Questions", ["1", "2", "3", "4", "5"])
    if easygui.choicebox("Did you have a specific strategy during the game?", "Game Questions", ["Yes", "No"]) == "Yes":
        easygui.enterbox("Please explain your strategy", "Game Questions")
    easygui.multchoicebox("What did you experience when the ghost was close to catching you? You may select multiple answers.", "Game Questions", ["Stress", "Hope", "Boredom", "Excitement", "Anxiety", "Disinterest"])
    if easygui.choicebox("Did you feel stressed or nervous at all while playing this game? If so, when?", "Game Questions", ["Yes, when I got close to the ghost", "Yes when the ghost was chasing me", "Yes (other)", "No"]) == "Yes (other)":
        easygui.enterbox("When did you feel stressed or nervous?", "Game Questions")
    easygui.enterbox("Is there anything you would change to make the game better or run more smoothly?")
    easygui.choicebox("Have you ever played a Pacman game before?", "Game Questions", ["Yes", "No"])


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

def first_image():
    return Image.open("/Users/Tarun/Desktop/pacman_graphics/image1.png")

def second_image():
    return Image.open("/Users/Tarun/Desktop/pacman_graphics/image2.png")

def third_image():
    return Image.open("/Users/Tarun/Desktop/pacman_graphics/image3.png")

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
    comp_questions()
    webbrowser.open("file://" + "/Users/Tarun/pacman-task/main_practice.html")
    ready_for_game()
    webbrowser.open("file://" + "/Users/Tarun/pacman-task/index.html")
    game_questions()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
