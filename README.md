# canvas-quiz-to-csv

`canvas-quiz-to-csv` is a small script to convert a graded multiple-choice quiz from Canvas to a CSV file. The CSV file can then be imported into services like Quizlet. It uses BeautifulSoup to extract the text from a Canvas page saved as an HTML file.

## Installation
1. Download and install [Python](https://www.python.org/downloads/)
2. Open a Terminal or PowerShell window
3. Clone this repo: `git clone https://github.com/rajivshah3/canvas-quiz-to-csv`
4. Switch to the cloned directory: `cd canvas-quiz-to-csv`
5. Install the dependencies: `pip install -r requirements.txt` (on macOS: `pip3 install -r requirements.txt`)

## Usage
1. Navigate to your Canvas quiz and save it as an HTML file (in Google Chrome, go to File > Save Page As and choose the location to save the file in)
2. Run `python main.py` (on macOS: `python3 main.py`) and paste the path of the HTML file (for example: `/Users/rajiv/Downloads/Module 3 Quiz.html`) when prompted

You can now use the resulting CSV file with Quizlet's import feature. When creating a set, click "Import from Word, Excel, Google Docs, etc." and paste the contents of your CSV file. Make sure to switch the "Between term and definition" setting to "Comma".
