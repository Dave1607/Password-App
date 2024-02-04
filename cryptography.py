import hashlib

#hashing algorithm using SHA-256
def hash_password(password):
    # Hash the combined data using a secure hashing algorithm (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

#Comparing passwords for equality, taking in the hashed and plain text password
def check_password(stored_password, provided_password):
    """
        Checks if the provided password matches the stored one (encrypted).
        
        :param stored_password: Encrypted password from database.
        :type stored_password: bytes
        :param provided_password: Password provided by user for comparison.
        :type provided_password: str
        :return: True if passwords match, False otherwise.
        :rtype: bool
    """
    hashed_password = hash_password(provided_password)
    # Compare the two encrypted passwords
    if hashed_password == stored_password:
        return True
    else:
        return False