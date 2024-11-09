import json
from datetime import datetime
import re

class Security:
    def __init__(self):
        self.storage_file = "user_security_info.json"
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                self.stored_data = json.load(f)
                # Ensure stored_data is a dictionary
                if not isinstance(self.stored_data, dict):
                    self.stored_data = {}
        except (FileNotFoundError, json.JSONDecodeError):
            self.stored_data = {}

    def get_user_input(self):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender: ")
        grade = input("Enter your grade: ")
        major = input("Enter your major: ")
        socialaccount = input("Enter your social account: ")
        
        user_info = f"Name: {name} Age: {age} Gender: {gender} Grade: {grade} Major: {major} socialaccount: {socialaccount}"
        return user_info

    def create_unique_username(self, base_username):
        """
        Generates a unique username based on the base username.
        """
        username = base_username
        counter = 1
        while username in self.stored_data:
            username = f"{base_username}_{counter}"
            counter += 1
        return username

    def encrypt(self, s):
        def get_weight(char):
            return ord(char) - 96
        
        def encrypt_uniform(uniform_str):
            if not uniform_str:
                return ""
            weight = get_weight(uniform_str[0])
            return ''.join(str(weight * (i + 1)) for i in range(len(uniform_str)))
        
        if not s:
            return 0

        result = ''.join(encrypt_uniform(substring) for char, substring in zip(s, s.split(char)))
        return int(result) if result else 0

    def is_social_account_info(self, param):
        pattern = r'^[A-Z][a-zA-Z]*:www\.[a-z0-9\.]+/[a-zA-Z0-9_]+$'
        return bool(re.match(pattern, param))

    def secure(self, info):
        def encrypt_social(word):
            prefix = word[:word.rfind('/')+1]
            username = word[word.rfind('/')+1:]
            encrypted_username = str(self.encrypt(username))
            return prefix + encrypted_username

        words = info.split()
        result_words = [encrypt_social(word) if self.is_social_account_info(word) else word for word in words]
        return ' '.join(result_words)

    def store_user_info(self, user_info, username=None):
        # Encrypt information
        secured_info = self.secure(user_info)

        # Check for existing user data
        for data in self.stored_data.values():
            if data["encrypted_info"] == secured_info:
                return False, "Error: User information already exists."

        # Prompt for a base username and create a unique one
        if not username:
            base_username = input("Enter a desired username: ")
            username = self.create_unique_username(base_username)

        timestamp = datetime.now().isoformat()
        user_data = {
            "encrypted_info": secured_info,
            "timestamp": timestamp,
            "last_modified": timestamp
        }

        self.stored_data[username] = user_data

        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(self.stored_data, f, indent=4, ensure_ascii=False)
            return True, f"Data saved successfully with username: {username}"
        except IOError as e:
            return False, f"Error saving data: {str(e)}"

    def get_user_info(self, username):
        if username in self.stored_data:
            return True, self.stored_data[username]
        return False, "User NOT FOUND"

    def update_user_info(self, username, new_info):
        if username in self.stored_data:
            secured_info = self.secure(new_info)
            self.stored_data[username]["encrypted_info"] = secured_info
            self.stored_data[username]["last_modified"] = datetime.now().isoformat()
            
            try:
                with open(self.storage_file, 'w', encoding='utf-8') as f:
                    json.dump(self.stored_data, f, indent=4, ensure_ascii=False)
                return True, "Database updated successfully"
            except IOError as e:
                return False, f"Error updating data: {str(e)}"
        return False, "User NOT FOUND"

# Using the Security class
sec = Security()
user_info = sec.get_user_input()
save_status, message = sec.store_user_info(user_info)

print(message)
