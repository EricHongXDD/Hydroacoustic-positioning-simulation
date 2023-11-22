import os
import datetime

import sys


def pin_jie(a):
    str_p = ''
    for ia in range(len(a)):
        str_p = str_p + ' ' + a[ia]
    return str_p


class CheckPoint:
    def __init__(self, args):
        self.getcmd = sys.argv
        self.pin_jie = pin_jie
        self.args = args
        self.load_model = ''
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        appendix = str.split(self.args.data_loader_path, '/')[-1]
        if args.load == '.':
            # self.dir = args.save_file + args.model + '_' + \
            #            self.args.data_train[1]
            self.dir = args.save_file
        else:
            self.dir = args.save_file + args.load

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        open_type = 'a' if os.path.exists(self.dir + '/log.txt') else 'w'
        self.log_file = open(self.dir + '/log.txt', open_type)
        with open(self.dir + '/config.txt', open_type) as f:
            f.write('python' + self.pin_jie(self.getcmd) + '\n')
            f.write(now + '\n\n')
            for arg in vars(args):
                # 'args.arg' is equivalent to 'getattr(args, arg)'
                f.write('{}: {}\n'.format(arg, getattr(args, arg)))
            f.write('\n')

    def write_log(self, log, refresh=False):
        self.log_file.write(log + '\n')
        if refresh:
            self.log_file.close()
            self.log_file = open(self.dir + '/log.txt', 'a+')

    def done(self):
        self.log_file.close()

    def load(self):
        if self.args.resume == -1:
            file_list = os.listdir(self.dir + 'model')
            sorted(file_list)
            self.load_model = os.path.join(self.dir, 'model', file_list[-1])

        elif self.args.resume == 0:
            if self.args.pre_train != '.':
                print('Loading model from {}.'.format(self.args.pre_train))
                self.load_model = self.args.pre_train
                print('Load_model_mode = 1')

        else:
            self.load_model = os.path.join(self.dir, 'model',
                                           '{}_epoch_{}.pth'.format(self.args.model, self.args.resume))
            print('Load_model_mode = 2')

        return self.load_model
