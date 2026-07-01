# 4-scripting

This repository contains two scripts (one written in Bash and the other in Python) designed to take a user's name as a command-line argument and display a customized greeting along with the current localized time

`Hello <name>, right now the time is <current date and time based on timezone>`
## Included Files
* `hello.sh` - The Bash implementation.
* `hello.py` - The Python implementation.

---

## 1. Bash Script (`hello.sh`)

**Language Type:** Bash operates as an **interpreted** language. This means you do not need to compile the code beforehand; the Bash shell reads and executes the script directly at runtime.

### Execution Commands

First, grant the script execution permissions (you only need to do this once):
```bash
chmod +x hello.sh
```

Next, run the script and pass your name as an argument:
```bash
./hello.sh "Abu Dujan"
```

Alternatively, you can bypass the permission step by calling the bash interpreter directly:
```bash
bash hello.sh "Abu Dujan"
```

### Expected Output
```text
Hello Abu Dujan, right now the time is Wed Jul 01 19:45:36 IST 2026
```
*(Note: The exact output will reflect the local timezone configured on your operating system).*

---

## 2. Python Script (`hello.py`)

**Language Type:** Similar to Bash, Python is an **interpreted** language. Python is an interpreted language. The CPython interpreter reads and
runs the source file directly at runtime — there's no separate compile
step the user has to perform (CPython compiles to bytecode internally and
automatically, but that's an implementation detail, not a manual build
step like with C or Java).

### Execution Commands

First, verify that Python 3 is installed on your system:
```bash
python3 --version
```

Then, execute the script by passing your name to the Python interpreter:
```bash
python3 hello.py "Abu Dujan"
```
