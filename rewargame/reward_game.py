import datetime

# create a list to hold the table data
data = []

# load data from a file, if it exists
try:
  with open('reward_game_data.txt', 'r') as f:
    for line in f:
      data.append(line.strip().split(','))
except FileNotFoundError:
  pass

# request input from the user
while True:
  print_only = input('Do you want to print the current data only? (y/n)')
  
  # if the user wants to print only, break out of the loop
  if print_only == 'n':
    task = input('Enter the task: ')
    points_earned = input('Enter the points earned: ')
    points_redeemed = input('Enter the points redeemed: ')
  
    # get the current date and time
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
  
    # add data to the list
    data.append([date, task, points_earned, points_redeemed, 0])
  
  
  
  # calculate the total points
  for row in data:
    row[4] = str(int(row[2]) - int(row[3]))
  
  # print the table
  print('Date | Task | Points Earned | Points Redeemed | Total Points')
  print('---|---|---|---|---')
  for row in data:
    print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
  
  # save the data to a file
  with open('reward_game_data.txt', 'w') as f:
    for row in data:
      f.write(','.join(row) + '\n')
  
  # generate and print statistics
  points_earned_total = sum([int(row[2]) for row in data])
  points_redeemed_total = sum([int(row[3]) for row in data])
  total_points = points_earned_total - points_redeemed_total
  print(f'Total points earned: {points_earned_total}')
  print(f'Total points redeemed: {points_redeemed_total}')
  print(f'Total points: {total_points}')
  
  # ask the user if they want to enter more data
  more_data = input('Do you want to enter more data? (y/n)')
  if more_data == 'n':
    break
