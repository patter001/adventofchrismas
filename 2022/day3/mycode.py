# https://adventofcode.com/2022/day/3
import pdb

with open("input.txt") as f:
    input = f.read()

# with open("test_input.txt") as f:
#     input = f.read()

# with open("part2_test_input.txt") as f:
#     input = f.read()    

DEBUG = 1
# with open("input.txt") as f:
#     input = f.read()

def part1():
    rucksacks = input.splitlines()
    priorities = []
    for s, sack in enumerate(rucksacks):
        halfway = len(sack)//2
        comp1, comp2 = sack[:halfway], sack[halfway:]
        common = set(comp1).intersection(set(comp2))
        assert len(common)==1, f"you have a bug: {common}, line {s}"
        checkit = common.pop()
        # ugly one liner's
        priority = (ord(checkit.upper()) + 1) - ord("A") + (checkit.isupper())*26
        # OR, dont do conversion do check
        # priority = (ord(checkit) + 1) - (ord("A") if checkit.isupper() else ord("a")) + (checkit.isuper())*26    
        priorities.append(priority)
        if DEBUG:
            print(f"{s}:{checkit}:{priority}")
    print(sum(priorities))

def part2():
    rucksacks = input.splitlines()
    priorities = []
    def check_group(group):
        common = group[0].intersection(group[1]).intersection(group[2])
        assert len(common)==1, f"you have a bug: {common}, line {s}"
        checkit = common.pop()
        # ugly one liner's
        priority = (ord(checkit.upper()) + 1) - ord("A") + (checkit.isupper())*26
        # OR, dont do conversion do check
        # priority = (ord(checkit) + 1) - (ord("A") if checkit.isupper() else ord("a")) + (checkit.isuper())*26    
        priorities.append(priority)
        if DEBUG:
            print(f"{s}:{checkit}:{priority}")

    group = []
    for s, sack in enumerate(rucksacks):
        group.append(set(sack))
        if len(group)<3:
            continue
        check_group(group)
        group = []
    print(sum(priorities))
