#coding:utf-8

get = '  ____      _' + '\n'\
      ' / ___| ___| |_' + '\n' \
      '| |  _ / _ \ __|' + '\n' \
      '| |_| |  __/ |_' + '\n' \
      ' \____|\___|\__|' + '\n'


wild =  '__        __  _     _' + '\n' \
        '\ \      / (_) | __| |' + '\n' \
        ' \ \ /\ / /| | |/ _  |' + '\n' \
        '  \ V  V / | | | (_| |' + '\n' \
        '   \_/\_/  |_|_|\__,_|' + '\n'


str_and = '    _              _' + '\n' \
      '   / \   _ __   __| |' + '\n' \
      '  / _ \ | \'_ \ / _  |' + '\n' \
      ' / ___ \| | | | (_| |' + '\n' \
      '/_/   \_\_| |_|\__,_|' + '\n'


tough = ' _                    _' + '\n' \
        '| |_ ___  _   _  __ _| |__' + '\n' \
        '| __/ _ \| | | |/ _  |  _ \\' + '\n' \
        '| || (_) | |_| | (_| | | | |' + '\n' \
        '\__\___/ \__,_|\__,  |_| |_|' + '\n' \
        '                |___/' + '\n'


def GetWildAndTough(fromNum, toNum):
    for n in range(fromNum, toNum):
        tmp = ''
        if n % 3 == 0 and n % 5 == 0 :
            tmp = get + wild + str_and + tough
        elif n % 3 == 0 :
            tmp = get
        elif n % 5 == 0 :
            tmp = wild
        else :
            tmp = str(n)
        print (tmp)


GetWildAndTough(15, 16)
