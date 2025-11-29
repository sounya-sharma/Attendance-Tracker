from MyQR import myqr
import os
import time
f = open('QR_Attendance\\students.txt','r')
lines = f.read().split("\n")
print(lines)

# Create a folder if it doesn't exist
qr_dir = 'QR_Attendance\\qr-codes'
if not os.path.exists(qr_dir):
    os.makedirs(qr_dir)

for _ in range (0,len(lines)):
    data = lines[_]
    if data.strip():  # Skip empty lines
        qr_name = f"{data}.png"
        version,level,qr = myqr.run(
            str(data),
            level='H',
            version=1,
            colorized=True,
            contrast=1.0,
            brightness=1.0,
            save_name = qr_name,
            save_dir=qr_dir
        )