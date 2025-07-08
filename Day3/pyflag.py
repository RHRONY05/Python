import pyfiglet

# Generate ASCII art text
ascii_art = pyfiglet.figlet_format("Hello, World!")
print(ascii_art)

# Create a banner for your project
banner = pyfiglet.figlet_format("Project X", font="starwars")
print(banner)

# Create larger ASCII art by using a bigger font and width
ascii_art_large = pyfiglet.figlet_format("Big Text", font="block", width=100)
print(ascii_art_large)

# Using a "dotmatrix" font
ascii_art_dot = pyfiglet.figlet_format("Dot Matrix", font="dotmatrix",width=100)
print(ascii_art_dot)