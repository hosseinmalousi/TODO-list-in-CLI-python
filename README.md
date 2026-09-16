# Just Do — CLI To-Do List

**Just Do** is a small, dependency-free command-line to-do application written in Python. It lets you keep a persistent list of tasks, add optional due dates and descriptions, mark work as complete, edit tasks, and review completed work.

## Features

- Add tasks with a title, optional description, and optional due date
- View pending tasks from the main menu
- Mark a pending task as complete
- Edit a pending task's title, date, or description
- Delete one task or clear all pending tasks
- View completed tasks
- Persist tasks locally in JSON files between runs
- Display a friendly start-up banner and current date/time

## Requirements

- Python **3.12+**

No third-party packages are required.

## Run the application

From the project directory, run:

```bash
python3 main.py
```

Use the numbered menu to choose an action. Enter `q` in task-selection prompts to return to the main menu where that option is shown.

## Task data

The program saves its data beside the source code:

| File | Purpose |
| --- | --- |
| `undone_tasks.json` | Tasks that are still pending |
| `done_tasks.json` | Tasks marked as completed |

Each task stores a unique ID, title, description, due date, and completion status. You can back up these two files to preserve or transfer your task list.

## Due dates

When adding a task, enter a date in `DD/MM/YYYY` format, for example `24/12/2026`. Leave it blank when the task has no due date.

## Project structure

```text
.
├── main.py              # Application logic and command-line menu
├── Asccii_art.py        # Start-up banner
├── undone_tasks.json    # Pending task storage
└── done_tasks.json      # Completed task storage
```

## Ideas for the next version

See the project review for recommended bug fixes and feature ideas before treating the stored JSON files as long-term data.

## License

No license has been specified yet. Add one (for example, MIT) if you plan to share or publish the project.
