print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_van_vleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 39

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots.")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_van_vleet_3pts_made} 3 point shots.")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots.")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamal_murray_3pts_attempts = 130
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_van_vleet_3pts_attempts = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
james_harden_3pts_attempts = 117
# print()

print("Challenge 2.4: Build on your print statement")

# # TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# # the number of three point shots for each player. E.g., output should be similar to
# # "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
# print()
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots off {jamal_murray_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_van_vleet_3pts_made} 3 point shots off {fred_van_vleet_3pts_attempts} attempts.")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots off {james_harden_3pts_attempts} attempts.")


print("In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts.")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# # TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# # TODO: Calculate and print the 3 point percentage for Jamal Murray
jamal_murray_3pts_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempts
print(jamal_murray_3pts_made/jamal_murray_3pts_attempts)
# # TODO: Calculate and print the 3 point percentage for Fred VanVleet
print(fred_van_vleet_3pts_made/fred_van_vleet_3pts_attempts)
fred_van_vleet_3pts_percentage = fred_van_vleet_3pts_made/fred_van_vleet_3pts_attempts
# # TODO: Calculate and print the 3 point percentage for James Harden
james_harden_3pts_percentage = james_harden_3pts_made/james_harden_3pts_attempts
print(james_harden_3pts_made/james_harden_3pts_attempts)
# print()

# print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# # TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(f"In the 2020 NBA playoffs, \nJamal Murray made {jamal_murray_3pts_made} 3 point shots \noff {jamal_murray_3pts_attempts} attempts \nat a percentage of {jamal_murray_3pts_percentage}.")
print(f"In the 2020 NBA playoffs, \nFred VanVleet made {fred_van_vleet_3pts_made} 3 point shots \noff {fred_van_vleet_3pts_attempts} attempts \nat a percentage of {fred_van_vleet_3pts_percentage}.")
print(f"In the 2020 NBA playoffs, \nJames Harden made {james_harden_3pts_made} 3 point shots \nof {james_harden_3pts_attempts} attempts \nat a percentage of {james_harden_3pts_percentage}.")

# print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# # TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(f"In the 2020 NBA playoffs, \nJamal Murray made {jamal_murray_3pts_made} 3 point shots \noff {jamal_murray_3pts_attempts} attempts \nat a percentage of {jamal_murray_3pts_percentage}.".upper())
print(f"In the 2020 NBA playoffs, \nFred VanVleet made {fred_van_vleet_3pts_made} 3 point shots \noff {fred_van_vleet_3pts_attempts} attempts \nat a percentage of {fred_van_vleet_3pts_percentage}.".upper())
print(f"In the 2020 NBA playoffs, \nJames Harden made {james_harden_3pts_made} 3 point shots \noff {james_harden_3pts_attempts} attempts \nat a percentage of {james_harden_3pts_percentage}.".upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# # TODO: make a variable called `lakers_are_best` to indicate this
# # TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = True
print(f"Yes, it is {lakers_are_best} L.A. will win the 2019-2020 COVID Championship!")
# print('Challenge 3.4: Type Conversion')
# # TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_are_best = True
print(int(lakers_are_best))
# # TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_are_best = True
print(float(lakers_are_best))
# print('Challenge 3.5: Type Conversion Part 2')
# # TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(str(jamal_murray_3pts_percentage))
print(str(fred_van_vleet_3pts_percentage))
print(str(james_harden_3pts_percentage))
# # TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(jamal_murray_3pts_percentage))
print(int(fred_van_vleet_3pts_percentage))
print(int(james_harden_3pts_percentage))
