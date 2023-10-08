import os
def writeModel(tablename, fields):
    file_name = './core/models.py'
    open_file = open(file_name, 'r')
    read_line = open_file.readlines()
    open_file.close()

    field_definitions = []

    for i in fields:
        removespace = ''.join(i['fieldname'].split())
        field = removespace.lower()
        if i['type'] == 'CharField':
            field_definitions.append(
                f"{field} = models.{i['type']}(max_length={i['length']}, null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'IntegerField':
            field_definitions.append(
                f"{field} = models.{i['type']}(null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'BooleanField':
            field_definitions.append(
                f"{field} = models.{i['type']}(default=True,null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'DateTimeField':
            field_definitions.append(
                f"{field} = models.{i['type']}(auto_now=True, null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'DecimalField':
            field_definitions.append(
                f"{field} = models.{i['type']}(max_digits={i['length']}, null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'EmailField':
            field_definitions.append(
                f"{field} = models.{i['type']}(max_length={i['length']}, null={i['null']}, blank={i['blank']},unique=True )")
        elif i['type'] == 'FileField':
            field_definitions.append(
                f"{field} = models.{i['type']}(upload_to='file_uploads/',default=None, null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'ImageField':
            field_definitions.append(
                f"{field} = models.{i['type']}(upload_to='iamges_uploads/',default=None, null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'PositiveIntegerField':
            field_definitions.append(
                f"{field} = models.{i['type']}(null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'TextField':
            field_definitions.append(
                f"{field} = models.{i['type']}(null={i['null']}, blank={i['blank']} )")
        elif i['type'] == 'UUIDField':
            field_definitions.append(
                f"{field} = models.{i['type']}(default=uuid.uuid4,editable=False,unique=True )")
        elif i['type'] == 'ForeignKey':
            field_definitions.append(
                f"{field} = models.{i['type']}({i['model_names']},on_delete=models.CASCADE)")
        elif i['type'] == 'ManyToManyField':
            field_definitions.append(
                f"{field} = models.{i['type']}({i['model_names']})")
        elif i['type'] == 'OneToOneField':
            field_definitions.append(
                f"{field} = models.{i['type']}({i['model_names']},on_delete=models.CASCADE)")
        elif i['type'] == 'JSONField':
            field_definitions.append(
                f"{field} = models.{i['type']}(default=dict,null={i['null']}, blank={i['blank']})")
        elif i['type'] == 'SlugField':
            field_definitions.append(
                f"{field} = models.{i['type']}(max_length={i['length']},unique=True,null={i['null']}, blank={i['blank']})")

    checktablename = checkmodelsfile(tablename, file_name)
    if checktablename != True:
        # Create the model class
        model_class = f'\n\nclass {tablename}(models.Model):\n\t'
        model_class += '\n\t'.join(field_definitions)
        read_line.insert(len(read_line), model_class)

        # Reopen the file in write mode and write the modified content
        open_file = open(file_name, 'w')
        open_file.writelines(read_line)
        open_file.close()
        writeadminfile(tablename)
        return True
    return False



def checkmodelsfile(tablename, filepath):
    openfile = open(filepath, 'rt')
    readfile = openfile.read()
    if f"class {tablename}(models.Model):" in readfile:
        return True
    return False


def writeadminfile(tablename):
    file_name = './core/admin.py'
    open_file = open(file_name, 'r')
    read_line = open_file.readlines()
    open_file.close()

    read_line.insert(len(read_line),f"\nadmin.site.register({tablename})")

    # Reopen the file in write mode and write the modified content
    open_file = open(file_name, 'w')
    open_file.writelines(read_line)
    open_file.close()
    print("NICE")
