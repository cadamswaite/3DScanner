def start_it():
    from random import randint
    with open('temp.ply', 'w') as f:
        f.write("")

def plotit(x,y,z):
    with open('temp.ply', 'a') as f:
        f.write(str(x) + " " + str(y) + " " + str(z) + "\n")

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def finish_it():
    with open('temp.ply', 'r') as f:
        file = f.read()
    with open('plot2.ply', 'w') as f:
        f.write("""ply
format ascii 1.0
element vertex """ + str(file_len('temp.ply')) + """
property float x
property float y
property float z
element face 0
property list uchar int vertex_indices
end_header
""" + file)
