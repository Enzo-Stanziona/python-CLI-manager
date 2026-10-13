# python-CLI-manager
Features

Command Routing System: Uses a nested dictionary structure to map user text commands to specific backend functions with parameter validation.

File Management (arch):

Create directories (nf)

List directory contents (ls)

Search files recursively (sc)

Copy files or directories (cp)

Move files or directories (mv)

System Diagnostics (sys):

Check OS details and architecture (os--v)

List environment variables cleanly (env--v)

Inspect executable/file version info using Windows API (arc--v)

Requirements

Python 3.x

pywin32 library (required only for Windows-specific file version checking: pip install pywin32)

Usage Examples

Once the application is running, type commands directly into the prompt (>):

Check System Version:

> sys os--v


List Environment Variables:

> sys env--v


Create a New Folder:

> arch nf my_folder C:/Users/YourName/Desktop


Check File Version (Windows):

>sys os--v

> sys arc--v C:\Windows\System32 notepad.exe
