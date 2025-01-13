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