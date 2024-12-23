# Context managers are a good tool to manage resources

print("Example 1")

with open('notes.txt', 'w') as file:
    file.write('some todo...')

# The previous two lines does the same thing as the following
file = open('notes.txt', 'w')
try:
    file.write('some todo...')
finally:
    file.close()

print("\nExample 2")
# Setting up a context manager as a class

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename