import sys
from simulator import *

input = sys.stdin.readline



# 변수들
MAX_ARRAY_LENGTH = 100000

current_sort_type = Sort_type.BUBBLE
array_size = 1000
shuffle = [10]
show_detail = True

# 시뮬레이터
Simul = simulator()


# 도움말 출력
def help(command):
    if len(command) == 1:
        print("사용 가능한 명령어 모음입니다\n")
        print("/title : 타이틀 화면을 출력합니다")
        print("/start : 시뮬레이션을 시작합니다")
        print("/change_alg : 사용할 정렬 알고리즘을 설정합니다")
        print("/array : 정렬할 배열의 크기를 설정합니다")
        print("/shuffle : 배열을 몇 번 섞을지 설정합니다")
        print("/detail : 시뮬레이션 도중 세부 정보 표기 유무를 설정합니다\n")
        print("명령어의 자세한 정보를 보려면 /help /start 와 같이 입력하세요")
        return
    
    
    if command[1] == "/title":
        print("/title : 타이틀 화면을 출력합니다\n현재 선택된 알고리즘, 배열 크기 등의 정보가 표기됩니다\n사용법 : /title")
    elif command[1] == "/start":
        print("/start : 정렬 시뮬레이션을 시작합니다\n선택된 옵션에서의 정렬 소모 시간을 출력합니다\n사용법 : /start")
    elif command[1] == "/change_alg":
        print("/alg : 사용할 정렬 알고리즘을 설정합니다\n사용법 : /alg 숫자\n")
        print("/0 : 버블 정렬")
        print("/1 : 선택 정렬")
        print("/2 : 병합 정렬")
        print("/3 : 힙 정렬")
    elif command[1] == "/array":
        print("/array : 정렬할 배열의 크기를 설정합니다\n배열 크기는 %d이하 자연수로만 설정할 수 있습니다" % MAX_ARRAY_LENGTH)
        print("사용법 : /array 숫자")
    elif command[1] == "/shuffle":
        print("/shuffle : 배열을 섞을 횟수를 설정합니다\n섞기 횟수는 0이상 자연수로만 설정할 수 있습니다")
        print("한 번의 섞기마다 전체 배열의 약 5%가 랜덤하게 재배치됩니다")
        print("섞는 횟수를 여러 개 지정할 경우 시뮬레이션이 여러 번 실행됩니다")
        print("사용법 : /shuffle 숫자 숫자 숫자...")
    elif command[1] == "/detail":
        print("/detail : 시뮬레이션 도중 세부 정보 표기 유무를 설정합니다\nOn일 때 정렬 알고리즘의 종류에 따라 더 많은 정보가 출력됩니다")
        print("사용법 : /detail On/Off")
    else:
        print("오류 : 해당 명령어의 설명을 찾을 수 없습니다")
        

# /title 명령어
def title():
    print("정렬 알고리즘 시뮬레이션 v1.0")
    print("제작자 : 김제율\n")
    print("현재 정렬 알고리즘 : %s" % current_sort_type.name)
    print("현재 배열 크기 : %d" % array_size)
    tmp = "["
    for i in range(len(shuffle)):
        if i != len(shuffle) - 1:
            tmp += "%d, " % shuffle[i]
        else:
            tmp += "%d]" % shuffle[i]
    print("배열 섞기 횟수 : %s" % tmp)
    tmp = "On" if show_detail else "Off"
    print("세부 정보 표기 : %s" % tmp)
    print()
    print("도움말을 보시려면 /help를 입력하세요")

# /start 명령어
def start():
    print("<현재 설정>\n")
    print("현재 정렬 알고리즘 : %s" % current_sort_type.name)
    print("현재 배열 크기 : %d" % array_size)
    tmp = "["
    for i in range(len(shuffle)):
        if i != len(shuffle) - 1:
            tmp += "%d, " % shuffle[i]
        else:
            tmp += "%d]" % shuffle[i]
    print("배열 섞기 횟수 : %s" % tmp)
    tmp = "On" if show_detail else "Off"
    print("세부 정보 표기 : %s" % tmp)
    print("="*50 + "\n")
    
    while True:
        print("시뮬레이션을 시작하시겠습니까? Y/N")
        command = input().strip()
        
        if command == "Y":
            Simul.set(current_sort_type, array_size, shuffle, show_detail)
            Simul.simualate_all()
            break
        elif command == "N":
            print("="*50)
            print("시뮬레이션이 취소되었습니다")
            return
  
# /alg 명령어
def alg(type):
    global current_sort_type
    
    
    for alg in Sort_type:
        if str(alg.value) == type:
            current_sort_type = alg
            print("사용할 알고리즘이 변경되었습니다 : %s" % alg.name)
            return
    
    print("오류 : 해당 알고리즘 번호는 지정되지 않았습니다")
    
# /array 명령어
def array(length):
    global array_size
    
    
    try:
        length = int(length)
    except:
        print("오류 : 배열 크기는 1이상 %d이하의 자연수여야 합니다" % MAX_ARRAY_LENGTH)
        return

    if 0 < length and length <= MAX_ARRAY_LENGTH:
        array_size = length
        print("배열 크기가 변경되었습니다 : %d" % length)
    else:
        print("오류 : 배열 크기는 1이상 %d이하의 자연수여야 합니다" % MAX_ARRAY_LENGTH)


# /shuffle 명령어
def shuffle_set(command : list):
    global shuffle
    
    # 검사
    for cmd in command:
        try:
            tmp = int(cmd)
            
            if tmp < 0:
               raise Exception 
        except:
            print("오류 : 부적절한 인자가 입력되었습니다\n/shuffle 명령어의 인자는 0이상 정수여야 합니다")
            return
    
    shuffle.clear()
    for cmd in command:
        shuffle.append(int(cmd))
    
    tmp = "["
    for i in range(len(shuffle)):
        if i != len(shuffle) - 1:
            tmp += "%d, " % shuffle[i]
        else:
            tmp += "%d]" % shuffle[i]
    print("배열 섞기 횟수가 변경되었습니다 : %s" % tmp)

        
    

# /detail 명령어
def detail(arg):
    global show_detail
    
    if arg == "On":
        show_detail = True
        print("세부 사항 표기 : On")
    elif arg == "Off":
        show_detail = False
        print("세부 사항 표기 : Off")
    else:
        print("오류 : 알 수 없는 인자입니다\n/detail 명령어의 인자는 \"On\" 또는 \"Off\"여야 합니다")
            


def main():
    print("="*50)
    title()
    print("="*50 + "\n")
    
    while True:
        command = input().strip().split()
        
        print("="*50)
        
        if len(command) == 0:
            print("오류 : 공백은 정의되지 않은 명령어입니다")
            print("="*50 + "\n")
            continue
        
        if command[0] == "/help":
            help(command)     
        elif command[0] == "/title":
            title()
        elif command[0] == "/start":
            start()
        elif command[0] == "/alg":
            if len(command) == 1:
                print("오류 : 인자 개수가 부족합니다")
            else:
                alg(command[1])
        elif command[0] == "/array":
            if len(command) == 1:
                print("오류 : 인자 개수가 부족합니다")
            else:
                array(command[1])
        elif command[0] == "/shuffle":
            if len(command) == 1:
                print("오류 : 인자 개수가 부족합니다")
            else:
                shuffle_set(command[1:])  
        elif command[0] == "/detail":
            if len(command) == 1:
                print("오류 : 인자 개수가 부족합니다")
            else:
                detail(command[1])
        elif command[0] == "/이스터에그":
            print("여기 사람이 갈려나가고 있어요")
        else:
            print("오류 : 정의되지 않은 명령어입니다")

        
        print("="*50 + "\n")
        
if __name__ == "__main__":
    main()