import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.float_format = "{:,.2f}".format

df = pd.read_csv("properties.csv")
df["price_in_kc"] = df["price_in_kc"].astype(float)
grouped_df = df.groupby("locality")
mean_df = grouped_df.mean()
mean_df = mean_df.reset_index()
plt.ticklabel_format(style="plain")
plt.bar(mean_df["locality"], mean_df["price_in_kc"])
plt.title("Prices of flats in Prague based on Sreality.cz offers", fontsize=14)
plt.xlabel("Locality", fontsize=14)
plt.ylabel("Price", fontsize=14)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(["{:,.0f} Kč".format(x) for x in current_values])
plt.show()
