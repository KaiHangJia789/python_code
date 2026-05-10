def binnary_search(my_list,target):
    start = 0
    end = len(my_list)-1
    while start <= end:
        mid = (start+end)//2
        if my_list[mid]== target:
            return True
        
        elif target > my_list[mid]:
            start = mid+1

        else:
            end = mid-1
            
    return False

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print(binnary_search(my_list,10))
