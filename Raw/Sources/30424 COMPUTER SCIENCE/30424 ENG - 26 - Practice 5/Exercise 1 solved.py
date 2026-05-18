import random, webbrowser


econ_terms = ['market', 'economy', 'money', 'price', 'cost', 'value', 'capital', 'demand', 'supply', 'profit', 'loss', 'investment', 'interest', 'inflation', 'tax', 'budget', 'income', 'wage', 'employment', 'labor', 'policy', 'government', 'credit', 'debt', 'wealth', 'growth', 'recession', 'trade', 'goods', 'services', 'regulation', 'bank', 'currency', 'competition', 'monopoly', 'equity', 'liability', 'firm', 'shareholder', 'consumer', 'producer', 'subsidy', 'inequality', 'resource', 'exchange', 'transaction', 'stock', 'bond', 'rate', 'sector']



def wiki1(seq):
    word = random.choice(seq)
    d = input('The chosen word is ' + word + '.\nDo you want to see the related webpage? (yes/no) ')
    if d.lower() in ['y', 'yes']:
        webbrowser.open('https://en.wikipedia.org/wiki/' + word)
    else:
        print('Ok. Thank you.')


def wiki2(seq, num):
    chosen_words = {}
    while len(chosen_words) < num:
        word = random.choice(seq)
        if word not in chosen_words:
            chosen_words[word] = 'https://en.wikipedia.org/wiki/' + word

    return chosen_words








    
