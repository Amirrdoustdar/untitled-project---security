# User Security Information System

This project is a Python-based user security system that allows users to securely store and manage personal information. The system encrypts user details, creates unique usernames, and stores them in a JSON file. Additionally, it ensures that no duplicate user data is stored.

## Features

### User Information Collection
The program collects personal information such as:
- Name
- Age
- Gender
- Grade
- Major
- Social account

### Unique Username Generation
If a user tries to create an account with an existing username, the system will automatically generate a unique username by appending a counter to the base username.

### Data Encryption
User information is encrypted for privacy, including social account usernames.

### Data Storage
The information is securely stored in a JSON file (`user_security_info.json`) for later retrieval and updates.

### Data Integrity Check
The system prevents storing duplicate information. If the same user details are entered, an error message is returned.

## New in Version 1.1

### 🚀 Improvements and New Features:

#### Advanced Encryption
The system now uses SHA-256 for encryption, providing a higher level of security for user data.

#### Enhanced Input Validation
- Added validation for user inputs such as name (only alphabetic characters) and age (must be between 0 and 120).

#### Social Account Validation
- Improved regex pattern to validate social account URLs more accurately.

#### User Management
- **Delete User:** Added functionality to delete user data securely.
- **Search User:** Users can now be searched based on keywords in their encrypted information.
- **Update User:** Improved user information update functionality with timestamp tracking.

#### Backup System
- Added a backup feature to create a backup of the user data in a separate JSON file (`user_security_info_backup.json`).

#### Logging System
- Implemented a logging mechanism to track all activities and errors, stored in `security.log`.

#### Unit Tests
- Added unit tests to ensure the system's reliability and correctness. Tests cover encryption, input validation, and social account validation.

## Installation

1. Clone the repository or download the Python file.
2. Ensure Python 3.x is installed on your system.
3. You do not need to install any external libraries for this project, as it only uses the built-in `json`, `datetime`, and `re` libraries.

## Usage

1. **Run the Script:** Execute the Python script in your terminal or preferred Python IDE.

2. **Input User Information:**
   - The system will prompt you to enter personal details such as:
     - Name
     - Age
     - Gender
     - Grade
     - Major
     - Social Account

3. **Unique Username Creation:**
   - You will be prompted to enter a desired username.
   - If the username already exists, the system will automatically append a number (e.g., `username_1`, `username_2`, ...) to create a unique username.

4. **Data Encryption:**
   - All personal information (including social account usernames) will be encrypted for security purposes before being stored.

5. **Data Storage:**
   - Your encrypted user information will be stored in `user_security_info.json`.
   - The program checks for existing data, preventing duplicate entries.

6. **Error Handling:**
   - If the same user information is entered more than once, an error will be displayed indicating that the information already exists.

## Example

When you run the script, the following prompts will appear:

```bash
Enter your name: John Doe
Enter your age: 25
Enter your gender: Male
Enter your grade: A
Enter your major: Computer Science
Enter your social account: Facebook:www.facebook.com/johndoe
Enter a desired username: johndoe
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with a descriptive message.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your code adheres to the existing code style and includes relevant tests.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided that you include the original license file in your distribution.

For more details, see the [LICENSE](LICENSE) file.
