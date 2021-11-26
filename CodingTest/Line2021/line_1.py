def solution(inputString):
    result = 0
    openBrackets = ['(', '{', '[', '<']
    closeBrackets = [')', '}', ']', '>']
    bracketStack = []
    for idx, inputChar in enumerate(inputString):
        
        if inputChar in openBrackets:
            bracketStack.append(openBrackets.index(inputChar))
            
        if inputChar in closeBrackets:
            
            if len(bracketStack) == 0:
                return idx * -1
            
            lastOpenBracketIdx = bracketStack.pop()
            
            if closeBrackets.index(inputChar) == lastOpenBracketIdx:
                result += 1
            else:
                return idx * -1
            
    if len(bracketStack) > 0:
        return (len(inputString)-1) * -1
    
    return result

def main():
    assertCode(0, solution("Hello, world!"))
    assertCode(-14, solution("line [({<plus>)}]"))
    assertCode(-15, solution("line [({<plus>})"))
    assertCode(-8, solution("ABC({ABC)ABC"))
    assertCode(2, solution("(A)[B]"))
    assertCode(-3, solution("ABC)ABC"))
    
def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----", "\nExpect:", answer, "\tResult:", submit)

if __name__ == '__main__':
    main()
    