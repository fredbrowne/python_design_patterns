# Design Patterns with Python

## Topics covered:

### Single Responsibility Principle

The main purpose of Single Responsibility Purpose is to not give too much to your class.
In this case, we have a Journal() class, which accepts entries, removes entries and display entries.

We could implement the methods to actually save those entries into a file, but if for any case you have
to add new functionalities or logics to the save the file, this class will lose its purpose
and will became to big. Using SRP we can extract the functionality of saving the file from Journal() class
and create a new class called PersinstanceManager() which will be responsible for this actions.

This class can then be extracted into a new file, imported and re-used, as well as changed without
impacting the current Journal() class.

