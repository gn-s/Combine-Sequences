def combine(forward, reverse):
    num = len(forward)
    start = num // 2
    end =  start + 4
    for i in range(start, end):
        seq = []
        seq.append(forward[i])
    print(num)
    print(start)
    print(end)
    print(f'{seq}')

    '''for j in reverse:
        for f in seq:
            if seq[f] == reverse[j]:'''

def fix_test():
    pass


def main():
    print('---------Hello welcome to Combine Sequences program!----------')
    forward = input('Input Forward Sequence:')
    reverse = input('Input Reverse Sequence:')
    combined = combine(forward, reverse)
    print(f'The combined sequence is: {combined}')


if __name__ == "__main__":
        main()