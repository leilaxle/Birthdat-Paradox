import datetime
import random

def getBirthdays(numberOfBirthdays):
    """Returns a list of numberOfBirthdays random date objects for birthdays."""
    birthdays = []
    for _ in range(numberOfBirthdays):
        startOfYear = datetime.date(2000, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthday list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None
    else:
        seen = set()
        for birthday in birthdays:
            if birthday in seen:
                return birthday
            else:
                seen.add(birthday)
        return None

# Display the intro
print('''The birthday paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large. 
This program uses Monte Carlo simulation to explore this concept.''')
print()

# Set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays shall I generate? Maximum 100.")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount
    print("Please enter a number between 1 and 100.")
print()

# Generate and display the birthdays
print("Here are", numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    monthName = MONTHS[birthday.month - 1]
    dateText = '{}{}.'.format(monthName, birthday.day)
    if i != 0:
        print(',', end='')
    print(dateText, end='')
print()
print()

# Check for a match
match = getMatch(birthdays)
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    print('multiple people have a birthday on', monthName, match.day)
else:
    print('there are no matching birthdays.')
print()

# Run simulations
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1

# Display simulation results
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
