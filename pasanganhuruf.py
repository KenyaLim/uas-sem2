def pasanganHuruf(s):
    if len(s) <= 2:
        return 0
    if s[0] == s[2]:
        return 1 + pasanganHuruf(s[1:])
    elif s[0]!=s[2]:
        return 0+pasanganHuruf(s[1:])

# Main program
print(pasanganHuruf("ababa"))  # Expected output: 3
print(pasanganHuruf("acay"))   # Expected output: 1
print(pasanganHuruf("bxbxx"))  # Expected output: 2
print(pasanganHuruf("kukuruyuk"))  # Expected output: 4
