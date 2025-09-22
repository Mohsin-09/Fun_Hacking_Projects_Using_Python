# 49_backup_encrypt.md
Example command to encrypt backups with openssl:
openssl enc -aes-256-cbc -salt -in backup.tar -out backup.tar.enc
Always manage keys securely.
