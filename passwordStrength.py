#password checker
import tkinter

#test-complete
def checkPasswordLength(password: str) -> bool:
    if len(password) >= 12:
        return True
    else:
        return False

#test-complete      
def hasNumber(password: str) -> bool:
    for ch in password:
        if (ord(ch) >= 48 and ord(ch) <= 57):
            return True
    return False

#test-complete
def hasUppercase(password: str) -> bool:
    for ch in password:
        if (ord(ch) >= 65 and ord(ch) <= 90):
            return True
    return False

#test-complete
def hasLowerCase(password: str) -> bool:
    for ch in password:
        if ord(ch) >= 97 and ord(ch) <=122:
            return True
    return False

#test-complete
def hasConsecutiveChars(password: str) -> bool:
    for i in range(len(password) - 2):
        if (ord(password[i]) == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2])):
            return True
    return False

#test-complete
def hasRepetativeChars(password: str) -> bool:
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False

#test-complete
def hasSpecialCharacter(password: str) -> bool:
    for ch in password:
        if not ch.isalnum():
            return True
    return False



window = tkinter.Tk()
window.title('Password Strength')
window.geometry("500x500")
pLabel = tkinter.Label(window, text="Password: ")
pLabel.grid(row=0, column=1)
pEntry = tkinter.Entry(window)
pEntry.grid(row=0, column=2)
checkButton = tkinter.Button(window, text='Check password', width=25, command=lambda: testAll(pEntry.get()))
checkButton.grid(row=1, column=2)

#results
pLenghtLabel = tkinter.Label(window, text="Password Length Good: ")
pLenghtLabel.grid(row = 2, column=1)
hasNumberLabel = tkinter.Label(window, text="Contains Numbers: ")
hasNumberLabel.grid(row = 3, column=1)
hasUppercaseLabel = tkinter.Label(window, text="Contains uppercase chars: ")
hasUppercaseLabel.grid(row = 4, column=1)
hasLowerCaseLabel = tkinter.Label(window, text="Contains lowercase chars: ")
hasLowerCaseLabel.grid(row = 5, column=1)
hasConsecutiveLabel = tkinter.Label(window, text="Contains consecutive chars: ")
hasConsecutiveLabel.grid(row = 6, column=1)
hasRepetativeLabel = tkinter.Label(window, text="Contains repetative chars: ")
hasRepetativeLabel.grid(row = 7, column=1)
hasSpecialLabel = tkinter.Label(window, text="Contains special chars: ")
hasSpecialLabel.grid(row = 8, column=1)

pLengthLabelResult = tkinter.Label(window, text="")
pLengthLabelResult.grid(row = 2, column=2)
hasNumberLabelResult = tkinter.Label(window, text="")
hasNumberLabelResult.grid(row = 3, column=2)
hasUppercaseLabelResult = tkinter.Label(window, text="")
hasUppercaseLabelResult.grid(row = 4, column=2)
hasLowerCaseLabelResult = tkinter.Label(window, text="")
hasLowerCaseLabelResult.grid(row = 5, column=2)
hasConsecutiveLabelResult = tkinter.Label(window, text="")
hasConsecutiveLabelResult.grid(row = 6, column=2)
hasRepetitiveLabelResult = tkinter.Label(window, text="")
hasRepetitiveLabelResult.grid(row = 7, column=2)
hasSpecialLabelResult = tkinter.Label(window, text="")
hasSpecialLabelResult.grid(row = 8, column=2)

def testAll(password: str) -> None:
    pLengthLabelResult.config(text=str(checkPasswordLength(password)))
    hasNumberLabelResult.config(text=str(hasNumber(password)))
    hasUppercaseLabelResult.config(text=str(hasUppercase(password)))
    hasLowerCaseLabelResult.config(text=str(hasLowerCase(password)))
    hasConsecutiveLabelResult.config(text=str(hasConsecutiveChars(password)))
    hasRepetitiveLabelResult.config(text=str(hasRepetativeChars(password)))
    hasSpecialLabelResult.config(text=str(hasSpecialCharacter(password)))

window.mainloop()