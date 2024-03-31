# Python Web Scraper

This is a Python-based web scraping project that checks for broken links on a given website. It uses Selenium for web navigation and Requests for HTTP requests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

You also need to have the following Python libraries installed:
- selenium~=4.19.0
- requests~=2.31.0

You can install these using pip:
```bash
pip install -r requirements.txt
```

### Installing

Clone the repository to your local machine:
```bash
git clone https://github.com/TurgayArif/link-checker-py.git
```

Navigate to the project directory:
```bash
cd link-checker-py
```

Run the main script:
```bash
python main.py
```

## Usage

The script navigates to a given website, finds all the anchor tags on the page, checks for duplicate links, and then visits each unique link to check if it's broken or not. It prints the status of each link and the total number of broken links found.

You can change the website to be checked by modifying the `BASE_URL` variable in `main.py`.

## Built With

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Requests](https://docs.python-requests.org/en/master/)

## Authors

- Turgay Arif

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to Selenium and Requests for making this project possible.
- Thanks to all contributors to this project.
