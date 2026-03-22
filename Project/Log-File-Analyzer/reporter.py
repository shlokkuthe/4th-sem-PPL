def generate_report(error, warning, info, total):
    
    if total > 0:
        e_per = (error / total) * 100
        w_per = (warning / total) * 100
        i_per = (info / total) * 100
    else:
        e_per = w_per = i_per = 0

    if error > warning:
        severity = "HIGH"
    elif warning > info:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    print("\n--- LOG SUMMARY ---")
    print("Total Lines:", total)
    print("Errors:", error, "(", round(e_per,2), "% )")
    print("Warnings:", warning, "(", round(w_per,2), "% )")
    print("Info:", info, "(", round(i_per,2), "% )")
    print("System Severity:", severity)

    # save to file
    f = open("report.txt", "w")
    f.write("LOG SUMMARY\n")
    f.write("Total Lines: " + str(total) + "\n")
    f.write("Errors: " + str(error) + "\n")
    f.write("Warnings: " + str(warning) + "\n")
    f.write("Info: " + str(info) + "\n")
    f.write("Severity: " + severity + "\n")
    f.close()