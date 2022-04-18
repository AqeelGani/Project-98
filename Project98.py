from tokenize import Name


def SwapFileData():
    file1Name = input('Enter Your File Name : ')
    file2Name = input('Enter Your File Name : ')
    file1 = open(file1Name)
    file2 = open(file2Name)
    file1Data = file1.read()
    file2Data = file2.read()
    with open(file1Name, 'w') as f1:
        f1.write(file2Data)
    with open(file2Name, 'w') as f2:
        f2.write(file1Data)
    print('File Data Swapped Successfully!')

SwapFileData()