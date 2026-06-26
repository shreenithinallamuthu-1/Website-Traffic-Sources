import csv
import os
import matplotlib.pyplot as plt
import pandas as pd


def get_next_serial_number(filename):
    """Calculates the next serial number by looking past the descriptive title block header."""
    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
        return 1

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = list(csv.reader(file))
            # Find where the actual data rows start (skipping our descriptive headers)
            data_rows = [row for row in reader if row and row[0].isdigit()]
            if not data_rows:
                return 1
            # Get the S.No from the last data row
            return int(data_rows[-1][0]) + 1
    except (IndexError, ValueError):
        return 1


def generate_all_charts(filename):
    """Reads the CSV file, correctly skipping the descriptive title block to display the interactive charts."""
    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
        print(
            "\n[Warning] No data available in the CSV yet to generate charts."
        )
        return

    try:
        # Load data using pandas, skipping the first 2 layout rows
        df = pd.read_csv(filename, skiprows=2)

        if df.empty:
            print("\n[Warning] The CSV file is empty.")
            return

        # Ensure correct column parsing names after skip
        df.columns = df.columns.str.strip()

        # --- DATA PROCESSING ---
        df_visitors = (
            df.groupby("Source Name")["Monthly Visitors"].sum().reset_index()
        )
        df_visitors = df_visitors.sort_values(
            by="Monthly Visitors", ascending=False
        )

        df_bounce = (
            df.groupby("Source Name")["Bounce Rate (%)"].mean().reset_index()
        )
        df_bounce = df_bounce.sort_values(by="Bounce Rate (%)", ascending=False)

        pie_colors = [
            "#3498db",
            "#2ecc71",
            "#e74c3c",
            "#f1c40f",
            "#9b59b6",
            "#1abc9c",
        ]

        print("\n[Rendering Charts...] Close each window to view the next one.")

        # --- CHART 1: MONTHLY VISITORS BAR CHART ---
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(
            df_visitors["Source Name"],
            df_visitors["Monthly Visitors"],
            color="#3498db",
            edgecolor="#2980b9",
            alpha=0.9,
        )
        ax1.set_title(
            "Total Monthly Visitors by Traffic Source",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax1.set_xlabel("Traffic Source Name", fontsize=12, labelpad=10)
        ax1.set_ylabel("Monthly Visitors", fontsize=12, labelpad=10)
        ax1.grid(axis="y", linestyle="--", alpha=0.5)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

        # --- CHART 2: MONTHLY VISITORS PIE CHART ---
        fig2, ax2 = plt.subplots(figsize=(7, 7))
        ax2.pie(
            df_visitors["Monthly Visitors"],
            labels=df_visitors["Source Name"],
            autopct="%1.1f%%",
            startangle=140,
            colors=pie_colors[: len(df_visitors)],
            textprops={"fontsize": 11},
        )
        ax2.set_title(
            "Percentage Share of Monthly Visitors",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        plt.tight_layout()
        plt.show()

        # --- CHART 3: BOUNCE RATE BAR CHART ---
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        ax3.bar(
            df_bounce["Source Name"],
            df_bounce["Bounce Rate (%)"],
            color="#e67e22",
            edgecolor="#d35400",
            alpha=0.9,
        )
        ax3.set_title(
            "Average Bounce Rate (%) by Traffic Source",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax3.set_xlabel("Traffic Source Name", fontsize=12, labelpad=10)
        ax3.set_ylabel("Bounce Rate (%)", fontsize=12, labelpad=10)
        ax3.grid(axis="y", linestyle="--", alpha=0.5)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"\n[Error] Could not display charts: {e}")


def collect_traffic_data():
    filename = "website_traffic_data.csv"

    # Columns structure setup
    headers = [
        "S.No.",
        "Source Type",
        "Source Name",
        "Monthly Visitors",
        "Bounce Rate (%)",
    ]
    file_exists = os.path.isfile(filename)

    print("=" * 60)
    print("      WEBSITE TRAFFIC DATA COLLECTOR & INTERACTIVE VISUALIZER")
    print("=" * 60)
    print(f"Data will be saved to: {os.path.abspath(filename)}\n")

    current_sno = get_next_serial_number(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # If the file is brand new, create a descriptive header summary block (Without Date/Time)
        if not file_exists:
            writer.writerow(
                ["REPORT TITLE:", "WEBSITE TRAFFIC SOURCES AND PERFORMANCE DATA"]
            )
            writer.writerow(
                ["-" * 15, "-" * 50]
            )  # Clean visual divider row block
            writer.writerow(headers)  # Actual data table headers

        while True:
            print("-" * 40)
            print("Enter details for a new traffic source:")

            # 1. Get Source Type
            print("Select Source Type:")
            print("1. Organic Search (e.g., Google, Bing)")
            print("2. Social Media (e.g., LinkedIn, Instagram)")
            print("3. Paid Ads (e.g., PPC, Meta Ads)")
            print("4. Direct / Referral / Other")

            choice = input("Enter choice (1-4) or type the name directly: ")
            if choice == "1":
                source_type = "Organic Search"
            elif choice == "2":
                source_type = "Social Media"
            elif choice == "3":
                source_type = "Paid Ads"
            elif choice == "4":
                source_type = "Direct/Referral/Other"
            else:
                source_type = choice if choice.strip() else "Unknown"

            # 2. Get specific Source Name
            source_name = input(
                "Enter specific source name (e.g., Google, Newsletter, Facebook): "
            ).strip()
            if not source_name:
                source_name = "Not Specified"

            # 3. Get Monthly Visitors
            while True:
                try:
                    visitors = int(
                        input("Enter number of monthly visitors: ")
                    )
                    if visitors < 0:
                        print("Visitors cannot be negative. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # 4. Get Bounce Rate
            while True:
                try:
                    bounce_rate = float(
                        input("Enter bounce rate percentage (e.g., 42.5): ")
                    )
                    if 0 <= bounce_rate <= 100:
                        break
                    else:
                        print("Bounce rate must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid percentage.")

            # Save the background incremented S.No, leaving IDLE terminal print statements clean
            writer.writerow(
                [current_sno, source_type, source_name, visitors, bounce_rate]
            )
            print("\n Data successfully saved to CSV!")

            current_sno += 1

            cont = (
                input("\nDo you want to add another traffic source? (y/n): ")
                .strip()
                .lower()
            )
            if cont != "y":
                print("\nExiting data entry interface...")
                break

    generate_all_charts(filename)
    print("Thank you for using the program!")


if __name__ == "__main__":
    collect_traffic_data()
