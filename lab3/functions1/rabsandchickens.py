def solve(numheads, numlegs):
    chikens = (numlegs - (4 * numheads)) / -2
    rabits = numheads - chikens
    return f"Rabits: {int(rabits)}\nChikens: {int(chikens)}"