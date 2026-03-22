from reader import read_file
from analyzer import analyze
from reporter import generate_report

file = input("Enter log file name: ")

lines = read_file(file)

error, warning, info, total = analyze(lines)

generate_report(error, warning, info, total)