import paramiko

def port(server, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.connect(server, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    return ssh_stdout