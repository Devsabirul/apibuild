def writeModel(tablename,fields):
    file_name = './core/models.py'
    open_file = open(file_name, 'r')
    read_line = open_file.readlines()
    open_file.close()

    field_definitions = []

    for i in fields:
        removespace = ''.join(i['fieldname'].split())
        field = removespace.lower()
        field_definitions.append(f"{field} = models.{i['type']}(max_length={i['length']}, null={i['null']}, blank={i['blank']} )")

    # Create the model class
    model_class = f'\n\nclass {tablename}(models.Model):\n\t'
    model_class += '\n\t'.join(field_definitions)
    read_line.insert(len(read_line),model_class)

    

    # Reopen the file in write mode and write the modified content
    open_file = open(file_name, 'w')
    open_file.writelines(read_line)
    open_file.close()
    return True