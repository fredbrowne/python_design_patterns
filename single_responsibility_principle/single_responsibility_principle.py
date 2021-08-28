# Single Responsibility Principle
#
# The main purpose of Single Responsibility Purpose is to not give too much to your class.
# In this case, we have a Journal() class, which accepts entries, removes entries and display entries.
#
# We could implement the methods to actually save those entries into a file, but if for any case you have
# to add new functionalities or logics to the save the file, this class will lose its purpose
# and will became to big. Using SRP we can extract the functionality of saving the file from Journal() class
# and create a new class called PersinstanceManager() which will be responsible for this actions.
#
# This class can then be extracted into a new file, imported and re-used, as well as changed without
# impacting the current Journal() class.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

class PersistanceManager:
    @staticmethod
    def save_to_file(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()

    def load(self, filename):\
        pass

    def low_from_web(self, uri):
        pass

j = Journal()
j.add_entry('Entrada 1')
j.add_entry('Um novo texto')
print(f'Journal entries: \n{j}')

file = r'journal.txt'

PersistanceManager.save_to_file(j, file)