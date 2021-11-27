import string

def solution(source):
    answer = ''
    sourceList = list(source)
    dest = []
    
    while(len(sourceList) > 0):
        isAlphabetExist = [False] * 26
        
        for idx, sourceChar in enumerate(sourceList):
            alphabetIdx = string.ascii_lowercase.index(sourceChar)
            # print(sourceList)
            
            if not isAlphabetExist[alphabetIdx]:
                # print(sourceChar)
                isAlphabetExist[alphabetIdx] = True
                dest.append(sourceChar)
                sourceList[idx] = ''
                
        
        dest.sort()
        answer += "".join(dest)
        dest.clear()
        while '' in sourceList:
            sourceList.remove('')
    
    return answer

def assertCode(answer, submit):
    print("\t", "----- PASS -----" if answer == submit else "----- FAIL -----",
          "\nExpect:", answer, "\tResult:", submit)

def main():
    assertCode("cetuxee", solution("execute"))

if __name__ == '__main__':
    main()
    