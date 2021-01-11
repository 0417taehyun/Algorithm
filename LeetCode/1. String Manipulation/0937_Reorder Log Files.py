def reorderLogFiles(logs: list[str]) -> list[str]:
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        letters = sorted(letters, key = lambda item: (item.split()[1], item.split()[2]))
        return letters + digits
    

if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(reorderLogFiles(logs))
