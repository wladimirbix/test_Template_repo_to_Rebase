# Unicon CLI Tool Template

This repository is a template using the custom Unicon CLI Tool. It provides a foundation to create and customize your own projects.

## Instructions

1. Install Visual Studio Code.

2. Install Docker Desktop.

3. Install the following Visual Studio Code extensions:
    - Docker
    - Dev Containers

4. Create your own repository using the template  
   Go to GitHub and click the "Use this template" button to create your own repository based on this template.

5. Start Docker Desktop  
   Make sure Docker Desktop is installed and running on your computer.

6. Build and open the program in the Docker container  
   Open Visual Studio Code and press Ctrl + Shift + P to open the command palette. Search for the command "Remote-Containers: Open Folder in Container" and select it.

7. Create a profile  
   Once the container is built, type `unicon` in the console and follow the instructions to create a profile.

8. Log into a Databricks profile  
   To log into a Databricks profile, click on the Databricks extension icon on the left side of Visual Studio Code and select "Log in". Then choose the profile you want to log in with.

9. Incorporate changes from the template  
   To incorporate future changes from the template, use the `git rebase` command. Do **not** use the `git commit` command since that will overwrite your code.

## Important Notes

- Folders that begin with a dot (.) must not be modified (e.g., .devcontainer, .vscode, .databricks, ...).
- The `resources` folder contains code templates.
- The `src` folder is where the user's code goes.
- The `test` folder contains automated tests.
- The `tmp` folder contains temporary files and cache files.



## Useful and Commonly Used VSC Shortcuts

### General:
- Command Palette: `Ctrl + Shift + P` (Windows/Linux) / `Cmd + Shift + P` (Mac)
- Open Settings: `Ctrl + ,` (Windows/Linux) / `Cmd + ,` (Mac)
- Toggle Sidebar: `Ctrl + B` (Windows/Linux) / `Cmd + B` (Mac)

### File Management:
- New File: `Ctrl + N` (Windows/Linux) / `Cmd + N` (Mac)
- Open File: `Ctrl + O` (Windows/Linux) / `Cmd + O` (Mac)
- Save File: `Ctrl + S` (Windows/Linux) / `Cmd + S` (Mac)
- Close File: `Ctrl + W` (Windows/Linux) / `Cmd + W` (Mac)

### Editing:
- Cut Line: `Ctrl + X` (Windows/Linux) / `Cmd + X` (Mac)
- Copy Line: `Ctrl + C` (Windows/Linux) / `Cmd + C` (Mac)
- Paste: `Ctrl + V` (Windows/Linux) / `Cmd + V` (Mac)
- Undo: `Ctrl + Z` (Windows/Linux) / `Cmd + Z` (Mac)
- Redo: `Ctrl + Y` (Windows/Linux) / `Cmd + Shift + Z` (Mac)
- Find: `Ctrl + F` (Windows/Linux) / `Cmd + F` (Mac)
- Replace: `Ctrl + H` (Windows/Linux) / `Cmd + Option + F` (Mac)

### Navigation:
- Go to File: `Ctrl + P` (Windows/Linux) / `Cmd + P` (Mac)
- Go to Definition: `F12`
- Go to Line: `Ctrl + G` (Windows/Linux) / `Cmd + G` (Mac)

### Multi-Cursor and Selection:
- Add Cursor Below: `Ctrl + Alt + Down Arrow` (Windows/Linux) / `Cmd + Option + Down Arrow` (Mac)
- Add Cursor Above: `Ctrl + Alt + Up Arrow` (Windows/Linux) / `Cmd + Option + Up Arrow` (Mac)
- Select All Occurrences: `Ctrl + Shift + L` (Windows/Linux) / `Cmd + Shift + L` (Mac)

### Code Formatting and Refactoring:
- Format Document: `Shift + Alt + F` (Windows/Linux) / `Shift + Option + F` (Mac)
- Rename Symbol: `F2`
- Quick Fix: `Ctrl + .` (Windows/Linux) / `Cmd + .` (Mac)

### Terminal:
- Toggle Terminal: `Ctrl + ` (Windows/Linux) / `Cmd + ` (Mac)
- Create New Terminal: `Ctrl + Shift + ` (Windows/Linux) / `Cmd + Shift + ` (Mac)

### Debugging:
- Start Debugging: `F5`
- Step Over: `F10`
- Step Into: `F11`
- Step Out: `Shift + F11`

### Miscellaneous:
- Zen Mode: `Ctrl + K Z` (Windows/Linux) / `Cmd + K Z` (Mac)
- Toggle Comment: `Ctrl + /` (Windows/Linux) / `Cmd + /` (Mac)

## Additional Notes

- Keep the README file up to date to inform new users about changes or additional instructions.
- Ensure that all dependencies required for running the project are documented.
