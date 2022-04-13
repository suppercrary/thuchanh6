from typing import TextIO
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    line = reader.readline()
    if not line:
        return None
    key, name= line.split()
    molecule = [name]

    serial_numer=1
    reading=True
    while reading:
        line= reader.readline()
        if line.startswith("END"):
            reading=False
        else:
            key, num, atom_type,x,y,z =line.split()
            if int(num)!=serial_numer:
                print("bádabasl".format(serial_numer,num))
                molecule.append([atom_type,x,y,z])
        serial_numer+=1

    return molecule

def read_all_molecules(reader: TextIO) -> list:
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('bt8_multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)