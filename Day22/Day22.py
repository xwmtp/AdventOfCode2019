# https://adventofcode.com/2019/day/22


f = open("Input22.txt")
inputs = f.read().splitlines()
f.close()

class Space_cards:

    def __init__(self, stock_size):
        self.cards = list(range(stock_size))


    def deal_into_new_stack(self):
        self.cards.reverse()

    def cut_n_cards(self, n):
        self.cards = self.cards[n:] + self.cards[:n]

    def deal_with_increment_n(self, n):
        size = len(self.cards)
        table = [0] * size
        i, t = 0, 0
        for i in range(size):
            table[t] = self.cards[i]
            t = (t + n) % (size)
        self.cards = table

    def parse_shuffle_instructions(self, instructs):
        for instruct in instructs:
            print(self.cards)
            if instruct == 'deal into new stack':
                print('reversing')
                self.deal_into_new_stack()
            else:
                words = instruct.split(' ')
                if words[0] == 'cut':
                    print(f'cutting {words[1]}')
                    self.cut_n_cards(int(words[1]))
                if words[0] == 'deal':
                    print(f'dealing increment {int(words[-1])}')
                    self.deal_with_increment_n(int(words[-1]))



inputs_1 = ['cut 6','deal with increment 7','deal into new stack']
inputs_2 = ['deal with increment 7','deal with increment 9','cut -2']
inputs_3 = ['deal into new stack','cut -2','deal with increment 7','cut 8','cut -4','deal with increment 7','cut 3','deal with increment 9','deal with increment 3','cut -1']

cards = Space_cards(10)

cards.parse_shuffle_instructions(inputs_1)
print(cards.cards)
#print(cards.cards.index(2019))



# too low 2652

# --- Part 2 ---

class Space_card:

    def __init__(self, card, total):
        self.positions = {card}
        self.card = card
        self.opposite_card = total - card - 1
        self.total = total

    def deal_into_new_stack(self):
        for pos in self.positions.copy():
            self.positions.add(self.total-pos-1)

    def cut_n_cards(self, n):
        for pos in self.positions.copy():
            self.positions.add((pos+n)%self.total)

    def deal_with_increment_n(self, n):
        for pos in self.positions.copy():
            self.positions.add((n * pos)%self.total)


    def parse_shuffle_instructions(self, instructs):
        for instruct in instructs:
            print(len(self.positions))
            if instruct == 'deal into new stack':
                self.deal_into_new_stack()
            else:
                words = instruct.split(' ')
                if words[0] == 'cut':
                    print(f'cutting {words[1]}')
                    self.cut_n_cards(int(words[1]))
                if words[0] == 'deal':
                    print(f'dealing increment {int(words[-1])}')
                    self.deal_with_increment_n(int(words[-1]))



card = Space_card(2020, 119315717514047)

card.parse_shuffle_instructions(inputs)




print('')
print(card.positions)
print(len(card.positions))
print(119315717514047)
