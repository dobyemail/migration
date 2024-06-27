# migration

migration between email accounts  Email Migration Tool Preview  Migrating your emails to a new email address or changing the mail provider can be a challenging task. That tool helps you to migrate your emails to a new account. No chaos with multiple email addresses in your mail program, lost data or undeliverable emails.


### Usage

You can run the script from the command line with arguments similar to the `imapsync` tool:

```sh
python sync.py --host1 test1.lamiral.info --port1 993 --user1 test1 --password1 "secret1" --host2 test2.lamiral.info --port2 993 --user2 test2 --password2 "secret2"
```

### Explanation

1. **Argument Parsing:** The script uses the `argparse` module to parse the command-line arguments.
2. **Command-line Arguments:** Users can provide the source and destination IMAP servers, ports, usernames, and passwords as command-line arguments.
3. **Folders:** The script lists all folders in the source IMAP account and migrates the emails to the corresponding folders in the destination account.
4. **Exception Handling:** Basic error handling is implemented to manage connection issues and email fetching problems.


### Notes

- **Security:** Be cautious when passing passwords as command-line arguments since they can be visible in the shell history and process list. It’s safer to read sensitive information from a secure file or environment variable.
- **Testing:** Test the script with a few folders and emails to ensure it functions as expected before proceeding with a full migration.
- **Improvements:** You can enhance the script by adding more robust error handling, logging, and handling specific IMAP folder structures.




For the given script, you'll need:

- `argparse` (though this is part of the Python standard library and doesn't need to be listed separately)
- `imaplib` (also part of the Python standard library)
- `email` (also part of the Python standard library)

Since all these modules are part of the standard library, a minimal `requirements.txt` isn't strictly necessary. However, if you're using a virtual environment or making sure your project has a proper setup, it's good practice to have a `requirements.txt` for future scalability or additional dependencies.

If you plan to enhance the script, you might consider adding external packages for logging, configuration, or advanced email manipulation (like `mailbox`). For now, here’s a minimal example `requirements.txt` that you might use:

### Optional Packages for Enhanced Functionality
If you want to extend functionality, you could add external libraries. Here’s an enhanced `requirements.txt` including two additional packages for demonstrating purposes:

- `pytz` for timezone-aware dates (useful for IMAP operations)
- `requests` to fetch credentials securely from a web service, etc.

Here's what your `requirements.txt` might look like:

```txt
# requirements.txt

# These packages are standard libraries and need not be included
# argparse (Standard Library)
# imaplib (Standard Library)
# email (Standard Library)

# Add these if you plan to extend functionality
pytz==2023.2
requests==2.31.0
```

### Steps to Create and Use `requirements.txt`

1. **Create `requirements.txt`:**
   Create the `requirements.txt` file in the same directory as your script and insert the content above.

2. **Install Packages from `requirements.txt`:**

   Use the following command to install packages listed in `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```
