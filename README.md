# PyFind - Finding instances in a codebase

This project is a simple script I had put together to go through the codebase of a repository and find instances of strings.
It helps a lot with application rebranding or even when trying to find objects like images.

The idea is to make this extensible so it doesnt just look for text, but also compares contents in files with the given pattern, that being an image comparisson, or even binary chunks.

### Requirements
This project makes use of Python 3.7 coding styles, as well as the following libraries:
* Docopt (argument parsing made as easy as writing a MAN page).
* Colorama (for the styling in the CLI)
* PyTest for unit testing.

In an Anaconda/Pip environment, simply install the requirement.txt file and you will have all the necessary libraries. 
