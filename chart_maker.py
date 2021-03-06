import pandas as pd
import matplotlib.pyplot as plt


class ChartMaker:
    def __init__(self, csv_name: str, num_of_pages: int) -> None:
        self.csv_name = csv_name
        self.num_of_pages = num_of_pages

    def make_a_bar_chart(self):
        pd.options.display.float_format = "{:,.2f}".format
        df = pd.read_csv(f"{self.csv_name}.csv")
        df.drop_duplicates(subset=None, inplace=True)
        df["price_in_kc"] = df["price_in_kc"].astype(float)
        grouped_df = df.groupby("locality")
        mean_df = grouped_df.mean()
        mean_df = mean_df.reset_index()
        plt.ticklabel_format(style="plain")
        plt.bar(mean_df["locality"], mean_df["price_in_kc"])
        plt.title(
            f"Average price of a flat in Prague based on Sreality.cz offers\n(first {self.num_of_pages} {'pages' if self.num_of_pages > 1 else 'page'})",
            fontsize=14,
        )
        plt.xlabel("Locality", fontsize=14)
        plt.ylabel("Price", fontsize=14)
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(["{:,.0f} Kč".format(x) for x in current_values])
        plt.show()
