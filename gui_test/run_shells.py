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

    '''
    在当前目录下的操作: 去某子目录/返回上级
    '''
    def cd_to(self, _dir):
        cmd = 'cd ' + self.curr_dir + ' && cd ' + _dir + ' && pwd'
        _cd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        (stdout, stderr) = _cd.communicate()
        self.curr_dir = bytes.decode(stdout).replace('\n', '')
        # print('cd_to', self.str_arr(self.curr_dir))

        _cd.kill()
        return self.curr_dir


    # name参数的长度大于1, 外部判断
    # 先实现1级目录
    def create(self, name):
        params = name.split('/')
        if params[len(params) - 1] == '': # 创建目录
            for param in params:
                if param == '': continue
                self.__make_dir(self.curr_dir + '/' + param)
            # pa = filter(lambda p: p != '', params)
            # self.__make_file()
        else: # 创建文件
            pass
            for param in params:
                if param == '': continue
                self.__make_file(self.curr_dir + '/' + param)
            # if name.index('/') == len(name) - 1:
            #     self.__make_dir(name)
            # else:
            #     self.__make_file(name)

    def __make_dir(self, dir_name):
        cmd = 'mkdir ' + dir_name
        print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    def __make_file(self, file_name):
        cmd = 'touch ' + file_name
        print(cmd)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)




if __name__ == '__main__':
    shell = RunShell()
    print(shell.curr_dir)
    shell.cd_to('Downloads/shells')
    print(shell.curr_dir)

    # create
    shell.create('ttestt.txt')