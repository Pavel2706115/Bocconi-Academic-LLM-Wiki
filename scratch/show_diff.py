import difflib

file1 = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Sources\30067 ECONOMIC HISTORY\6_The industrialisation process_2.md"
file2 = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\scratch\6_test_out.md"

with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

diff = difflib.unified_diff(
    f1_lines, f2_lines,
    fromfile="original", tofile="cleaned",
    n=3
)

with open(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\scratch\diff.txt", "w", encoding="utf-8") as df:
    df.writelines(diff)

print("Diff report written successfully.")
