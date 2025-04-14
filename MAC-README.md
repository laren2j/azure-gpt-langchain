# Setting Up a Python Virtual Environment (`venv`) on macOS

This guide will walk you through creating and activating a Python virtual environment using `venv` on your Mac. Virtual environments help keep your project's dependencies separate, which is super useful!

## Step 0: Checking if Python is Ready

First, let's see if Python 3 is already installed. Open your **Terminal** application. You can find it by going to **Finder** -> **Applications** -> **Utilities** -> **Terminal**.

In the Terminal, type this command and press Enter:

```Bash
python3 --version
```

If you see a version number like `Python 3.9.6`, you're good to go! If you get an error message saying "command not found" or something similar, you'll need to install Python 3. You can download the latest version from the official Python website (python.org).

## Step 1: Making Your Project Folder
Now, let's create a folder for your project. Decide where you want to keep your project files. For this example, we'll create a folder called "azure-gpt-langchain" on your Desktop.

In your Terminal, type these commands one by one, pressing Enter after each:

```Bash
cd Desktop
mkdir azure-gpt-langchain
cd azure-gpt-langchain
```

* `cd Desktop` moves you to your Desktop folder.
* `mkdir azure-gpt-langchain` creates a new folder named "azure-gpt-langchain".
* `cd azure-gpt-langchain` moves you into the "azure-gpt-langchain" folder.

## Step 2: Making the Virtual Environment
Inside your project folder, create the virtual environment. We'll call it `azure-gpt-langchain_env`. Type this command and press Enter:

```Bash
python3 -m venv azure-gpt-langchain_env
```

This creates a new folder called `azure-gpt-langchain_env` inside your project folder. This is where all the packages for your project will live.

## Step 3: Activate the Virtual Environment
To start using the virtual environment, you need to activate it. Type the following command and press Enter:

```Bash
source azure-gpt-langchain_env/bin/activate
```

You'll know it's activated when you see `(azure-gpt-langchain_env)` at the beginning of your command prompt, like this: `(azure-gpt-langchain_env) $`.

## Step 4: Installing the Packages You Need
Now, let's install the Python packages your project needs. For this example, we'll install `azure-search-documents` and `azure-identity`. Type these commands, pressing Enter after each:

```Bash
pip install --upgrade --quiet azure-search-documents
pip install --upgrade --quiet azure-identity
```

* `pip install` installs the packages.
* `--upgrade` makes sure you get the latest versions.
* `--quiet` keeps the output clean.

You can find more info about azure search with langchain here: (langchain vector store : azure search)[https://python.langchain.com/docs/integrations/vectorstores/azuresearch/#install-azure-ai-search-sdk]

## Step 5: Leaving the Virtual Environment
When you're done working on your project, you can "deactivate" the virtual environment. Type this and press Enter:

```Bash
deactivate
```

The `(azure-gpt-langchain_env)` will disappear from your command prompt.

# Important Things to Remember
* **Keep Things Separate:** Virtual environments keep your project's packages separate, which is super important!
* **Always Activate:** Make sure you activate your virtual environment before installing or running anything for your project.
* **Name It What You Want:** You can name your virtual environment anything you like (e.g., `myenv`,` project_venv`). Just replace `azure-gpt-langchain_env` with your chosen name in the commands.

You're all set! Have fun building your project! 🚀