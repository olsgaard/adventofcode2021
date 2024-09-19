from collections import defaultdict

example = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()

def compute_directory_sizes(commands: str) -> defaultdict:
    dirsizes = defaultdict(int)
    path = ['/']
    commands = commands.split("\n")
    first_command = commands.pop(0)
    assert "first_command == $ cd /", f"'{first_command}'"
    for command in commands:
        if command.startswith("$ cd"):
            _prompt, cmd, arg = command.split()
            if arg == "..":
                path.pop()
            else:
                path.append(path[-1]+'/'+ arg)
        elif command.startswith("$ ls") or command.startswith("dir"):
            continue
        else:
            for p in path:
                dirsizes[p] += int(command.split()[0])
    return dirsizes

def solution1(commands: str) -> int:
    dirsizes = compute_directory_sizes(commands)
    total = sum([v for v in dirsizes.values() if v < 100000])
    return total

def solution2(commands: str) -> int:
    total_disk_space = 70000000
    needed_disk_space = 30000000
    dirsizes = compute_directory_sizes(commands)
    currently_available = total_disk_space - int(dirsizes['/'])
    space_needed = needed_disk_space - currently_available
    space_to_be_deleted = min([v for v in dirsizes.values() if v >= space_needed])
    return space_to_be_deleted

with open("day7_input.txt") as f:
    input_text = f.read().strip()
    print("Solution 1:", solution1(input_text))
    print("Solution 2:", solution2(input_text))