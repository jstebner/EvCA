from classes import *

def main():
    tests = {
        'ecva_ex': {
            'init_config': '10100111010',
            'rule_table': '00010111'
        },
        'wolfram_110': {
            # 'init_config': '0'*200 + '1' + '0'*200,
            'init_config': '0'*499 + '1',
            # 'init_config': unif_random_bitstr(401),
            'rule_table': rule_from_int(110)
        },
        'wolfram_34': {
            'init_config': bitstr_from_txt('8==D'),
            'rule_table': rule_from_int(34)
        },
        'wolfram_69': {
            'init_config': unif_random_bitstr(100),
            'rule_table': rule_from_int(69)
        }
    }

    # use N = 149
    test_ca = CA(**tests['wolfram_34'])
    test_ca.step(99)
    test_ca.show_std()
    

if __name__ == '__main__':
    main()