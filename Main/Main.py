from Generator import generate
from Gui import run_gui
import  logging
def main():
    generate(8)
    run_gui()

if __name__ == "__main__":
    main()
    logging.info(f"password ")