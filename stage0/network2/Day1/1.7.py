import subprocess
ip_addr = input("Enter ip address to check : ")
result = subprocess.run(["ping" , "-c" , "1" , "-W" , "2"  , ip_addr] , stdout=subprocess.DEVNULL , stderr=subprocess.DEVNULL)
if result.returncode == 0 :
    print("ip is reachable")
else:
    print("ip is not reachable")




