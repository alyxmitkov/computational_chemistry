import sys
import os

def read_xyz_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_atoms = int(lines[0].strip())
            symbols = []
            coordinates = []

            for line in lines[2:]:  
                data = line.split()
                if len(data) >= 4:  
                    symbols.append(data[0])
                    coordinates.append([float(data[i]) for i in range(1, 4)])
                else:
                    print(f"Ignoring invalid line: {line}")

            return num_atoms, symbols, coordinates
    except Exception as e:
        print(f"An error occurred while reading the XYZ file: {e}")
        return None, None, None

def count_unpaired_electrons(symbols, atomic_charges):
    try:
        num_unpaired_electrons = sum(atomic_charges.get(symbol, 0) for symbol in symbols)
        return num_unpaired_electrons
    except Exception as e:
        print(f"An error occurred while counting unpaired electrons: {e}")
        return None

def calculate_multiplicity(num_unpaired_electrons):
    try:
        if num_unpaired_electrons % 2 == 0:
            return 1  
        else:
            return 2  
    except Exception as e:
        print(f"An error occurred while calculating multiplicity: {e}")
        return None

def calculate_total_electrons(symbols, atomic_charges):
    try:
        total_electrons = sum(atomic_charges.get(symbol, 0) for symbol in symbols)
        return total_electrons
    except Exception as e:
        print(f"An error occurred while calculating total electrons: {e}")
        return None

def calculate_molecular_charge(symbols, atomic_charges):
    
    total_charge = sum(atomic_charges.get(symbol, 0) for symbol in symbols)
    return total_charge

def calculate_vibrational_dof(num_atoms, is_linear):
    try:
        if is_linear:
            return 3 * num_atoms - 5
        else:
            return 3 * num_atoms - 6
    except Exception as e:
        print(f"An error occurred while calculating vibrational degrees of freedom: {e}")
        return None

def write_to_output_file(file_path, multiplicity, total_electrons, total_charge, vibrational_dof, molecule_name, is_linear, num_atoms):
    try:
        with open(file_path, "w") as output_file:
            output_file.write(" __  __       _                 _            \n")
            output_file.write("|  \\/  | ___ | | ___  ___ _   _| | __ _ _ __ \n")
            output_file.write("| |\/| |/ _ \\| |/ _ \\/ __| | | | |/ _` | '__|\n")
            output_file.write("| |  | | (_) | |  __/ (__| |_| | | (_| | |   \n")
            output_file.write("|_| _|_|\\___/|_|\\___|\\___|\\__,_|_|\\__,_|_|   \n")
            output_file.write("   / \\   _ __   __ _| |_   _ ___(_)___       \n")
            output_file.write("  / _ \\ | '_ \\ / _` | | | | / __| / __|      \n")
            output_file.write(" / ___ \\| | | | (_| | | |_| \\__ \\ \\__ \\      \n")
            output_file.write("/_/   \\_\\_| |_|\\__,_|_|\\__, |___/_|___/      \n")
            output_file.write("                       |___/                   \n")

            output_file.write('\n')  

            output_file.write("Molecular Analysis Data\n")
            output_file.write("Developed by Alyx Mitkov\n")
            output_file.write("Version 0.1\n")
            output_file.write('\n')  
            output_file.write(f"This molecular analysis reveals essential characteristics of the analyzed structure. The script extracts information from an XYZ file, including the number of atoms, atomic symbols, and coordinates. Utilizing predefined atomic charges, it calculates the total number of unpaired electrons, determining the multiplicity of the molecular system. The script further computes the total number of electrons and the resulting molecular charge. These findings are presented in this output file, offering insights into the molecular properties. The program also outputs the vibrational degrees of freedom calculated on the basis of the molecular linearity given as a terminal argument and the number of atoms.\n")
            output_file.write('\n')
            output_file.write(f"Molecule Name: {molecule_name}\n")
            output_file.write(f"Total Number of Atoms: {num_atoms}\n")
            output_file.write(f"Molecule Type: {'Linear' if is_linear else 'Non-linear'}\n")
            output_file.write('\n')
            output_file.write(f"Total Molecular Charge: {total_charge}\n")
            output_file.write(f"Total Electrons: {total_electrons}\n")
            output_file.write(f"Multiplicity: {multiplicity}\n")
            output_file.write('\n')
            output_file.write(f"Vibrational Degrees of Freedom: {vibrational_dof}\n")
            
        print(f"Output written to {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python combined_script.py file.xyz linear/nonlinear")
        sys.exit(1)

    xyz_file_path = sys.argv[1]
    molecule_type = sys.argv[2].lower()
    molecule_name, _ = os.path.splitext(os.path.basename(xyz_file_path))
    
    atomic_charges = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5,
                      'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
                      'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15,
                      'S': 16, 'Cl': 17, 'K': 19, 'Ar': 18, 'Ca': 20,
                      'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25,
                      'Fe': 26, 'Ni': 28, 'Co': 27, 'Cu': 29, 'Zn': 30,
                      'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35,
                      'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40,
                      'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45,
                      'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50,
                      'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55,
                      'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60,
                      'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65,
                      'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
                      'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75,
                      'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
                      'Tl': 81, 'Pb': 82, 'Bi': 83, 'Th': 90, 'Pa': 91,
                      'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96,
                      'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100, 'Md': 101,
                      'No': 102, 'Lr': 103, 'Rf': 104, 'Db': 105, 'Sg': 106,
                      'Bh': 107, 'Hs': 108, 'Mt': 109, 'Ds': 110, 'Rg': 111,
                      'Cn': 112, 'Nh': 113, 'Fl': 114, 'Mc': 115, 'Lv': 116,
                      'Ts': 117, 'Og': 118}

    num_atoms, symbols, coordinates = read_xyz_file(xyz_file_path)
    if num_atoms is None or symbols is None or coordinates is None:
        sys.exit(1)

    num_unpaired_electrons = count_unpaired_electrons(symbols, atomic_charges)
    if num_unpaired_electrons is None:
        sys.exit(1)

    multiplicity = calculate_multiplicity(num_unpaired_electrons)
    if multiplicity is None:
        sys.exit(1)

    total_electrons = calculate_total_electrons(symbols, atomic_charges)
    if total_electrons is None:
        sys.exit(1)

    total_charge = calculate_molecular_charge(symbols, atomic_charges)

    vibrational_dof = calculate_vibrational_dof(num_atoms, molecule_type == 'linear')
    if vibrational_dof is None:
        sys.exit(1)
    is_linear = molecule_type == 'linear'
    
    input_file_name, _ = os.path.splitext(os.path.basename(xyz_file_path))
    output_file_path = f"{input_file_name}_molecular_analysis.out"

    
    write_to_output_file(output_file_path, multiplicity, total_electrons, total_charge, vibrational_dof, molecule_name, is_linear, num_atoms)

if __name__ == "__main__":
    main()
