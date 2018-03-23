import fileinput
import sys

def fix_unused_param(file):
    with open(file) as log:
        for line in log:
            line = line.strip()
            if line.endswith('[-Wunused-parameter]'):
                file_path = line[0:line.index(':')]
                var_name = line.split("'")[1]
                func_name = next(log).strip()
                line_no = int(line.split(':')[1])
                for fline in fileinput.input(file_path, inplace=True):
                    if fileinput.filelineno() == line_no:
                        print(fline.rstrip().replace(' %s' % var_name, ''))
                    else:
                        print(fline.rstrip())


def main(argv):
    if len(argv) is 0:
        print ('Error: pass a log file as argument')

    for file in argv:
        fix_unused_param(file)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
