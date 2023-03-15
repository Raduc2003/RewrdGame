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
window = tk.Tk()
window.title('Reward Game')
window.geometry("900x600")

# set the background color to the specified color palette
window.configure(bg='#D5D8DD')

# create the input fields
task_label = tk.Label(text='Task:', font=("Helvetica", 18), bg='#D5D8DD')
task_entry = tk.Entry(font=("Helvetica", 18), bg='#5CA2BE')

points_earned_label = tk.Label(text='Points Earned:', font=("Helvetica", 18), bg='#D5D8DD')
points_earned_entry = tk.Entry(font=("Helvetica", 18), bg='#5CA2BE')

points_redeemed_label = tk.Label(text='Points Redeemed:', font=("Helvetica", 18), bg='#D5D8DD')
points_redeemed_entry = tk.Entry(font=("Helvetica", 18), bg='#5CA2BE')

# create the submit button
submit_button = tk.Button(text='Submit', font=("Helvetica", 18), bg='#2A4353', fg='#D5D8DD', relief='flat', bd=0)
# create the show data button
show_data = tk.Button(text="Data so far", font=("Helvetica", 18), bg='#2A4353', fg='#D5D8DD', relief='flat', bd=0)
# create the show data button
remove_button = tk.Button(text="Remove last entry", font=("Helvetica", 18), bg='#2A4353', fg='#D5D8DD', relief='flat', bd=0)
# create the output field
# create a scrollbar and text widget for the output
output_frame = tk.Frame(window)
scrollbar = tk.Scrollbar(bg='#D5D8DD')
output_text = tk.Text(font=("Helvetica", 18), bg='#989DA4', fg='#2A4353', yscrollcommand=scrollbar.set)
# configure the scrollbar to work with the text widget
scrollbar.config(command=output_text.yview)


# create a function to handle the submit button click
def submit_button_click():
  task = task_entry.get()
  points_earned = points_earned_entry.get()
  points_redeemed = points_redeemed_entry.get()
  # get the current date and time
  now = datetime.datetime.now()
  date = now.strftime('%Y-%m-%d %H:%M:%S')
  # add the data to the list and calculate the total points

  data.append([date, task, points_earned, points_redeemed, 0])
  print(data)
  for row in data:
    row[4] = str(int(row[2]) - int(row[3]))
    
  
  # generate and print the table
  output = 'Date | Task | Points Earned | Points Redeemed | Total Points\n'
  output += '---|---|---|---|---\n'
  for row in data:
    output += f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n'
  
  # save the data to a file
  with open('reward_game_data.txt', 'w') as f:
    for row in data:
      f.write(','.join(row) + '\n')
  
  # generate and print statistics
  points_earned_total = sum([int(row[2]) for row in data])
  points_redeemed_total = sum([int(row[3]) for row in data])
  total_points = points_earned_total - points_redeemed_total
  output += f'Total points earned: {points_earned_total}\n'
  output += f'Total points redeemed: {points_redeemed_total}\n'
  output += f'Total points: {total_points}\n'
  
  # update the output label with the table and statistics
  output_text.insert('end', output)
  
# create a function to handle the show data button click
def show_data_click():
  # generate and print the table
  output = 'Date | Task | Points Earned | Points Redeemed | Total Points\n'
  output += '---|---|---|---|---\n'
  for row in data:
    output += f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n'
  # generate and print statistics
  points_earned_total = sum([int(row[2]) for row in data])
  points_redeemed_total = sum([int(row[3]) for row in data])
  total_points = points_earned_total - points_redeemed_total
  output += f'Total points earned: {points_earned_total}\n'
  output += f'Total points redeemed: {points_redeemed_total}\n'
  output += f'Total points: {total_points}\n'
  
  # clear the output text widget and insert the new text
  output_text.delete('1.0', tk.END)
  output_text.insert('1.0', output) 

  
# create a function to handle remove last entry
def remove_click():
  with open("reward_game_data.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines[:-1]:
        f.write(line)
    f.truncate()
  # update the output
  output_text.delete('1.0', tk.END)
  output = 'Date | Task | Points Earned | Points Redeemed | Total Points\n'
  output += '---|---|---|---|---\n'
  for row in data:
    output += f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}\n'
  output_text.insert('1.0', output)

# bind the submit button click to the function
submit_button.config(command=submit_button_click)
# bind the show data button click to the function
show_data.config(command=show_data_click)
# bind the remove button click to the function
remove_button.config(command=remove_click)
# layout the widgets
task_label.pack()
task_entry.pack()
points_earned_label.pack()
points_earned_entry.pack()
points_redeemed_label.pack()
points_redeemed_entry.pack()
submit_button.pack()
show_data.pack()
remove_button.pack()
# output_label.pack()
scrollbar.pack(side='right', fill='y')
output_text.pack(side='left', fill='both', expand=True)

# run the main loop
window.mainloop()
