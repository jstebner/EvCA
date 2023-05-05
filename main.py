from classes import *


def main():
    tests = {
        'ecva_ex': {
            'init_config': '10100111010',
            'rule_table': '00010111'
        },
        'wolfram_110': {
            'init_config': '0'*100 + '1' + '0'*100,
            'rule_table': rule_from_int(110)
        }
    }


    test_ca = CA(**tests['wolfram_110'])
    test_ca.step(20)
    test_ca.show_std()
    

if __name__ == '__main__':
    main()