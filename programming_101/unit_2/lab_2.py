# Lab 2 10/28/21

# Mad Libs

# base text to be used, credit: Swedish House Mafia

# Upon a hill {location} across a blue lake{noun},
# That's where I had my first heartbreak{noun related to emotion}.
# I still remember how it all changed.
# My father{family member} said,
# "Don't you worry{verb}, don't you worry{verbx2}, child.
# See heaven{Proper noun}'s got a plan for you.

# mad lib variables from above with inputs
location = input("Name a location: ")
noun = input("Provide a noun: ")
emote = input("Provide a noun related to emotion: ")
fam = input("Provide a family member: ")
verb = input("Provide an action verb: ")
proper = input("Provide a proper noun: ")

# printing out updated lyrics
print("\n")
print(f"Upon a {location} across a blue {noun},")
print(f"That's where I had my first {emote}.")
print(f"I still remember how it all changed.")
print(f"My {fam} said,")
print(f"Don't you {verb}, don't you {verb}, child")
print(f"See {proper}'s got a plan for you.")
