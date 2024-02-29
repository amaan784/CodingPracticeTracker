# if __name__ == '__main__':
    
    # names_list = []
    # scores_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
        
    #     names_list.append(name)
    #     scores_list.append(score)
        
    # arr_list = list(scores_list)
    # print(list(set(sorted(arr_list)))[1])
    
    # # [index for index, value in enumerate(lst) if value == element]
    
    # # final_list = []
    # # for i in range(len(names_list)):
    # #     final_list.append([names_list[i], scores_list[i]])
        
    # # print(final_list)
    
    
def findLowestInNested(listToUse):
    lowest = listToUse[0][1]
    for i in listToUse:
        if i[1] < lowest:
            lowest = i[1]
    return lowest 

if __name__ == '__main__':
    l = []
    tempList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    
    lowest = findLowestInNested(l)
    
    for i in l:
        if lowest != i[1]:
            tempList.append(i)
    
    secondLowest = findLowestInNested(tempList)
    
    list_to_print = []
    for i in l:
        if i[1] == secondLowest:
            list_to_print.append(i[0])
    
    list_to_print.sort()
    for i in list_to_print:
        print(i)
    
