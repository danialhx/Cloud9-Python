import os
import subprocess

#cmd ls
print("#run py script cmd ls")
os.system("ls")
print("")

#cmd ls -l file.md
print("#run py script cmd ls -l file.md")
subprocess.run(["ls","-l","/home/ec2-user/environment/README.md"])
print("")

#run uname -a on CLI
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("")

#cmd ps -x
command2="ps"
command2Argument="-x"
print(f'Gathering active process information with command: {command2} {command2Argument}')
subprocess.run([command2,command2Argument])
print("")