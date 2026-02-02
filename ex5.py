# Ex5: Safe Dial Rotation Analysis
#
# Dial specifications:
# - The dial has values from 0 to 99 arranged in a circle.
# - Moving left from 0 wraps to 99.
# - Moving right from 99 wraps to 0.
# - The dial starts at position 50.
#
# Rotation format:
# - Each line contains a direction ('L' or 'R') followed by an integer step count.
#
# Rules:
# - Apply rotations sequentially.
# - After each rotation, check the dial position.
# - Count how many times the dial points to 0 after a rotation.
# - Count how many times the dial passes 0 position during rotation.

# Output:
# - Return the total number of times the dial lands on 0.
# - Return the total number of times the dial passes 0.

# Task source https://adventofcode.com/2025/day/1

class Dial:
  def calculate_zero_lands():
    pass
  
  def calculate_zero_passes():
    pass


# Example usage
if __name__ == "__main__":
    input_data = "read it from input.txt"
    dial = Dial()
  
    assert dial.calculate_zero_lands(input_data) == 1141
    assert dial.calculate_zero_passes(input_data) == 6634
