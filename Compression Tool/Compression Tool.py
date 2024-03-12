def stepOne():
    with open('135-0.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        letter_freqs = {}
        for c in text:
            letter_freqs[c] = 1 + letter_freqs.get(c, 0)
        print("X IS", letter_freqs['X'])
        print("T IS", letter_freqs['t'])

stepOne()