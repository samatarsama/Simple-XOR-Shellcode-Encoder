import base64


raw_shellcode = (

)

shellcode = bytes(raw_shellcode, 'latin1') 

xor_key = 0x41
xor_encrypted = bytes([b ^ xor_key for b in shellcode])

lines = []
line = ""
for i, byte in enumerate(xor_encrypted):
    line += f"\\x{byte:02x}"
    if (i + 1) % 16 == 0:
        lines.append(f"\"{line}\"")
        line = ""
if line: 
    lines.append(f"\"{line}\"")

print("\nHave Funn hacking here is your Encrypted shellcode ;D:\n")
print("(\n" + "\n".join(lines) + "\n)")
