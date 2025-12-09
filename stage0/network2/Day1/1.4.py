def is_private_ip(ip:str)->bool:
    parts = ip.split(".")
    nums = list(map(int , parts))
    part1 , part2  = nums[0] , nums[1] 
    if part1 == 10:
        return True
    elif part1 == 172:
        if 16 <= part2 <=31:
            return True
    elif part1 == 192 and part2 == 168:
        return True
    return False







