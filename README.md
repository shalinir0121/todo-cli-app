\# CLI Todo App



A simple command-line to-do list application built in Python.



\## Features

\- Add new tasks

\- List all tasks with completion status

\- Mark tasks as done

\- Delete tasks

\- Tasks are saved in a JSON file (`tasks.json`) so they persist between runs



\## How to Use



1\. Make sure you have Python installed.

2\. Clone this repository or download the `todo.py` file.

3\. Run the program:

&nbsp;  ```bash

&nbsp;  python todo.py

Available commands:



text

add <task>      - Add a new task

list            - Show all tasks

done <index>    - Mark task at index as done

delete <index>  - Remove task at index

exit            - Exit the program

Example

text

Welcome to CLI Todo App

Type 'add <task>', 'list', 'delete <index>', 'done <index>', or 'exit'



> add Buy milk

Added: Buy milk



> list

0\. \[✗] Buy milk



> done 0

Marked as done: Buy milk



> list

0\. \[✓] Buy milk



> exit

Goodbye!

