import random
 
def sort_by(a):
  return a[1]

def main():
  team_count = int(input('How many teams?'))
  dice_rolls = int(input('How many dice would you like to roll?'))
  dice_size = int(input('How many sides are the dice?'))
  results = []

  for j in range (0,team_count):
    
    teamname = input('Teamname?')
    
    
    dice_sum = 0
    for i in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      if roll == 1:
        print(f'You rolled a {roll}! Critical Fail!')
      elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success!')
      else:
        print(f'You rolled a {roll}')
      dice_sum += roll

    print(f'{teamname} have rolled a total of {dice_sum}')
    results.append([teamname , dice_sum])

    # print(results)

##  for i in range(0, len(results)):
##    #print(i)
##    print('Team:',results[i][0],' scored ', results[i][1] ,' points')

  results.sort(key=sort_by, reverse = True)

  print('The winner is : ', results[0][0],' that scored ', results[0][1], ' points!') 
  for i in range(1, len(results)):
    #print(i)
    print('Team:',results[i][0],' scored ', results[i][1] ,' points')


if __name__== "__main__":
  main()
