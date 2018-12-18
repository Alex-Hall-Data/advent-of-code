import itertools

input_text = open("day1_input.txt","r").readlines()

processed_list = list()
for line in input_text:
    processed_list.append(int(line.rstrip()))
    
past_frequencies = list()
running_total=0

for line in itertools.cycle(processed_list):
    if running_total in past_frequencies:
        print(running_total)
        break
    
    else:
        past_frequencies.append(running_total)
        running_total = running_total + line
    
    
    
