line = '4of Fo1r pe6ople g3ood th5e the2'
splited_arr = line.split(' ')
new_arr = []
correct_line = ''
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
      for word in splited_arr:
           if str(num) in word:
              new_arr.append(word)
              correct_line = ' '.join(new_arr)
