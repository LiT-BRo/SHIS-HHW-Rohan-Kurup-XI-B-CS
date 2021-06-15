import random
turns, score = [], []

def retry(score, turns):
    opt = (input("Want to play more? (y/n) => "))  

    if opt == "y":
        game()
    else :
        sumt = str(sum(turns)) # sumt = sum_turns
        sums = str(sum(score)) # sums = sum_score
        print("\nNice try! Your score is =", sums+"/"+sumt)
        print("======= Thanks for playing LiTBRo's Square Game =======")
        exit()

def game():
    n1 = random.randint(0, 10)
    ans = square(n1**2)
    print("\nWhat is the square of", str(n1)+"?")
    user = int(input("==> "))
    a = 1
    turns.append(a)

    if user == ans:
        print("\nCongrats! Right answer\n")
        b = 1
        score.append(b)
        retry(score, turns)

    elif user != ans:
        print("\nBuzzz! Wrong answer... The correct answer is = ", ans, '\n')
        retry(score, turns)

print("\n======= Welcome to LiTBRo's Square Game! =======\n")
print("Let's check how good your math is!")
game()
