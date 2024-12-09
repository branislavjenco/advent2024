diskmap = ""

with open("input.txt") as f:
    diskmap = f.read().strip()

def diskmap_to_blocks(diskmap):
    blocks = []
    for i, ch in enumerate(diskmap):
        for j in range(int(ch)):
            if i % 2 == 0:
                blocks.append(i // 2)
            else:
                blocks.append(".")
    return blocks


def find_next_backfill_i(blocks, current):
    if blocks[current] != ".":
        return current
    else:
        new = current
        while blocks[new] == ".":
            new -= 1
        return new

def fix_blocks(blocks):
    backfill_i = len(blocks) - 1
    i = 0
    while i < backfill_i:
        if blocks[i] == ".":
            backfill_i = find_next_backfill_i(blocks, backfill_i)
            if backfill_i < i:
                break
            blocks[i] = blocks[backfill_i]
            blocks[backfill_i] = "."
            backfill_i -= 1
        i += 1
    return blocks

def checksum(blocks):
    i = 0
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != ".":
            checksum += int(blocks[i]) * i
    return checksum

blocks = diskmap_to_blocks(diskmap)
print("Part 1", checksum(fix_blocks(blocks.copy())))

def blocks_to_files(blocks):
    files = []
    curr_ch = blocks[0]
    curr_file = [curr_ch]
    i = 1
    while i < len(blocks):
        nex = blocks[i]
        if nex != curr_ch:
            files.append(curr_file)
            curr_file = [nex]
        else:
            curr_file.append(curr_ch)
        curr_ch = blocks[i]
        i += 1
    files.append(curr_file)
    return files
        

def is_free(space):
    if len(space) == 0:
        return 0
    return space[0] == "."

files = blocks_to_files(blocks)
i = len(files) - 1
while i > 0:
    # print("".join(["".join([str(x) for x in file]) for file in files]))
    file = files[i]
    if is_free(file):
        i -= 1
        continue
    l = len(file)
    j = 0
    spliced = False
    while j < i:
        space = files[j] 
        if is_free(space):
            if l <= len(space):
                files.insert(j, file)
                files[i+1]  =["." for _ in range(l)] 
                files[j+1] = ["." for _ in range(len(space) - l)]
                spliced = True
                break
        j += 1
    i -= 1
                
def files_to_blocks(files):
    blocks = []
    for file in files:
        blocks.extend(file)
    return blocks

blocks = files_to_blocks(files)
print(blocks[:100])
print("Part 2", checksum(blocks))
