import csv
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
            logging.info(f"Loaded {len(rows)} rows from {filename}")
            return header, rows
    except FileNotFoundError:
        logging.error("CSV file not found.")
        print("❌ data.csv not found. Please check the file.")
        return None, None
    except StopIteration:
        logging.error("CSV file is empty.")
        print("❌ CSV file is empty.")
        return None, None


def clean_data(rows):
    if not rows:
        return []

    cleaned = []
    for row in rows:
        if all(cell.strip() != "" for cell in row):
            cleaned.append(row)

    logging.info(f"Cleaned data: {len(cleaned)} valid rows found")
    return cleaned


def save_data(filename, header, rows):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    header, rows = load_data("data.csv")

    if header is None:
        return

    cleaned_rows = clean_data(rows)
    save_data("clean_data.csv", header, cleaned_rows)
    print("✅ Cleaning complete! clean_data.csv created.")


if __name__ == "__main__":
    main()
