Mining Phase:

## Tool:
We write a small python tool to work with data

To run it:
>python ./formatData.py

```
**************************************
Choose one of the following: /n
1 - SVM - Format Data
2 - SVM - Split Data 80 - 20
3 - SVM - Split Data to 5 fold
4 - SVM - Merge Data for fold training
5 - Maxent - Format Data
6 - Maxent - Split Data 80 - 20
7 - Maxent - Split Data to 5 fold
8 - Maxent - Merge Data for fold training
9 - Calculate Precision, Recall and F1 score
10 - Calculate Average of Result
11 - Decision Tree
0 - Exit
**************************************
```

## MaximumEntropyDemo
MaximumEntropyDemo use the Stanford Classifier

Example:
>java -jar ./tools/maxent/stanford-classifier-3.5.2.jar  -prop ./tools/maxent/basic.prop

### Sample Result

```
Reading dataset from ./data/maxent/maxent_train ... done [1.6s, 220620 items].
numDatums: 220620
numDatumsPerLabel: {General_Desktop=34970.0, General_Mobile=185650.0}
numLabels: 2 [General_Mobile, General_Desktop]
numFeatures (Phi(X) types): 105834 [CLASS, 1-SW-CINK PEAX, 1-SW-77678, 1-SW-540x960, 1-SW-2014-01-19, ...]
................................................................

......
General_Mobile	General_Mobile	1.000	1.000
General_Mobile	General_Mobile	1.000	1.000
General_Mobile	General_Mobile	1.000	1.000
General_Mobile	General_Mobile	1.000	1.000
General_Mobile	General_Mobile	0.981	0.981
General_Mobile	General_Mobile	1.000	1.000
General_Desktop	General_Desktop	0.974	0.974
General_Desktop	General_Desktop	0.981	0.981
General_Mobile	General_Mobile	0.998	0.998
General_Mobile	General_Mobile	1.000	1.000
General_Mobile	General_Mobile	1.000	1.000
General_Desktop	General_Desktop	0.970	0.970
General_Mobile	General_Mobile	0.999	0.999
General_Mobile	General_Mobile	0.985	0.985
General_Mobile	General_Desktop	0.872	0.128
......

55156 examples in test set
Cls General_Mobile: TP=46103 FN=391 FP=93 TN=8569; Acc 0.991 P 0.998 R 0.992 F1 0.995
Cls General_Desktop: TP=8569 FN=93 FP=391 TN=46103; Acc 0.991 P 0.956 R 0.989 F1 0.973
Accuracy/micro-averaged F1: 0.99122
Macro-averaged F1: 0.98366
```

## Support Vector Machine Tool:
SVM Light
We write a script to run this tool easier

>./doTest.sh

###Sample Result:
```
SVM-light Version V6.02
0 # kernel type
3 # kernel parameter -d 
1 # kernel parameter -g 
1 # kernel parameter -s 
1 # kernel parameter -r 
empty# kernel parameter -u 
1 # highest feature index 
220620 # number of training documents 
571 # number of support vectors plus 1 
-0.14145269 # threshold b, each following line is a SV (starting with alpha*y)
-6.2517540115473171488420724663444e-10 1:52596 #
6.2517540115473171488420724663444e-10 1:47581 #
-6.2517540115473171488420724663444e-10 1:306 #
6.2517540115473171488420724663444e-10 1:82276 #
-6.2517540115473171488420724663444e-10 1:82277 #
6.2517540115473171488420724663444e-10 1:1 #
-6.2517540115473171488420724663444e-10 1:306 #
6.2517540115473171488420724663444e-10 1:82275 #
-6.2517540115473171488420724663444e-10 1:82259 #
......

Runtime (without IO) in cpu-seconds: 0.02
Accuracy on test set: 84.40% (46551 correct, 8605 incorrect, 55156 total)
Precision/recall on test set: 84.40%/100.00%
```
-----------------

## Decision Tree
Run tool with option 11

###Sample Result:

```
SCREEN_RESOLUTION
	1200x720
	DEVICE_NAME
		iPhone
			->	General_Mobile
		HTC Glacier
			->	General_Desktop
	1949x1101
		->	General_Desktop
	271x438
		->	General_Mobile
	360x466
		->	General_Mobile
	518x389
		->	General_Desktop
	480x295
		->	General_Mobile
	720x1224
		->	General_Mobile
	401x3735
		->	General_Mobile
	533x320
		->	General_Desktop
	480x721
		->	General_Mobile
	1280x720
		->	General_Mobile
	986x495
		->	General_Mobile
	983x1561
		->	General_Mobile
	721x1280
		->	General_Mobile
	1025x408
		->	General_Mobile
	320x544
		->	General_Mobile
	320x542
		->	General_Mobile
	450x2260
		->	General_Mobile
	1000x442
		->	General_Mobile
	1503x2464.5
		->	General_Desktop
	480x508
		->	General_Mobile
	1043x586
		->	General_Desktop
	320x337
		->	General_Mobile
	640x360
	DEVICE_NAME
		Nokia 603
			->	General_Desktop
		HTC PN071
			->	General_Mobile
		SAMSUNG SM-G7102
			->	General_Mobile
		SAMSUNG SHV-E300K/KKUEML1
			->	General_Mobile
		JY-G3
			->	General_Mobile
		Nokia C6-00
			->	General_Desktop
	1280x806
		->	General_Mobile
	800x600
	DEVICE_NAME
		AN8CG3
			->	General_Mobile
		LG KU5400
			->	General_Desktop
		BlackBerry 8700
			->	General_Mobile
		Samsung S3600
			->	General_Desktop
		Nokia 2600c
			->	General_Desktop
		Ericsson P1i
			->	General_Desktop
		Nokia 7500
			->	General_Desktop
		Nokia 2760
			->	General_Desktop
	320x240
	DEVICE_NAME
		Q-Smart model S6
			->	General_Mobile
		Nokia 302
			->	General_Desktop
	184x246
		->	General_Mobile
	485x648
		->	General_Mobile
	360x640
	DEVICE_NAME
		C6903
			->	General_Mobile
		HTC
			->	General_Mobile
		PG86100
			->	General_Mobile
		HTC One X
			->	General_Mobile
		N9500
			->	General_Mobile
		AVEO X6
			->	General_Mobile
		SAMSUNG SHV-E300K/KKUENA2
			->	General_Mobile
		HTC Butterfly
			->	General_Mobile
		Find 5
			->	General_Mobile
		Q-Smart S53
			->	General_Mobile
		SAMSUNG SGH-M919V
			->	General_Mobile
		I7100
			->	General_Mobile
		HTC X515e
			->	General_Mobile
		i9220
			->	General_Mobile
		Nokia C7-00
			->	General_Desktop
		CGC-L3
			->	General_Mobile
	320x157
		->	General_Desktop
	986x656
		->	General_Mobile
```
