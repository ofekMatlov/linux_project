from SshToServer import SshToServer
import re
import csv
import os

my_ssh = SshToServer("/Users/ofek_matlov/Desktop/aws/my-key-pair.pem", "13.60.182.178", "ubuntu")
stdout, stdrr = my_ssh.runRemoteCommand("python3 server_side.py")
#print(stdout)
#print(stdrr)

def checkCommend(output : str ) -> str :
    stdout, stdrr = my_ssh.runRemoteCommand(output)
    if stdout != "":
        return stdout
    else:
        return "Error: " + stdrr 
checkCommend("python3 server_side.py")


def toSaveCsv():  
    commend_return = (checkCommend("python3 server_side.py"))
    start = commend_return.find("ERROR")
    end = commend_return.find("}", start)
    res = commend_return[start:end]
    result = re.split(r'[,:]', res)
    file_path = "client_save_severity.csv"
    new_row = [result[1], result[3], result[5], result[7]]
    file_exists = os.path.isfile(file_path) 
    with open(file_path, "a") as file:
        writer = csv.writer(file)
        if file_exists:
            writer.writerow(new_row)
        else:    
            writer.writerow(["ERROR", "WARN", "INFO", "TIMESTAMP"])
            writer.writerow(new_row)

toSaveCsv()



