import pandas as pd

# read conversion table from ETS and remove unused column
scoring_table = pd.read_csv('./converted-scores-table.csv', delimiter=';')
scoring_table = scoring_table.drop(columns='Unnamed: 4').iloc[0:-2]

# convert range format from (num - num) to range(num, num) as a list
for i in range(len(scoring_table)):
    temp_arr = scoring_table['Number-Right Score Range'].iloc[i].split('-')
    scoring_table['Number-Right Score Range'].iloc[i] = list(range(int(temp_arr[0]), int(temp_arr[1]) + 1))

# take user inputs for each subtests
Section_1 = int(input('Enter the amount of questions you got right in Section 1 (Listening) : '))
Section_2 = int(input('Enter the amount of questions you got right in Section 2 (Structure and Written) : '))
Section_3 = int(input('Enter the amount of questions you got right in Section 3 (Reading Comprehension) : '))

input_array = [Section_1, Section_2, Section_3] # concat to an array / list for easy indexing

# matched the score to the scaled Score
Section_Scores = []
for j in range(1,4):
    for i in range(len(scoring_table)):        
        if input_array[j-1] in scoring_table['Number-Right Score Range'].iloc[i]:
            Section_Scores.append(list(scoring_table[f'Section {j} Converted Score'].iloc[i].split('-')))

# calculate the final socres
lower_bounds = 0
upper_bounds = 0
print('Scaled Score of your TOEFL ITP is')
for i in range(len(Section_Scores)):
    lower_bounds += int(Section_Scores[i][0])
    upper_bounds += int(Section_Scores[i][1])
    print(f'Section-{i} : {input_array[i]} -> {Section_Scores[i][0]}-{Section_Scores[i][1]}')

print(f'Total Scores : {lower_bounds} * 10/3 - {upper_bounds} * 10/3 -> {round(lower_bounds*10/3)}-{round(upper_bounds*10/3)}')