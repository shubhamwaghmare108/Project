# Voter Machine Code

# Voter Input
session = False
session_input = int(input('>>> Choose [1 To Start, 0 To Stop]:\n'))
session = True if session_input == 1 else False

if session:
    User_Name = 'abc'
    password = '123'
    print("!!!Greeting Operator!!!\n>>> Login into the system with user credentials.")
    inp_user_name = input('>>> Enter User Name:\n')
    inp_password = input('>>> Enter Password:\n')
    if User_Name == inp_user_name and password == inp_password:
        print('You have logged in successfully.')
    else:
        print('Invalid credentials. Exiting...')
        session = False

# Initialize Global Variables
Result = {'Cand1': 0, 'Cand2': 0, 'Cand3': 0, 'Cand4': 0}
Choice_list = {1: 'Cand1', 2: 'Cand2', 3: 'Cand3', 4: 'Cand4'}

# Cast Vote Function
def cast_vote_func():
    print('Greeting Voter, Please Cast Your Vote!')
    print("To cast your vote, press the button in front of the candidate's name.")
    print('Candidate Name\tButton')
    for i in Choice_list.keys():
        print(Choice_list[i], '\t\t', i)
    try:
        User_Input = int(input('>>> Please enter the Candidate Code to cast your choice:\n'))
        if 1 <= User_Input <= 4:
            Result[Choice_list[User_Input]] += 1
            print('Thank you for casting your vote.')
            print('You chose:', Choice_list[User_Input])
        else:
            print('Warning: Invalid input. Please choose between 1 to 4.')
    except ValueError:
        print('Error: Please enter a valid number.')
# Summary Result
def summary():
    print('Summary for session:')
    print('Candidate Name\tVote Count')
    for i in Result.keys():
        print(i, '\t\t', Result[i])
    print('Summary retrived Successfuly.')

# Summary Result with Winner Announcement
def result_summary():
    print('Result count for session:')
    print('Candidate Name\tVote Count')
    for candidate, votes in Result.items():
        print(candidate, '\t\t', votes)
    
    # Determine the winner
    max_votes = max(Result.values())
    winners = [candidate for candidate, votes in Result.items() if votes == max_votes]
    
    if len(winners) == 1:
        print('The winner is:', winners[0])
    else:
        print('It\'s a tie between:', ', '.join(winners))
    print('Summary retrieved successfully.')



# Reset Function
def reset_function():
    correct_passkey = "admin123"
    passkey=input('>>> Enter passkey:\n')
    if passkey==correct_passkey:
        global Result
        Result = {'Cand1': 0, 'Cand2': 0, 'Cand3': 0, 'Cand4': 0}
        for i in Result.keys():
            print(i, '\t\t', Result[i])
        print('Vote count have been reset Successfuly.')

# Operator Control
operations = {1: cast_vote_func, 2: summary, 3: result_summary ,4: reset_function}

while session:
    try:
        Operator_input = int(input('Please choose an operation:\n[1 for vote cast, 2 for summary, 3 for result_summary, 4 for reset, 0 to exit]:\n'))
        if Operator_input in operations:
            operations[Operator_input]()
        elif Operator_input == 0:
            print('Exiting session...')
            session = False
        else:
            print('Invalid operation. Please choose a valid option.')
    except ValueError:
        print('Error: Please enter a valid number.')


