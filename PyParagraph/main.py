import os
import re

paragraph0_txt = os.path.join('Resources','paragraph_0.txt')

with open(paragraph0_txt,'r') as txtfile:
    paragraph = [word for line in txtfile for word in line.split()]
    sentence_count, wordlenght_total = 0, 0
    for i in paragraph:
        wordlenght_total += len(i)
        if i[-1] == ("." or "?" or "!"):
            sentence_count += 1

print(f'Paragraph Analysis')
print(f'-------------------')
print(f'Approximate word count: {len(paragraph)}')
print(f'Approximate sentence count: {sentence_count}')
print(f'Average Letter Count: {round(wordlenght_total/len(paragraph),1)}')
print(f'Average Sentence Lenght: {round(len(paragraph)/sentence_count,1)}')

f = open("Analysis/paragraph_analysis.txt", "w")
f.write("Paragraph Analysis")
f.write("\n-------------------")    
f.write(f'\nApproximate word count: {len(paragraph)}')
f.write(f'\nApproximate sentence count: {sentence_count}')
f.write(f'\nAverage Letter Count: {round(wordlenght_total/len(paragraph),1)}')
f.write(f'\nAverage Sentence Lenght: {round(len(paragraph)/sentence_count,1)}')
#END