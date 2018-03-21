#!/usr/local/bin/python3
import subprocess

class RunShell:
    def __init__(self):
        self.start_dir = '~'
        self.curr_dir = '~'

    def str_to_arr(self, dir_str=''):
        dir_arr = dir_str.split('\n')
        # map(lambda x: x.replace('\n', ''), dir_arr)
        return dir_arr

    def get_current(self):
        return self.curr_dir

    def ls_l(self):
        cmd = 'ls ' + self.curr_dir
        p_ls = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        (stdout, stderr) = p_ls.communicate()
        dir_list = bytes.decode(stdout)
        # str_arr(dir_list)

        p_ls.kill()
        return self.str_to_arr(dir_list)

    def cd_to(self, _dir):
        cmd = 'cd ' + self.curr_dir + ' && cd ' + _dir + ' && pwd'
        _cd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        (stdout, stderr) = _cd.communicate()
        self.curr_dir = bytes.decode(stdout).replace('\n', '')
        # print('cd_to', self.str_arr(self.curr_dir))

        _cd.kill()
        return self.curr_dir



if __name__ == '__main__':
    shell = RunShell()
    print(shell.ls_l())
    shell.cd_to('Downloads')
    print(shell.curr_dir)
    print(shell.ls_l())
    shell.cd_to('shells')
    print(shell.curr_dir)
    print(shell.ls_l())
    shell.cd_to('..')
    print(shell.curr_dir)
    print(shell.ls_l())