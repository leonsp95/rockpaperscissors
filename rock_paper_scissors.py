varLives = 5
varScore = 0
drew = 0
varCompLives = 8
import msvcrt, random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#logo
print("             ____  ____  ________ __")
print("            / __ \/ __ \/ ____/ //_/")
print("           / /_/ / / / / /   /   ,<   ")
print("          / _, _/ /_/ / /___/ /| |_ ")
print("         /_/ |_|\____/\____/_/ |_( )")
print("                                 |/ ")
print("       ____  ___    ____  __________     ___   ")
print("      / __ \/   |  / __ \/ ____/ __ \   ( _ )  ")
print("     / /_/ / /| | / /_/ / __/ / /_/ /  / __ \/|")
print("    / ____/ ___ |/ ____/ /___/ _, _/  / /_/  < ")
print("   /_/   /_/  |_/_/   /_____/_/ |_|   \____/\/ ")
print("                                               ")
print("   _____ ____________________ ____  ____  _____ __")
print("  / ___// ____/  _/ ___/ ___// __ \/ __ \/ ___// /")
print("  \__ \/ /    / / \__  \__ \/ / / / /_/ /\__ \/ / ")
print(" ___/ / /____/ / ___/ /__/ / /_/ / _, _/___/ /_/  ")
print("/____/\____/___//____/____/\____/_/ |_|/____(_)   ")
print("")
print("---------------------------------------------------")
print(f"{bcolors.WARNING}Rock, Paper, Scissors\n(C)2021 Made by Leon\nVisit me at: github.com/leonsp95{bcolors.ENDC}")
print("---------------------------------------------------")
print(f"{bcolors.WARNING}RULES:\nYou start with", varLives, f"lives;\nIf you win, you get one point;\nIf you fail, you lose a life;{bcolors.ENDC}")
print("---------------------------------------------------")
print(f"{bcolors.WARNING}Type 'score' anytime to check how many points and lives left you have;\nType 'exit' to quit the game.\nGood luck!{bcolors.ENDC}")
print("---------------------------------------------------\n")
#game
while True:
    rps = input("Rock, Paper or Scissors? ").lower()
    computer = ("rock", "paper", "scissors")
    computer = random.choice(computer)
    #win
    if (rps == "rock" and computer == "paper") or (rps == "paper" and computer == "scissors") or (rps =="scissors" and computer == "rock"):
        print(f"{bcolors.FAIL}The computer chose", computer,f". You lose.\n{bcolors.ENDC}")
        varLives -=1
    #lose
    if (rps == "rock" and computer == "scissors") or (rps == "paper" and computer == "rock") or (rps == "scissors" and computer == "paper"):
        print(f"{bcolors.GREEN}The computer chose", computer, f". You win!\n{bcolors.ENDC}")
        varScore +=1
    #draw
    if (rps == computer):
        print("It's a tie! You both chose", rps,"!\n")
        drew +=1
    if (rps == "score"):
        print("You have", varLives, "lives.\nYour score is:", varScore)
    if varLives == 0:
        print("You have run out of lives.\nYour score:",varScore,"\nYou drew",drew,"times.\nPress 'e' to exit.")
        varLives = 5
        varScore = 0
        drew = 0
        varCompLives = 5
        char = msvcrt.getch()
        if char == b"e":
            break
        else:
            print("")
    if(rps == "exit"):
        print("Are you sure you want to quit?\nPress 'e' again to exit.")
        quitChar = msvcrt.getch()
        if quitChar == b"e":
            break