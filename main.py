from src.exporter import fetch_users
from src.analyzer import process_data
from src.database import save_to_db
from src.visualizer import draw_chart

def main():
    print("Starting ETL pipeline...")
    fetch_users()
    process_data()
    save_to_db()
    print("Generating dashboard...")
    draw_chart()

if __name__ == '__main__':
    main()