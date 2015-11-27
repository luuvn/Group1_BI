import random
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('ISO-8859-1')

#DATA
SVM_DIR = 'data/vne.txt'
SVM_FORMAT_DIR = 'data/svm/svm_formated'
SVM_TRAIN_DIR = 'data/svm/svm_train'
SVM_TEST_DIR = 'data/svm/svm_test'
SVM_PART_DIR = 'data/svm/svm_part'
SVM_MERGE_DIR = 'data/svm/svm_merge'
SVM_BALANCE_DIR = 'data/svm/svm_balance'

SVM_MOBILE_KEY = 1
SVM_DESKTOP_KEY = -1

def formatFile():
    #Format data for SVM
    content = ''
    with open(SVM_DIR, "r") as f:
        lines = f.readlines()
        item_list = lines[0].split("\r")
        for line in item_list[1:]:
            test_list = line.split("\t")
            key = 1
            if test_list[14] == 'General_Mobile':
                key = SVM_MOBILE_KEY
            else:
                key = SVM_DESKTOP_KEY
            content += str(key) + " "
            content += str(textCount) + ":" + test_list[0]

            # for word in test_list:
            #     if word != test_list[0]:
            #         content += str(textCount) + ":" + word + ' '
            #         textCount += 1

            content += "\n"
    print(content)

    if not os.path.isdir('data/svm'):
        os.makedirs('data/svm')

    with open(SVM_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def checkData(data):
    mobileList = []
    desktopList = []

    for s in data:
        if s.startswith('1'):
            mobileList.insert(0,s)
        else:
            desktopList.insert(0,s)

    print("-------------------")
    print("Total: ", len(data))
    print("Mobile Number: ", len(mobileList))
    print("Desktop Number: ", len(desktopList))
    print("-------------------")

def splitDataPercent(train, test):
    formatDir = SVM_FORMAT_DIR
    trainDir = SVM_TRAIN_DIR
    testDir = SVM_TEST_DIR

    data = []

    with open(formatDir, "r") as f:
        for word in f.read().split('\n'):
            if len(word) > 0:
                data.insert(0,word)

    random.shuffle(data)
    countData = len(data)
    print("countData", countData)
    itemTrainNum = int(round((train * countData)/100))
    print("itemTrainNum", itemTrainNum)
    itemTestNum = countData - itemTrainNum
    print("itemTestNum", itemTestNum)

    train_data = data[:itemTrainNum]
    test_data = data[itemTrainNum:]

    checkData(train_data)
    checkData(test_data)

    testContent = ''
    trainContent = ''

    with open(trainDir, 'w') as f:
        f.write('\n'.join(train_data))
        f.write('\n')

    with open(testDir, 'w') as f:
        f.write('\n'.join(test_data))
        f.write('\n')

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[ i * length // wanted_parts: (i + 1) * length // wanted_parts]
             for i in range(wanted_parts) ]

def saveDataPartFile(part_list ,partNum):
    partDir = SVM_PART_DIR
    print("Part Count", len(part_list))
    checkData(part_list)

    content = ''
    file_dir = partDir + str(partNum)
    with open(file_dir, 'w') as f:
        f.write('\n'.join(part_list))
        f.write('\n')

def splitDataPartNum(num):
    formatDir = SVM_FORMAT_DIR
    data = []
    with open(formatDir, "r") as f:
        for word in f.read().split('\n'):
            if len(word) > 0:
                data.insert(0, word)
        # data = f.read().split('\n')
    random.shuffle(data)
    countData = len(data)
    print("countData", countData)

    for x in range(0, num):
        saveDataPartFile(split_list(data, num)[x], x)

def mergeList(testNum, rangeNum):
    partDir = SVM_PART_DIR
    mergeDir = SVM_MERGE_DIR

    data = []
    for x in range(0, rangeNum):
        if x != testNum:
            print("MergeCount", str(x) + " | " + str(testNum))
            file_dir = partDir + str(x)
            with open(file_dir, "r") as f:
                for word in f.read().split('\n'):
                    if len(word) > 0:
                        data.insert(0, word)
                # data += f.read().split('\n')
    print("MergeCount", len(data))

    checkData(data)

    content = ''
    file_dir = mergeDir + str(testNum)
    with open(file_dir, 'w') as f:
        f.write('\n'.join(data))
        f.write('\n')

def calculatePRF(tp, fn, fp, tn):
    # P (Precision) = TP / (TP + FP) (True positives / All predicted positives)
    # R (Recall) = TP / (TP + FN) (True positives / All actual positives)
    # F1 = 2 * ((P * R) / (P + R))

    p = tp / (tp + fp)
    r = tp / (tp + fn)
    f1 = 2 * ((p * r) / (p + r))

    print('Precision: ', str(p))
    print('Recall: ', str(r))
    print('F1 Score: ', str(f1))

def calculateAvg(input):
    data = input.split(' ')
    sumList = 0
    for x in data:
        sumList += float(x)
    result = sumList / len(data)
    print("AVG: ", result)

def main():
    oper = -1
    while int(oper) != 0:
        print('**************************************')
        print('Choose one of the following: ')
        print('1 - SVM - Format Data')
        print('2 - SVM - Split Data 80 - 20')
        print('3 - SVM - Split Data to 5 fold')
        print('4 - SVM - Merge Data for fold training')
        print('5 - Calculate Precision, Recall and F1 score')
        print('6 - Calculate Average of Result')
        print('0 - Exit')
        print('**************************************')
        oper = int(input("Enter your options: "))

        if oper == 0:
            exit()
        elif oper == 1:
            formatFile()
        elif oper == 2:
            splitDataPercent(80,20)
        elif oper == 3:
            splitDataPartNum(5)
        elif oper == 4:
            for x in range(0, 5):
                mergeList(x,5)
        elif oper == 5:
            #tp, fn, fp, tn
            tp = int(input("Enter True Positives(TP): "))
            fn = int(input("Enter False Negatives(FN): "))
            fp = int(input("Enter False Positives(FP): "))
            tn = int(input("Enter True Negatives(TN): "))
            calculatePRF(tp,fn,fp,tn)
        elif oper == 6:
            data = input("Enter values: ")
            calculateAvg(data)

if __name__ == "__main__":
    main()
