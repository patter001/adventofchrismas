# https://adventofcode.com/2022/day/4

with open("input.txt") as f:
    input = f.read()

# with open("test1.txt") as f:
#     input = f.read()

# with open("test2.txt") as f:
#     input = f.read()
# 
def part1a():
    # just curious if it could be done in one line, but got stuck on how to do more without a 
    # a function or without repeating an opertion
    assignments = [
        #bool()
        (   
            range(*list((map(int,a[0].split("-"))))),
            range(*list(map(int,a[1].split("-"))))
        )
         for a in 
        [a for a in [l.split(",") for l in input.splitlines()]]
    ]
    #counts = [if ]
    return assignments


def part1b():
    # more readable
    from collections import namedtuple
    GroupBase = namedtuple("GoupBase", ["min","max"])

    def group_from_str(thestr):
        min, max = thestr.split("-")
        return GroupBase(int(min),int(max))

    def groups_from_assignemtns(thestr):
        groups = thestr.split(",")
        return group_from_str(groups[0]), group_from_str(groups[1])
    
    def overlaps(group0,group1):
        return (
            (group0.min<=group1.min and group0.max>=group1.max)
            or
            (group1.min<=group0.min and group1.max>=group0.max)
        )

    all_groups = [groups_from_assignemtns(l) for l in input.splitlines()]
    overlaps = [ overlaps(*g) for g in all_groups]
    return sum(overlaps)

def part2a():
    # just curious if it could be done in one line but it is 2x as slow as 2b
    return sum([
        bool(   
            set(range(*
                [i+j for i,j in enumerate(map(int,a[0].split("-")))
                ])) 
                &
            set(range(*
                [i+j for i,j in enumerate(map(int,a[1].split("-")))
                ])) 
        )
         for a in 
        [a for a in [l.split(",") for l in input.splitlines()]]
    ])


def part2b():
    # more readable
    from collections import namedtuple
    GroupBase = namedtuple("GoupBase", ["min","max"])

    def group_from_str(thestr):
        min, max = thestr.split("-")
        return GroupBase(int(min),int(max))

    def groups_from_assignemtns(thestr):
        groups = thestr.split(",")
        return group_from_str(groups[0]), group_from_str(groups[1])
    
    def overlaps(group0,group1):
        return (
            (group0.min<=group1.min and group1.min<=group0.max)
            #group1.min-group0.min>=0 and group0.max-group1.min>0
            or
            (group1.min<=group0.min and group0.min<=group1.max)
        )

    all_groups = [groups_from_assignemtns(l) for l in input.splitlines()]
    overlaps = [ overlaps(*g) for g in all_groups]
    return sum(overlaps)

print(part2a())