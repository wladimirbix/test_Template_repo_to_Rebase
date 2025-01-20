Prerequisites:

1. Install Visual Studio Code.
2. Install the following Visual Studio Code extensions:
    - Docker
    - Dev Containers
3. Install Docker Desktop.

Running the Code:

1. Start Docker Desktop on your computer.
2. Open Visual Studio Code.
3. Press Ctrl + Shift + P and select Dev Containers: Rebuild and Reopen in Container (or press the "Reopen in Container" Button on the Bottom right).
    - Wait until the terminal displays a message like:
      [108850 ms] Port forwarding 63516 > 39813 > 39813 terminated with code 0 and signal null.
4. Navigate to src/main.py and run the file.
5. If you see Hello World! in the terminal, the container setup was successful.





Useful and Commonly used VSC Shortcuts:


General:
- Command Palette: `Ctrl + Shift + P` (Windows/Linux) / `Cmd + Shift + P` (Mac)
- Open Settings: `Ctrl + ,` (Windows/Linux) / `Cmd + ,` (Mac)
- Toggle Sidebar: `Ctrl + B` (Windows/Linux) / `Cmd + B` (Mac)

File Management:
- New File: `Ctrl + N` (Windows/Linux) / `Cmd + N` (Mac)
- Open File: `Ctrl + O` (Windows/Linux) / `Cmd + O` (Mac)
- Save File: `Ctrl + S` (Windows/Linux) / `Cmd + S` (Mac)
- Close File: `Ctrl + W` (Windows/Linux) / `Cmd + W` (Mac)

Editing:
- Cut Line: `Ctrl + X` (Windows/Linux) / `Cmd + X` (Mac)
- Copy Line: `Ctrl + C` (Windows/Linux) / `Cmd + C` (Mac)
- Paste: `Ctrl + V` (Windows/Linux) / `Cmd + V` (Mac)
- Undo: `Ctrl + Z` (Windows/Linux) / `Cmd + Z` (Mac)
- Redo: `Ctrl + Y` (Windows/Linux) / `Cmd + Shift + Z` (Mac)
- Find: `Ctrl + F` (Windows/Linux) / `Cmd + F` (Mac)
- Replace: `Ctrl + H` (Windows/Linux) / `Cmd + Option + F` (Mac)

Navigation:
- Go to File: `Ctrl + P` (Windows/Linux) / `Cmd + P` (Mac)
- Go to Definition: `F12`
- Go to Line: `Ctrl + G` (Windows/Linux) / `Cmd + G` (Mac)

Multi-Cursor and Selection:
- Add Cursor Below: `Ctrl + Alt + Down Arrow` (Windows/Linux) / `Cmd + Option + Down Arrow` (Mac)
- Add Cursor Above: `Ctrl + Alt + Up Arrow` (Windows/Linux) / `Cmd + Option + Up Arrow` (Mac)
- Select All Occurrences: `Ctrl + Shift + L` (Windows/Linux) / `Cmd + Shift + L` (Mac)

Code Formatting and Refactoring:
- Format Document: `Shift + Alt + F` (Windows/Linux) / `Shift + Option + F` (Mac)
- Rename Symbol: `F2`
- Quick Fix: `Ctrl + .` (Windows/Linux) / `Cmd + .` (Mac)

Terminal:
- Toggle Terminal: `Ctrl + ` (Windows/Linux) / `Cmd + ` (Mac)
- Create New Terminal: `Ctrl + Shift + ` (Windows/Linux) / `Cmd + Shift + ` (Mac)

Debugging:
- Start Debugging: `F5`
- Step Over: `F10`
- Step Into: `F11`
- Step Out: `Shift + F11`

Miscellaneous:
- Zen Mode: `Ctrl + K Z` (Windows/Linux) / `Cmd + K Z` (Mac)
- Toggle Comment: `Ctrl + /` (Windows/Linux) / `Cmd + /` (Mac)