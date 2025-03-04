questions = [
    ["What is the capital of India?", ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"], "A"],
    ["Who is the founder of Microsoft?", ["A. Bill Gates", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "A"],
    ["Who is the founder of Google?", ["A. Bill Gates", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "C"],
    ["Who is the founder of Apple?", ["A. Bill Gates", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "B"],
    ["Who is the founder of Amazon?", ["A. Jeff Bezos", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "A"],
    ["Who is the founder of Facebook?", ["A. Bill Gates", "B. Mark Zuckerberg", "C. Larry Page", "D. Steve Jobs"], "B"],
    ["Who is the founder of Twitter?", ["A. Jack Dorsey", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "A"],
    ["Who is the founder of Instagram?", ["A. Kevin Systrom", "B. Steve Jobs", "C. Larry Page", "D. Mark Zuckerberg"], "A"]
]

prizes = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000]
final_amount = 0

def kbc_game():
    print("Welcome to Kaun Banega Crorepati (KBC)!\n")
    
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i][0]}")
        
        for option in questions[i][1]:
            print(option)
        
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == questions[i][2]:
            final_amount = prizes[i]
            print(f"Correct! You have won PKR{final_amount}\n")
        else:
            print("Wrong answer! Game Over.")
            break
    
    print(f"You are taking home PKR{final_amount}. Thanks for playing!")

kbc_game()
