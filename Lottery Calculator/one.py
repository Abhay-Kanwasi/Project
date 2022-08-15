def factorial(n):
    fact=1
    while(n>1):
        fact=fact*n
        n=n-1
    return fact
 
def combinations(n,k):
    num = factorial(n)
    den = factorial(k) * factorial(n-k)
    return num / den
 
def comb_ways(a,total_num,num_choices):
    num=factorial(num_choices)*factorial(total_num-num_choices)
    den=factorial(a)*factorial(num_choices-a)*factorial((total_num-num_choices)-(num_choices-a))*factorial(num_choices-a)
    return num/den
 
def one_ticket_probability(total_num,tickets,num_choices,num_joker,match_num,joker_ball=False):
    outcome_numbers=combinations(total_num, num_choices)
    successful_outcome = tickets
    if joker_ball==True:
        outcome_jokerBall = num_joker
    else :
        outcome_jokerBall = (num_joker)/(num_joker-1)
    total_outcomes = (outcome_numbers / comb_ways(match_num, total_num, num_choices)) * outcome_jokerBall
    probability_winning = (successful_outcome / total_outcomes)
    print("You're chances of winning are {:.18f}".format(probability_winning))
    print("You're chances of winning are 1 in {}".format(
        total_outcomes/successful_outcome))
    return probability_winning, (total_outcomes / successful_outcome)
 
 
total_numbers=50#Range
number_choices=6 #Number of choices
total_jokerBalls=5 #Number of joker balls
match_numbers=6 #Countr of matched numbers
Joker_present=True #Presence of joker ball
tickets=1 #Total number of tickets bought
 
for match_numbers in range(match_numbers+1):
    if(Joker_present):
        print("Joker Ball matches-",end=" ")
    else:
        print("Joker Ball does not match-",end=" ")
    print("Count of Numbers that matched the winning numbers = {}".format(match_numbers))
    one_ticket_probability(total_numbers,tickets,number_choices,total_jokerBalls,match_numbers,Joker_present)

#First we define a new function that calculates
#the probabilities and also gives results in a message box
 
import tkinter as tk
from tkinter import messagebox
 
def Calculate(entries):
    cal = one_ticket_probability(int(entries['Total Number'].get()),
                                 int(entries['Tickets bought'].get()),
                                 int(entries['Choices given'].get()),
                                 int(entries['total_jokerballs'].get()),
                                 int(entries['Match balls'].get()), v.get())
    messagebox.showinfo(
        "For the selected choices ",
        "\nYou're chances of winning are {:.18f} \nYou're chances of winning are 1 in {}\n"
        .format(cal[0], cal[1]))
 
#We use tkinter to make a window object
root = tk.Tk()
#we make a form for user to give his values
def makeform(root, fields):
    entries = {}
    #These are default values for lotto-india
    default_vals=['50','6','5','6','1']
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0,default_vals[fields.index(field)])
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[field] = ent
    return entries
 
 
fields = [
    'Total Number', 'Choices given', 'total_jokerballs', 'Match balls',
     'Tickets bought'
]
ents = makeform(root, fields)
v = tk.IntVar()
 
tk.Label(root,
         text="Jokeball matches",
         justify=tk.CENTER,
         padx=20).pack()
tk.Radiobutton(root, text="Matches", padx=20, variable=v,
               value=True).pack(anchor=tk.CENTER)
tk.Radiobutton(root, text="Not matches", padx=20, variable=v,
               value=False).pack(anchor=tk.CENTER)
b1 = tk.Button(root, text='Calculate Odds',
           command=(lambda e=ents: Calculate(e)))
b1.pack(side=tk.LEFT, padx=5, pady=5)
b3 = tk.Button(root, text='Quit', command=root.quit)
b3.pack(side=tk.LEFT, padx=5, pady=5)
text2 = tk.Text(root, height=20, width=60)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
text2.insert(tk.END, '\nLottery Prediction\n', 'big')
quote = """
Total Number : Totals numbers in range from which numbers are to be chosen e.g. for range 1-49, Total number = 50 
Choices given : Number of numbers we can select excluding the joker ball
Total Jokerballs : Total number of jokerballs from which one ball is to be chosen
Match balls: For how many matches you want to calculate probability
Tickets : Number of Tickets bought
Jokerball matches : Keep True if you want to calculate the probability of jokerball matching too
"""
text2.insert(tk.END, quote, 'color')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()