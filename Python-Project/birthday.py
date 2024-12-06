import datetime, random

def getBirthdays(numberOfBirthdays):    
    """Return a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthday have he same year
        startOfYear = datetime.date(2001,1,1)
        
        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are uniques. so return none
    
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday.
            
# Display the intro
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',  'Dec')

while True:
    print("How many birthday shall i generate? (max 100)") 
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)     
        break  
print()

# Generate and display the birthdays
print("Here are", numBDays, 'birthdays:')
birthdays= getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(',  ', end='')
        
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through the 100,000 simulations
print("Generating", numBDays, 'random birthdays 100,000 times....')
input("Press Enter to begin...")

print('Let\'s run another 100,00 simulations')
simMatch = 0
for i in range(100_000):
    if 1 % 10_000 == 0:
        print(i, 'simulation run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulation RUN.')

# Display simulation results:
probability= round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

