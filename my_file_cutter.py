import os
import tarfile


def do_split(filename, file_array):
    i = 1
    with open(filename, "r") as src:
        fil = "chunk_"+str(i)+".txt"
        file_array.append(fil)
        out = open(fil, "w")
        for line in src:
            # change according to chun k size(10mb for now)
            if os.stat(fil).st_size <= 10000000:
                out.write(line)
            else:
                out.close()
                i = i + 1
                fil = "chunk_"+str(i)+".txt"
                file_array.append(fil)
                out = open(fil, "w")
            out.close()
        src.close()
    return file_array


def main():
    # get file name from args ?
    filename = "t1.txt"
    # gz compressed tar ball
    tar = tarfile.open(filename+"_chunks.tar.gz", "w:gz")
    # change according to min file size (10 for now)
    if os.stat(filename) <= 10000000:
        tar.add(filename)
        tar.close()
        print("file is less than min size")
    else:
        file_array = []
        files = do_split(filename, file_array)
        for fil in files:
            tar.add(fil)
            os.remove(fil)
        tar.close()


if __name__ == "__main__":
    main()
