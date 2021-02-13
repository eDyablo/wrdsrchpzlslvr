# Home Test task

Word searches are a fun (or tedious, depending on your personality) puzzle where words are hidden in a grid of seemingly random letters. Humans are fairly slow at solving word search puzzles, at least when compared to a computer.

Your task is to write a Python program that searches a grid of letters (a-z only) for valid English words much more quickly than any human possibly could. Words can be found along any diagonal, forwards, upwards, downwards or backwards and must not ‘wrap’ between edges. You may use the provided list of words as a dictionary for this task (this file attached to the message).

### Your program should be able to:
- Generate a board of random letters.
- Identify all valid words (contained in the attached word list) in the board.
- Display results to the user.

### Things we like to see:
- Unit tests (pytest preferred).
- Docstrings.
- Usage information.
- Command-line parameters.
- Reasonable performance (<0.5s for a 15x15 board).

### Rules:
- Any version of Python greater than 3.6 may be used.
- Google and other resources may be used for library or syntax help and small pieces of the puzzle, but don’t look for or use any pre-built wordsearch solutions.

Third-party libraries are allowed, but they must not implement the majority of the logic for you.

### Instructions for candidate:
- Create a public Github repository.
- Initialize with an empty master branch
- Create a new branch.
- Push code to branch.
- Open a Pull Request from branch to empty master.
- Send us a link to their Pull Request (tag `@borysDrozhak` and `@carsongee`).
- We will review and comment on the pull request, and expect them to address code review feedback to get the feel for delivering an actual code change.
