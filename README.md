# Setting Up a Python Virtual Environment (`venv`)

This guide explains how to create and activate a Python virtual environment using `venv` on **Windows** and **macOS/Linux**.

## Prerequisites

Ensure Python is installed by running:

```sh
python3 --version
```

## If Python isn’t installed, install it inside WSL:

```sh
sudo apt update && sudo apt install python3 python3-venv python3-pip
```

# Creating and Activating a Virtual Environment

## Step 1: Open WSL
Launch WSL from PowerShell or Command Prompt:

```Powershell
wsl
```

## Step 2: Navigate to Your Project Folder
Move to the directory where your Python project is located:

```sh
cd /mnt/c/Users/user/Desktop/llm
```

## Step 3: Navigate to Your Project Folder
Move to the directory where your Python project is located:

```sh
python3 -m venv llm
```

## Step 4: Activate the Virtual Environment
Once created, activate the virtual environment:

```sh
source llm/bin/activate
```

## Step 5: Install Dependencies
After activation, install Python packages as needed (follow documentation in link):

```sh
pip install --upgrade --quiet  azure-search-documents
pip install --upgrade --quiet  azure-identity
```

[langchain vector store : azure search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/#install-azure-ai-search-sdk)

## Step 6: Deactivate When Done
To exit the virtual environment:

```sh
deactivate
```

# Notes
You can access Windows files inside WSL using /mnt/c/..., allowing easy integration with Windows tools.

Virtual environments help isolate dependencies, preventing conflicts between projects.

Always activate the virtual environment before running Python scripts inside WSL.

Now you're all set! 🚀