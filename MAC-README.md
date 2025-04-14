# Setting Up a Python Virtual Environment (`venv`) on macOS

This guide will walk you through creating and activating a Python virtual environment using `venv` on your Mac. Virtual environments help keep your project's dependencies separate, which is super useful!

## Prerequisites

First, let's make sure Python is installed. Open your **Terminal** application. You can find it by going to **Finder** -> **Applications** -> **Utilities** -> **Terminal**.

Once Terminal is open, type the following command and press Enter:

```sh
python3 --version
```

This command checks the version of Python 3 installed on your Mac. If Python 3 is installed, you'll see something like Python 3.9.6 (the version number might be different).

If you get an error message saying "command not found" or something similar, you'll need to install Python 3. You can download the latest version from the official Python website (python.org).

# Creating and Activating a Virtual Environment

## Step 1: Navigate to Your Project Folder
In the Terminal, use the cd command to move to the directory where you want to create your Python project. For example, if you want to create a project called "llm" on your Desktop, you would type:

```Bash
cd Desktop
mkdir llm
cd llm
```
This creates a new folder called "llm" on your Desktop and moves you into that folder.

## Step 2: Create the Virtual Environment
Now, create the virtual environment using the following command:

```Bash
python3 -m venv llm_env
```

This command creates a new directory called llm_env inside your current folder. This directory will contain all the necessary files to run your Python project in an isolated environment.

## Step 3: Activate the Virtual Environment
To start using the virtual environment, you need to activate it. Type the following command and press Enter:

```Bash
source llm_env/bin/activate
```

Once activated, you'll see the name of your virtual environment (llm_env) in parentheses at the beginning of your Terminal prompt, like this: (llm_env) $. This tells you that the virtual environment is active.

## Step 4: Install Dependencies
Now that the virtual environment is active, you can install the Python packages your project needs. For example, to install azure-search-documents and azure-identity, use the following commands:

```Bash
pip install --upgrade --quiet azure-search-documents
pip install --upgrade --quiet azure-identity
```

You can find more info about azure search with langchain here: (langchain vector store : azure search)[https://python.langchain.com/docs/integrations/vectorstores/azuresearch/#install-azure-ai-search-sdk]

The --upgrade flag ensures you get the latest versions, and --quiet keeps the output clean.

## Step 5: Deactivate the Virtual Environment
When you're finished working on your project and want to exit the virtual environment, simply type:

```Bash
deactivate
```

The (llm_env) part will disappear from your Terminal prompt, indicating that the virtual environment is no longer active.

# Notes
Virtual environments are essential for managing dependencies and preventing conflicts between different Python projects.

Always activate the virtual environment before installing or running Python packages for your project.

You can name your virtual environment anything you like (e.g., myenv, project_venv). Just replace llm_env with your chosen name in the commands.

Now you're ready to start building your Python project in a clean and organized environment! 🚀