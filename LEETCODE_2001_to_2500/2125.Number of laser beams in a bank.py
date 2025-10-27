def numberOfBeams(bank) -> int:
    filtered_list = [ele.count("1") for ele in bank if ele.count("1")!=0]
    ans = 0
    for i in range(len(filtered_list)-1):
        ans += filtered_list[i]*filtered_list[i+1]
    return ans  