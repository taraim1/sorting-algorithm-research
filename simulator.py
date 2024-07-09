# 시뮬레이터
from enum import Enum
import random
import time
import copy

class Sort_type(Enum):
    BUBBLE = 0
    SELECTION = 1
    MERGE = 2
    HEAP = 3

class simulator():
    sortType = Sort_type.BUBBLE
    array_size = 0
    shuffle = [100]
    show_detail = True
    time_show_limit = 7
    array = []
    
    def set(self, sortType : Sort_type, array_size : int, shuffle : list, show_detail : bool):
        self.sortType = sortType
        self.array_size = array_size
        self.shuffle = shuffle
        self.show_detail = show_detail
    
    
    # 시뮬레이션 실행
    def simualate_all(self):
        print("="*50)
        print("시뮬레이션이 시작되었습니다")
        
        for i, repeat in enumerate(self.shuffle):
            print("-"*50)
            print("시뮬레이션 %d : %d회 섞기" % (i+1, repeat))
            self.make_array(repeat)
            self.start_sort()
            print("-"*50 + "\n")
    
    # 정렬할 배열 만드는 메소드
    def make_array(self, repeat):
        self.array = [i for i in range(self.array_size)]
        
        # 섞기
        print("배열을 섞는 중... ", end="")
        
        
        for _ in range(repeat):
            # 서로 바꿀 약 5%를 고르기
            shuffle_list = [False]*self.array_size
            
            cnt = 0
            
            for i in range(self.array_size):
                rand = random.randint(1, 20)
                
                if rand == 1:
                    cnt += 1
                    shuffle_list[i] = True
            
            # 섞일 원소들의 인덱스만 따로 모은 리스트를 만글기
            tmp_list = [0]*cnt
            tmp_index = 0
            
            for i, shuffle in enumerate(shuffle_list):
                if shuffle:
                    tmp_list[tmp_index] = i
                    tmp_index += 1
            
            # 그걸 섞기
            random.shuffle(tmp_list)
            
            # 적용하기
            result_list = [0]*self.array_size
            tmp_index = 0
            for i in range(self.array_size):
                if shuffle_list[i]:
                    result_list[i] = self.array[tmp_list[tmp_index]]
                    tmp_index += 1
                else:
                    result_list[i] = self.array[i]
            self.array = copy.deepcopy(result_list)
            
            
        
        print("완료")
    
    # 정렬하는 메소드
    def start_sort(self):
        print("배열 정렬 중... ", end="")
        
        if self.sortType == Sort_type.BUBBLE:
            result = self.bubble_sort()
            print("완료\n")
            print("걸린 시간 : %s초" % str(result[0])[:self.time_show_limit])
            if self.show_detail:
                print("compariaon 횟수 : %d" % result[1])
                print("swap 횟수 : %d" % result[2])
        if self.sortType == Sort_type.SELECTION:
            result = self.selection_sort()
            print("완료\n")
            print("걸린 시간 : %s초" % str(result[0])[:self.time_show_limit])
            if self.show_detail:
                print("compariaon 횟수 : %d" % result[1])
                print("swap 횟수 : %d" % result[2])
    
    
    # 버블 정렬 (걸린 시간, comparison 횟수, swap 횟수) 리턴해줌
    def bubble_sort(self):
        comp = 0
        swap = 0
        start = time.time()
        
        for _ in range(self.array_size-1):
            is_swaped = False
            
            for i in range(self.array_size-1):
        
                
                comp += 1
                if self.array[i] > self.array[i+1]:
                    swap += 1
                    is_swaped = True
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]

            if not is_swaped:
                break
        return (time.time() - start, comp, swap)
    
    # 선택 정렬 (걸린 시간, comparison 횟수, swap 횟수) 리턴해줌
    def selection_sort(self):
        comp = 0
        swap = 0
        start = time.time()
        
        complete = True
        global min_index
        
        for i in range(self.array_size-1):
            complete = True
            min_index = 0
            min_value = self.array_size+1            
            
            for j in range(i, self.array_size-1):
                comp += 1
                if self.array[j] < min_value:
                    min_index = j
                    min_value = self.array[j]
                if self.array[j] > self.array[j+1]:
                    complete = False
            
            if complete:
                return(time.time() - start, comp, swap)
            
            if i != min_index:
                self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
                swap += 1
        
        return (time.time() - start, comp, swap)