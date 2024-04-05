def read_file(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

def write_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    file1 = "file1.txt"
    file2 = "file2.txt"
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    same_lines = lines1.intersection(lines2)
    diff_lines = lines1.symmetric_difference(lines2)

    write_file("same.txt", sorted(same_lines))
    write_file("diff.txt", sorted(diff_lines))

    print("Результати збережено у файлах 'same.txt' та 'diff.txt'.")

if __name__ == "__main__":
    main()
