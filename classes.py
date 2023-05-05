from matplotlib import pyplot as plt

def rule_from_int(id: int):
    return bin(id)[2:].zfill(8)[::-1]

class CA:
    def __init__(self, init_config: str, rule_table: str, r: int = 1) -> None:
        self.n = len(init_config)
        self.r = r
        self.history = [init_config]
        self.rule = rule_table
    
    def __str__(self) -> str:
        return self.history[-1] # TODO: make more good ig
    
    # TODO: maybe optimize this
    def step(self, t: int = 1) -> None:
        # what_the_hell_is_wrong_with_me = [self.history.append(''.join([self.rule[int(''.join([self.history[-1][j%self.n] for j in range(i-self.r, i+1+self.r)]), 2)] for i in range(self.n)])) for _ in range(t)]
        for _ in range(t):
            next_state = ''
            curr_state = self.history[-1]
            for i in range(self.n):
                neighborhood = [curr_state[j%self.n] for j in range(i-self.r, i+1+self.r)]
                lookup_idx = int(''.join(neighborhood), 2)
                next_state += self.rule[lookup_idx]
                
            self.history.append(next_state)
    
    # TODO: make better
    def show_std(self):
        plt.imshow([list(map(int, state)) for state in self.history])
        plt.show()