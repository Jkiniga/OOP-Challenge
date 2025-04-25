from pet import Pet

# Create a new pet
my_pet = Pet("Max")

print(f"Creating pet: {my_pet.name}")

# Perform actions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Train the pet with some tricks
my_pet.train("roll over")
my_pet.train("play dead")

# Display the status
my_pet.get_status()