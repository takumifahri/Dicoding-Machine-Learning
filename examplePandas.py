
import pandas as pd


data = {
    "Nama": ["Fahri", "Budi", "Siti"],
    "Umur": [25, 30, 22],
    "Kota": ["Jakarta", "Bandung", "Yogyakarta"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)