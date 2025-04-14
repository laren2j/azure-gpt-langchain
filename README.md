# Setting Up a Python Virtual Environment (`venv`)

Let's get started with creating a safe space for your Python projects! We'll use something called a "virtual environment" to keep things organized. Think of it as a separate little container where you can install Python packages without messing up your main Python setup.

This guide covers how to do this on **Windows** using WSL (Windows Subsystem for Linux). If you're on a Mac or Linux, you can find a separate guide here: [**macOS/Linux**](./MAC-README.md).

## Prerequisites

## Step 0: Checking if Python is Ready

First, we need to make sure you have Python installed. Open your **Windows Terminal** or **PowerShell** and type this, then press Enter:

```sh
python3 --version
```
If you see a version number like Python 3.9.6, you're good! If you get an error, don't worry, we'll fix that in the next step.

## Step 1: Installing Python (if needed) Inside WSL

If Python isn't installed, you'll need to install it inside WSL. To do this, type these commands one by one into your Windows Terminal or PowerShell, pressing Enter after each:

```sh
wsl
sudo apt update
sudo apt install python3 python3-venv python3-pip
```
*`wsl` starts your Windows Subsystem for Linux.
*`sudo apt update` refreshes the list of available software.
*`sudo apt install python3 python3-venv python3-pip` installs Python 3, the `venv` module (for creating virtual environments), and `pip` (a tool for installing Python packages).

## Step 2: Creating Your Project Folder

Now, let's create a folder for your project. Decide where you want to keep your project files. For this example, we'll create a folder called "llm" on your Desktop.

In your Windows Terminal or PowerShell (with WSL running), type these commands:

```sh
cd /mnt/c/Users/your_username/Desktop/
mkdir llm
cd llm
```

* Replace `your_username` with your actual Windows username.
* `cd /mnt/c/Users/your_username/Desktop/` moves you to your Desktop folder.
* `mkdir llm` creates a new folder named "llm".
* `cd llm` moves you into the "llm" folder.

## Step 3: Making the Virtual Environment
Inside your project folder, create the virtual environment. We'll call it `azure-gpt-langchain_env`. Type this command and press Enter:

```sh
python3 -m venv azure-gpt-langchain_env
```

This creates a new folder called `azure-gpt-langchain_env` inside your project folder. This is where all the packages for your project will live.

## Step 4: Activating the Virtual Environment
To start using the virtual environment, you need to "activate" it. Type this and press Enter:

```sh
source azure-gpt-langchain_env/bin/activate
```

You'll know it's activated when you see `(azure-gpt-langchain_env)` at the beginning of your command prompt, like this: `(azure-gpt-langchain_env) $`.

## Step 5: Installing the Packages You Need
Now, let's install the Python packages your project needs. For this example, we'll install `azure-search-documents` and `azure-identity`. Type these commands, pressing Enter after each:

```sh
pip install --upgrade --quiet azure-search-documents
pip install --upgrade --quiet azure-identity
```

* `pip install` installs the packages.
* `--upgrade` makes sure you get the latest versions.
* `--quiet` keeps the output clean.

(You can find more info about azure search with langchain here: [langchain vector store : azure search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/#install-azure-ai-search-sdk)
)

## Step 6: Leaving the Virtual Environment
When you're done working on your project, you can "deactivate" the virtual environment. Type this and press Enter:

```sh
deactivate
```
The `(azure-gpt-langchain_env)` will disappear from your command prompt.

# Important Things to Remember

* **WSL Access:** /mnt/c/ lets you access your Windows files from inside WSL.
* **Keep Things Separate:** Virtual environments keep your project's packages separate, which is super important!
* **Always Activate:** Make sure you activate your virtual environment before installing or running anything for your project.

You're all set! Have fun building your project! 🚀