# count = 0
# for s in [str(i) for i in range(1234,4322)]:
    
#     if '1'in s and '4' in s and '2' in s and '3' in s and '13' not in s and '31'not in s and s[0] !='4':
#         count += 1
#         print(s,end = '\n' if count % 5 == 0 else '\t')
    
my_list = ['aa','bb','cc','bb','bb','bb','dd']
for i in my_list[:]:    # [:]切片他的底层逻辑是浅拷贝，[::]他的底层逻辑是浅拷贝
    if i[1] == 'b':
        my_list.remove(i)
print(my_list)