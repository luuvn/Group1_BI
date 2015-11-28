import random
import re
import os
from dtree import *
from id3 import *
import sys
import pickle

reload(sys)
sys.setdefaultencoding('ISO-8859-1')
sys.setrecursionlimit(30000)

#DATA
SVM_DIR = 'data/vne.txt'
SVM_FORMAT_DIR = 'data/svm/svm_formated'
SVM_TRAIN_DIR = 'data/svm/svm_train'
SVM_TEST_DIR = 'data/svm/svm_test'
SVM_PART_DIR = 'data/svm/svm_part'
SVM_MERGE_DIR = 'data/svm/svm_merge'
SVM_BALANCE_DIR = 'data/svm/svm_balance'

#Maxent
MAXENT_DIR = 'data/vne.txt'
MAXENT_FORMAT_DIR = 'data/maxent/maxent_formated'
MAXENT_TRAIN_DIR = 'data/maxent/maxent_train'
MAXENT_TEST_DIR = 'data/maxent/maxent_test'
MAXENT_PART_DIR = 'data/maxent/maxent_part'
MAXENT_MERGE_DIR = 'data/maxent/maxent_merge'
MAXENT_BALANCE_DIR = 'data/maxent/maxent_balance'

TEST_DIR = 'data/data5.txt'

TEST_DUMP_DIR = 'data/dc_dump'

CONNECT_SQL = ""

SVM_MOBILE_KEY = 1
SVM_DESKTOP_KEY = -1

def formatSVM():
    #Format data for SVM
    content = ''
    textCount = 1
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
            content += "\n"
    print(content)

    if not os.path.isdir('data/svm'):
        os.makedirs('data/svm')

    with open(SVM_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def formatMaxent():
    content = ''
    data = []
    colArray = [15]
    with open(MAXENT_DIR, "r") as f:
        lines = f.readlines()
        item_list = lines[0].split("\r")
        for line in item_list[1:]:
            test_list = line.split("\t")
            content += test_list[14] + "\t"

            for temp in colArray:
                content += test_list[temp] + ","
            content = content[:-1]
            content += "\n"
    print(content)

    if not os.path.isdir('data/maxent'):
        os.makedirs('data/maxent')

    with open(MAXENT_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def formatSQL():
    cnxn = pyodbc.connect(CONNECT_SQL)
    cursor = cnxn.cursor()
    cursor.execute("select user_id, user_name from users")
    lines = cursor.fetchall()

    textCount = 1

    for line in lines:
        if line.device_type == 'General_Mobile':
            key = SVM_MOBILE_KEY
        else:
            key = SVM_DESKTOP_KEY
        content += str(key) + " "
        content += str(textCount) + ":" + line.device_id
        content += "\n"
    print(content)
    if not os.path.isdir('data/svm'):
        os.makedirs('data/svm')

    with open(SVM_FORMAT_DIR, "w") as file:
        file.write(content)
    file.close()
    print("Format Text Completed!!!")

def checkData(data, isMaxent):
    mobileList = []
    desktopList = []

    if isMaxent:
        for s in data:
            if s.startswith('General_Mobile'):
                mobileList.insert(0,s)
            else:
                desktopList.insert(0,s)
    else:
        for s in data:
            if s.startswith('1'):
                mobileList.insert(0,s)
            else:
                desktopList.insert(0,s)

    print("-------------------")
    print("Total: ", len(data))
    print("Mobile Version View Number: ", len(mobileList))
    print("Desktop Version View Number: ", len(desktopList))
    print("-------------------")

def splitDataPercent(train, test, isMaxent):
    if isMaxent:
        formatDir = MAXENT_FORMAT_DIR
        trainDir = MAXENT_TRAIN_DIR
        testDir = MAXENT_TEST_DIR
    else:
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

    checkData(train_data, isMaxent)
    checkData(test_data, isMaxent)

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

def saveDataPartFile(part_list ,partNum, isMaxent):
    if isMaxent:
        partDir = MAXENT_PART_DIR
    else:
        partDir = SVM_PART_DIR
    print("Part Count", len(part_list))
    checkData(part_list, isMaxent)

    content = ''
    file_dir = partDir + str(partNum)
    with open(file_dir, 'w') as f:
        f.write('\n'.join(part_list))
        f.write('\n')

def splitDataPartNum(num, isMaxent):
    if isMaxent:
        formatDir = MAXENT_FORMAT_DIR
    else:
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

def mergeList(testNum, rangeNum, isMaxent):
    if isMaxent:
        partDir = MAXENT_PART_DIR
        mergeDir = MAXENT_MERGE_DIR
    else:
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

    checkData(data, isMaxent)

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

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object.
    """

    if type(tree) == dict:
        print "%s%s" % (str, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (str, item)
            print_tree(tree.values()[0][item], str + "\t")
    else:
        print "%s\t->\t%s" % (str, tree)

def run_des_test():
    # Create a list of all the lines in the data file
    lines = []
    with open(TEST_DIR, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        lines = lines[0].split("\r")

    # Remove the attributes from the list of lines and create a list of
    # the attributes.
    lines.reverse()
    attributes = [attr.strip() for attr in lines.pop().split("\t")]

    target_attr = attributes[-1]

    lines.reverse()

    # Create a list of the data in the data file
    data = []

    if os.path.exists(TEST_DUMP_DIR):
        with open(TEST_DUMP_DIR, 'rb') as f:
            data = pickle.load(f)
    else:
        for line in lines:
            data.append(dict(zip(attributes,
                                 [datum.strip() for datum in line.split("\t")])))

        with open(TEST_DUMP_DIR, 'wb') as f:
            pickle.dump(data, f)

    random.shuffle(data)
    print(data)

    testData = data[:1000]

    # Copy the data list into the examples list for testing
    examples = testData

    # Create the decision tree
    tree = create_decision_tree(testData, attributes, target_attr, gain)

    # Classify the records in the examples list
    classification = classify(tree, examples)

    # Print out the classification for each record
    for item in classification:
        print item

    return tree

def decisionTree():
    print "------------------------\n"
    print "--   Classification   --\n"
    print "------------------------\n"
    print "\n"
    tree = run_des_test()
    print "\n"
    print "------------------------\n"
    print "--   Decision Tree    --\n"
    print "------------------------\n"
    print "\n"
    print_tree(tree, "")

def main():
    oper = -1
    while int(oper) != 0:
        print('**************************************')
        print('Choose one of the following: ')
        print('1 - SVM - Format Data')
        print('2 - SVM - Split Data 80 - 20')
        print('3 - SVM - Split Data to 5 fold')
        print('4 - SVM - Merge Data for fold training')
        print('5 - Maxent - Format Data')
        print('6 - Maxent - Split Data 80 - 20')
        print('7 - Maxent - Split Data to 5 fold')
        print('8 - Maxent - Merge Data for fold training')
        print('9 - Calculate Precision, Recall and F1 score')
        print('10 - Calculate Average of Result')
        print('11 - Decision Tree')
        print('0 - Exit')
        print('**************************************')
        oper = int(input("Enter your options: "))

        if oper == 0:
            exit()
        elif oper == 1:
            formatSVM()
        elif oper == 2:
            splitDataPercent(80,20, False)
        elif oper == 3:
            splitDataPartNum(5, False)
        elif oper == 4:
            for x in range(0, 5):
                mergeList(x,5, False)
        elif oper == 5:
            formatMaxent()
        elif oper == 6:
            splitDataPercent(80,20, True)
        elif oper == 7:
            splitDataPartNum(5, True)
        elif oper == 8:
            for x in range(0, 5):
                mergeList(x,5, True)
        elif oper == 9:
            #tp, fn, fp, tn
            tp = int(input("Enter True Positives(TP): "))
            fn = int(input("Enter False Negatives(FN): "))
            fp = int(input("Enter False Positives(FP): "))
            tn = int(input("Enter True Negatives(TN): "))
            calculatePRF(tp,fn,fp,tn)
        elif oper == 10:
            data = input("Enter values: ")
            calculateAvg(data)
        elif oper == 11:
            decisionTree()

if __name__ == "__main__":
    main()
