import pandas as pd
import requests
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# AMFI Codes
scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            filename = f"data/raw/nav_{code}.csv"

            nav_df.to_csv(filename, index=False)

            print(f"✅ Saved: {filename}")

        else:
            print(f"❌ Failed for {code}")

    except Exception as e:
        print(f"❌ Error for {code}: {e}")

print("NAV data download completed.")