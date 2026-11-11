# Simple XOR Shellcode Encoder

A small Python utility for studying how bytewise XOR changes the representation of a byte array. Applying the same key twice recovers the original bytes.

## Run locally

```sh
python XOR_SHELLCODE.py
```

The sample byte array and XOR key are defined in [XOR_SHELLCODE.py](XOR_SHELLCODE.py). The script prints the transformed bytes as hexadecimal escape sequences.
