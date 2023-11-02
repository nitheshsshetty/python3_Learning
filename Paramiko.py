import paramiko 
print("Using python3 to ssh to lremote server using paramiko ")
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("",username="",password="")
stdin, stdout, stderr = client.exec_command("ls -lrth","hostname")
print(stdout.read().decode())
client.close()
