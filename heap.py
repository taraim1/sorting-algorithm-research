# 힙 정렬에 쓸 힙을 구현해봄

class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)
        self.heap_count = 0
        
    # 부모 노드 주면 자식 노드랑 비교해서 힙으로 정렬    
    def max_heapify(self, parent):    
        left_child_i = 2*parent
        right_child_i = left_child_i + 1
        cnt = self.heap_count
        
        # 자식 노드 유무 검사
        if left_child_i <= cnt:
            is_left_exist = True
        else:
            is_left_exist = False
        
        if right_child_i <= cnt:
            is_right_exist = True
        else:
            is_right_exist = False
        
        # 위치 바꾸기
        # 자식이 없으면
        if not is_left_exist and not is_right_exist:
            return
        
        # 왼쪽 오른쪽 다 있으면
        if is_right_exist:
            if self.heap[left_child_i] >= self.heap[right_child_i]:
                if self.heap[left_child_i] >= self.heap[parent]:
                    self.heap[left_child_i], self.heap[parent] = self.heap[parent], self.heap[left_child_i]
                    self.max_heapify(left_child_i)
            else:
                if self.heap[right_child_i] >= self.heap[parent]:
                    self.heap[right_child_i], self.heap[parent] = self.heap[parent], self.heap[right_child_i]
                    self.max_heapify(right_child_i)
        
        # 왼쪽만 있으면
        else:
            if self.heap[left_child_i] >= self.heap[parent]:
                self.heap[left_child_i], self.heap[parent] = self.heap[parent], self.heap[left_child_i]
                self.max_heapify(left_child_i)

        
    # 리스트 주면 최대 힙으로 만들어줌
    def build_max_heap(self, arr : list):
        self.heap = [None]*(len(arr)+1)
        for i in range(len(arr)):
            self.heap[i+1] = arr[i]
        
        self.heap_count = len(arr)
        
        for i in range(self.heap_count//2, 0, -1):
            self.max_heapify(i)
        

        
    def remove_root(self):
        self.heap[1], self.heap[self.heap_count] = self.heap[self.heap_count], self.heap[1]
        self.heap_count -= 1
        self.max_heapify(1)
    
    def heap_sort(self):
        for _ in range(self.heap_count):
            self.remove_root()
        
