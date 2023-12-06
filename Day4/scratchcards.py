
def main():

    scracthies = read_file()

    total_score = 0

    for index, card in enumerate(scracthies):
        winners, our_numbers = clean_card(card)
        # print(winners, our_numbers)

        card_score = 0
        for num in winners:
            if num in our_numbers:
                # print(f'winning number: {num}')
                card_score = increment(card_score)

        total_score += card_score

        # if index > 5:
        #     break
    print(f"total_score: {total_score}")
    return
    
    
def increment(x):
    if x == 0:
        return 1
    else:
        return x + x

def clean_card(card):
    card = card.replace("  ", " ")
    index, data = card.split(":")
    winners, our_numbers = data.split("|")

    winners = winners.strip()
    our_numbers = our_numbers.strip()


    winners = winners.split(" ")
    our_numbers = our_numbers.split(" ")

    return winners, our_numbers
    

def read_file():
    with open("Day4/data/scratchies.txt", "r") as f:
        text = f.readlines()
    return text

def count_winners(winners, our_numbers):
    counter = 0
    for num in winners:
        if num in our_numbers:
            counter += 1
    return counter


def question2():
    scracthies = read_file()



    

    scratch_queue = []

    scratchie_lookups = {}
    for index, card in enumerate(scracthies):
        winners, our_numbers = clean_card(card)
        scratchie_lookups[index] = count_winners(winners, our_numbers)

        scratch_queue.append(index)

    total_scratchies = 0
    while len(scratch_queue) > 0:
        print(len(scratch_queue))
        print(total_scratchies)
        
        curr_scratchie_num = scratch_queue.pop(0)
        total_scratchies += 1

        win_number = scratchie_lookups[curr_scratchie_num]
        for i in range(win_number):
            scratch_queue.append(curr_scratchie_num+1+i)

    print(f"total_score: {total_scratchies}")
    return

if __name__ == "__main__":
    main()

    question2()