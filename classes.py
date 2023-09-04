import random
from matplotlib import pyplot as plt

def rule_from_int(id: int, size: int = 8):
    return bin(id)[2:].zfill(size)[::-1]

def bitstr_from_txt(msg: str, size: int = 7):
    return ''.join([bin(ord(char))[2:].zfill(size) for char in msg])

def unif_random_bitstr(size: int):
    return ''.join([str(random.randint(0,1)) for _ in range(size)])

class CA:
    def __init__(self, init_config: str, rule_table: str, r: int = 1) -> None:
        self.n = len(init_config)
        self.r = r
        self.history = [init_config]
        self.rule = rule_table
    
    def __str__(self) -> str:
        return f'CA(rule={self.rule}, r={self.r})'
    
    # TODO: maybe optimize this
    def step(self, t: int = 1) -> None:
        # what_the_hell_is_wrong_with_me = [self.history.append(''.join([self.rule[int(''.join([self.history[-1][j%self.n] for j in range(i-self.r, i+1+self.r)]), 2)] for i in range(self.n)])) for _ in range(t)]
        for _ in range(t):
            next_state = ''
            curr_state = self.history[-1]
            for i in range(self.n):
                # TODO: maybe replace this with numpy and convolution maybe
                neighborhood = [curr_state[j%self.n] for j in range(i-self.r, i+1+self.r)]
                lookup_idx = int(''.join(neighborhood), 2)
                next_state += self.rule[lookup_idx]
                
            self.history.append(next_state)
    
    def get_state(self):
        return self.history[-1]
    
    def show_std(self):
        plt.imshow(
            [list(map(lambda x: not int(x), state)) for state in self.history], 
            cmap='gray'
        )
        plt.title(self)
        plt.xticks([0,self.n])
        plt.yticks([0,len(self.history)])
        plt.show()

def make_sample(size: int, dist) -> list[str]:
    interval =[0,1]
    sample = list()
    for _ in range(size):
        p = int(100*dist(*interval))
        fella = ['1']*p + ['0']*(100-p)
        random.shuffle(fella)
        sample.append(''.join(fella))
    return sample

def reward_MAJ(ca):
    # NOTE: check if size//2 is a good way to check ig
    state = ca.get_state()
    n = ca.n
    return int(state == str(int(state.count('1') >= size//2))*size)

def reward_SYN(rule: str, size: int):
    pass

def reward_XOR(rule: str, size: int):
    pass

class GA:
    def __init__(self,  r: int, n: int, pop_size: int, reward) -> None:
       self.population = make_sample(pop_size, random.uniform) # REVIEW: if this is right
       self.reward = reward
       self.n = n
       self.r = r

    def eval_rule(self, rule: str, num_ic: int) -> int:
        # NOTE: if envs are created each time, or same 100 used per eval, or same 100 used overall
        fitness = 0
        for env in make_sample(num_ic, random.uniform):
            ca = CA(env, rule, self.r)
            seen = set()
            for _ in range(self.n*2):
                # REVIEW: this can prob be optimized
                state = int(ca.step(),2)
                if state in seen:
                    break
                seen.add(state)
            fitness += self.reward(state)
        return fitness