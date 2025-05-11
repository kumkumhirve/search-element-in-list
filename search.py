'''Q9: WAP to search element inside list?'''

def search_element(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return "element is found "
        
    return "element is not found"

print(search_element([2,4,6,8,9,1,0],8))