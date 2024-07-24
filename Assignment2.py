n = int(input("Total number of students: "))

cric = []
badm = []
foot = []
countc = 0
countb = 0
countf = 0 

a = int(input("Number of students who play cricket: "))
while a > 0:
    num_c = int(input("Enter the roll number of a student who plays cricket: "))
    cric.append(num_c)
    a -= 1

b = int(input("Number of students who play badminton: "))
while b > 0:
    num_b = int(input("Enter the roll number of a student who plays badminton: "))
    badm.append(num_b)
    b -= 1

c = int(input("Number of students who play football: "))
while c > 0:
    num_f = int(input("Enter the roll number of a student who plays football: "))
    foot.append(num_f)
    c -= 1

both_play = []
for roll_no in cric:
    if roll_no in badm:
        both_play.append(roll_no)

print("Students who play both cricket and badminton:", both_play)
either_play = []
play=[]
for roll_no in cric:
    if roll_no not in badm:
        either_play.append(roll_no)
        countc+=1

for roll_no in badm:
    if roll_no not in cric:
        either_play.append(roll_no)
        countb+=1
for roll_no in foot:
        if roll_no not in badm:
         either_play.append(roll_no)
         countf+=1

print("Students who play either cricket or badminton but not both:", either_play)
print("Number of student who play neither cricket nor badminton : ", n-(countc-countb))
print("Number of student who play cricket and football but not badminton:",countc+countb)

played_any_game = []

played_any_game.extend(cric)
played_any_game.extend(badm)
played_any_game.extend(foot)

played_any_game = list(set(played_any_game))

no_game_students = n - len(played_any_game)

print("Number of students who do not play any game:", no_game_students)
print("List of student who played any game",played_any_game )

all_games_players = []
for roll_no in cric:
    if roll_no in badm and roll_no in foot:
        all_games_players.append(roll_no)
    
print("List of Students who play all three games (cricket, badminton, and football):", all_games_players)