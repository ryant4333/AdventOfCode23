#Turn into list of lists so can use index's
#Either look for symbols and check surrounding numbers
#Or find numbers and their length and assess if they have a symbol nearby

#I think I will find the numbers and find the length, then check surrounding index's

SYMBOL_LIST = "!@#$%^&*()_-+={}[]"
for ch in row:
    if ch in SYMBOL_LIST:
        

def gen_manifest(text):
    #split \n
    #split' '
    # list()

def find_end_index(start_index):
    #start index tuple (x, y)

def main(manifest):
    curr_row = 0
    curr_col = 0

    for row, row_index in enumerate(manifest):
        for col, col_index in enumerate(row):
            if 