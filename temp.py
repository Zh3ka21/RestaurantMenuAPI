from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "123456789"
stored_hash = "$2b$12$YpsSEk7MNuVFjZEaTg/yJuNEHnMp1nX8pRNcL0XcEDJy7fTMloPcm"  # The one from your DB

# Verify if the password matches the stored hash
print(pwd_context.verify(password, stored_hash))  # Should print: True
