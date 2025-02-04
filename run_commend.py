from SshToServer import SshToServer

my_ssh = SshToServer("/Users/ofek_matlov/Desktop/aws/my-key-pair.pem", "13.60.182.178", "ubuntu")
stdout, stdrr = my_ssh.runRemoteCommand("date")
print(stdout)
print(stdrr)

def checkCommend(output):
    stdout, stdrr = my_ssh.runRemoteCommand(output)
    if stdout != "":
        print(stdout)
    else:
        print("Error: " + stdrr) 

checkCommend("wdwfewe")
