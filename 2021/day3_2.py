from collections import defaultdict

def ratings(numbers, find_oxygen):
  # Get the length of the binary numbers
  n = len(numbers[0])

  # Create a list to store the ratings
  oxygen_rating = []

  # Loop over the bits
  for bit in range(n):
    # Create a list of all possible numbers (0 and 1)
    possible_numbers = ["0", "1"]
    num_temp = [num[bit] for num in numbers]
    # Count the occurrences of each number in the current bit position
    counts = [num_temp.count(num) for num in possible_numbers]

    # If 0 and 1 are equally common, keep values with a 1 for the oxygen rating and 0 for the CO2 rating
    if counts[0] == counts[1]:
      common_bit = "1" if find_oxygen else "0"
      numbers = [number for number in numbers if number[bit] == common_bit]
      oxygen_rating.append(common_bit)
    # Otherwise, keep the most and least common numbers for the oxygen and CO2 ratings, respectively
    else:
      # Find the index of the most and least common numbers in the list
      max_index = counts.index(max(counts))
      min_index = counts.index(min(counts))

      # Use the index to get the actual numbers
      if find_oxygen:
        numbers = [number for number in numbers if number[bit] == possible_numbers[max_index]]
        oxygen_rating.append(possible_numbers[max_index])
      else:
        numbers = [number for number in numbers if number[bit] == possible_numbers[min_index]]
        oxygen_rating.append(possible_numbers[min_index])

  # Return the oxygen and CO2 ratings in decimal form
  return int("".join(oxygen_rating), 2)

# Read the numbers from the file
with open("day3.txt") as f:
  numbers = f.readlines()

# Test the function
print(ratings(numbers, True))
print(ratings(numbers, False))


