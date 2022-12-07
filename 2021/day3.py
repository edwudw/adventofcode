from collections import defaultdict

def most_and_least_common(numbers):
  # Get the length of the binary numbers
  n = len(numbers[0])

  # Create a list to store the most and least common numbers for each column
  most_common = []
  least_common = []

  # Loop over the columns
  for col in range(n):
    # Create dictionaries to count the occurrences of 0s and 1s in the current column
    counts = defaultdict(int)
    for number in numbers:
      counts[number[col]] += 1

    # Append the most and least common numbers to the appropriate lists
    most_common.append(max(counts, key=counts.get))
    least_common.append(min(counts, key=counts.get))

  # Multiply the most and least common numbers together and return the result in decimal
  result = int("".join(most_common), 2) * int("".join(least_common), 2)
  return result

# Read the numbers from the file
with open("day3.txt") as f:
  numbers = f.readlines()

# Test the function
print(most_and_least_common(numbers))

