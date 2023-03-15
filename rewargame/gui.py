import tkinter as tk
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

# create the main window
root = tk.Tk()
root.title('Reward Game')

# create the entry widgets
task_label = tk.Label(root, text='Task')
task_entry = tk.Entry(root)
points_earned_label = tk.Label(root, text='Points Earned')
points_earned_entry = tk.Entry(root)
points_redeemed_label = tk.Label(root, text='Points Redeemed')
points_redeemed_entry = tk.Entry(root)

# create the submit button
submit_button = tk.Button(root, text='Submit')

# create the text widget to display the table
table_text = tk.Text(root)

# create the function to be called when the submit button is clicked
def submit():
  # get the task and points from the entry widgets
  task = task_entry.get()
  points_earned = points_earned_entry.get()
  points_redeemed = points_redeemed_entry.get()
  
  # get the current date and time
  now = datetime.datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')
  
  # add data to the list
  data.append([date, task, points_earned, points_redeemed, 0])
  
  # calculate the total points
  for row in data:
    row[4] = str(int(row[2]) - int(row[3]))
  
  # clear the text widget
  table_text.delete('1.0', tk.END)
  
  # insert the table data into the text widget
  table_text.insert('1.0', 'Date | Task | Points Earned | Points Redeemed | Total Points\n')
  table_text.insert('2.0', '---|---|---|---|---\n')
  for row in data:
    table_text.insert('3.0', f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n')
  
  # save the data to a file
  with open('reward_game_data.txt', 'w') as f:
    for row in data:
      f.write(','.join(row) + '\n')
  
  # generate and print statistics
  points_earned_total = sum([int(row[2]) for row in data])
  points_redeemed_total = sum([int(row[3]) for row in data])
  total_points = points_earned_total - points_redeemed_total
  # ask the user if they want to enter more data
  more_data = input('Do you want to enter more data? (y/n)')
  
submit()