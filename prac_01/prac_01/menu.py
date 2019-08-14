userName=str(input("Enter name: "))
print("(H)ello"+'\n'+"(G)oodbye"+'\n'+"(Q)uit"+'\n')
menuChoice=str.upper(input())
while not(menuChoice=="Q" ):
    if menuChoice=="H":
        print(f'Hello {userName}')
    elif menuChoice=="G":
        print(f'Goodbye {userName}')
    else:
        print("Invalid choice")
    print("(H)ello" + '\n' + "(G)oodbye" + '\n' + "(Q)uit" + '\n')
    menuChoose = str.upper(input())
print("Finished")