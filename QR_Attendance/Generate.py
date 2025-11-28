from MyQR import myqr
import os

f = open('students.txt','r')
lines = f.read().split("\n")
print(lines)

# Create bca folder if it doesn't exist
if not os.path.exists('bca'):
    os.makedirs('bca')

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
            save_dir='bca'
        )