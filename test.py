import regex as re
def worldGen(size):
    blanks = '[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0]'
    with open("worldGen.txt","a") as f:
        print('works')
        if size == 'small':
            for i in range(20):
                f.write(f'{blanks}\n')               
            f.close()

if __name__ == '__main__':
    aList = []
    with open("worldGen.txt","r+") as f:
        line = f.readline()
        cnt = 1
        for i in range(20):
            print("Line {}: {}".format(cnt, line.strip()))
            aList.append(line)
            line = f.readline()
            cnt += 1
    
    print(aList)