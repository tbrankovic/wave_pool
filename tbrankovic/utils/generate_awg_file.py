# auteur : Jules M.
def generate_awg_file(signal, awg_file_path):
    # Créer un fichier texte compatible avec l'AWG
    with open(awg_file_path, 'w') as file:
        for amp in signal:
            file.write(f'{amp:.9e},0,0\n')

    print(f'Generated AWG file with success: {awg_file_path}')
