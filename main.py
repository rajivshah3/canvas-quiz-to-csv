from bs4 import BeautifulSoup
import csv

path = input("Enter path to read from: ")
htmlF = open(path, "r")
html_doc = htmlF.read()
soup = BeautifulSoup(html_doc, "html.parser")

outName = input("Enter name of CSV to output (default: output.csv): ") or "output.csv"
outRows = []

questions = soup.find_all(class_="question_holder")

for question in questions:
    qText = question.find(class_="question_text").text.strip()
    correctAnswer = question.find(class_="correct_answer").find(class_="answer_text").text.strip()
    outRows.append([qText, correctAnswer])

htmlF.close()
csvF = open(outName, "w")

csvwriter = csv.writer(csvF)
csvwriter.writerows(outRows)
csvF.close()
