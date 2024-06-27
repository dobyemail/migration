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
