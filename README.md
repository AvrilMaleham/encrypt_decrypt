# encrypt_decrypt

This Python script allows you to **encode text into numbers** and **decode numbers back into text** using a customizable cipher system.

## 🚀 How it Works

### 🧾 Inputs:

1. A **string**: Either plain text (for encoding) or a numeric string (for decoding)
2. A **mode**: `"encode"` or `"decode"`
3. An **even number** (required **only** for `"encode"` mode)

---

### 🔤 Encoding Logic

- Each letter **A–Z** is mapped to a number starting from the provided even number (which must be between 10-40), increasing in increments of **2**:
  - `A = starting_number`
  - `B = starting_number + 2`
  - `C = starting_number + 4`
  - ... and so on.
- Special characters are encoded as:
  - Space (` `) → `1`
  - Comma (`,`) → `3`
  - Full stop (`.`) → `5`
  - Newline (`\n`) → `7`
  - Single quote (`'`) → `9`
- At the end of the encoded string, the script appends:
  13579<starting_number>
  This helps with decoding later.

---

### 🔁 Decoding Logic

- Extracts the number after the `"13579"` marker to determine the base value used for encoding `A`.
- Reverses the mapping using the same increment logic (increments of 2).
- Replaces special values (1, 3, 5, 7, 9) back with their respective characters.

---

## 🛠️ Example Usage

```python
encrypt_decrypt("encode", "hello world", 10)
# Returns: '24183232380154384432161357910'

encrypt_decrypt("decode", "24183232380154384432161357910")
# Returns: 'HELLO WORLD'

```
