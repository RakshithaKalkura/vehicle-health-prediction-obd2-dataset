# Vehicle Engine Health Preditcion
Used 6 models - ANN, CNN, LSTM, Transformer-based, GNN and GRU. Each model was evaluated on 10 metrics - (Accuracy, Precision, Recall (Sensitivity), F1-Score, AUC-ROC, Log Loss (Cross-Entropy Loss), Cohen’s Kappa, Confusion Matrix, Mean Squared Error (MSE)) and the results were compared.

### Dataset Features summary 
#### 1. TIMESTAMP
- timestamp for the request
- Valid : 47.5k, 79%
- Mismatched - 0, 0%
- Missing - 12.9k, 21%
- Mean - 1503b
- Std. Deviation - .57b
- Quantiles
1500b
Min
1503b
25%
1504b
50%
1504b
75%
1505b
Max
#### 2. MARK
-vehicle' mark

chevrolet
23%
[null]
21%
Other (33842)
56%
Valid
47.5k
79%
Mismatched
0
0%
Missing
13.0k
21%
Unique
10
Most Common
chevrolet
23%
MODEL
vehicle' model

agile
23%
[null]
21%
Other (33842)
56%
Valid
47.5k
79%
Mismatched
0
0%
Missing
13.0k
21%
Unique
13
Most Common
agile
23%
CAR_YEAR
vehicle' year

Label	Count
2003.00 - 2003.65	507
2004.95 - 2005.60	903
2005.60 - 2006.25	6,184
2008.85 - 2009.50	7,485
2009.50 - 2010.15	145
2010.80 - 2011.45	13,617
2011.45 - 2012.10	8,494
2012.75 - 2013.40	2,240
2014.70 - 2015.35	6,018
2015.35 - 2016.00	1,866
2003
2016
Valid
47.5k
79%
Mismatched
0
0%
Missing
13.0k
21%
Mean
2.01k
Std. Deviation
2.93
Quantiles
2003
Min
2009
25%
2011
50%
2012
75%
2016
Max
ENGINE_POWER
Engine nominal power of the vehicle

Label	Count
1.00 - 1.85	5,581
13.75 - 14.60	16,580
15.45 - 16.30	17,813
17.15 - 18.00	7,485
1
18
Valid
47.5k
79%
Mismatched
0
0%
Missing
13.0k
21%
Mean
13.9
Std. Deviation
4.89
Quantiles
1
Min
14
25%
16
50%
16
75%
18
Max
AUTOMATIC
[null]
Boolean	Count
true	0
false	0
[null]	12,980
true

00%

false

00%

[null]

13.0k21%

Valid
0
0%
Mismatched
47.5k
79%
Missing
13.0k
21%
True
0
0%
False
0
0%
VEHICLE_ID
id from vehicle

car1
23%
[null]
21%
Other (33897)
56%
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Unique
14
Most Common
car1
23%
BAROMETRIC_PRESSURE(KPA)
self-explained

Label	Count
89.00 - 89.60	145
89.60 - 90.20	273
90.80 - 91.40	488
92.60 - 93.20	175
93.80 - 94.40	834
95.00 - 95.60	1,147
95.60 - 96.20	3,597
96.80 - 97.40	670
98.60 - 99.20	140
99.80 - 100.40	2,243
100.40 - 101.00	500
89
101
Valid
10.2k
17%
Mismatched
0
0%
Missing
50.2k
83%
Mean
96.4
Std. Deviation
2.87
Quantiles
89
Min
95
25%
96
50%
100
75%
101
Max
ENGINE_COOLANT_TEMP
Main Cooler Temperature

Label	Count
22.00 - 26.15	18
26.15 - 30.30	41
30.30 - 34.45	53
34.45 - 38.60	81
38.60 - 42.75	121
42.75 - 46.90	158
46.90 - 51.05	354
51.05 - 55.20	521
55.20 - 59.35	534
59.35 - 63.50	609
63.50 - 67.65	645
67.65 - 71.80	889
71.80 - 75.95	2,384
75.95 - 80.10	5,994
80.10 - 84.25	4,399
84.25 - 88.40	9,535
88.40 - 92.55	3,590
92.55 - 96.70	2,915
96.70 - 100.85	997
100.85 - 105.00	126
22
105
Valid
34.0k
56%
Mismatched
0
0%
Missing
26.5k
44%
Mean
81.8
Std. Deviation
10.9
Quantiles
22
Min
78
25%
85
50%
88
75%
105
Max
FUEL_LEVEL
Level of vehicle fuel at the moment of request.

[null]
95%
6,30%
0%
Other (2842)
5%
Valid
2994
5%
Mismatched
0
0%
Missing
57.4k
95%
Unique
195
Most Common
6,30%
0%
ENGINE_LOAD
[null]
49%
41%
6%
Other (27123)
45%
Valid
31.0k
51%
Mismatched
0
0%
Missing
29.5k
49%
Unique
244
Most Common
41%
6%
AMBIENT_AIR_TEMP
Label	Count
12.00 - 14.60	60
14.60 - 17.20	201
17.20 - 19.80	1
22.40 - 25.00	60
25.00 - 27.60	1,522
27.60 - 30.20	1,192
30.20 - 32.80	394
32.80 - 35.40	57
35.40 - 38.00	132
12
38
Valid
3619
6%
Mismatched
0
0%
Missing
56.8k
94%
Mean
27.6
Std. Deviation
4.29
Quantiles
12
Min
27
25%
27
50%
30
75%
38
Max
ENGINE_RPM
Label	Count
438.00 - 606.90	49
606.90 - 775.80	3,110
775.80 - 944.70	5,966
944.70 - 1113.60	2,405
1113.60 - 1282.50	2,341
1282.50 - 1451.40	2,509
1451.40 - 1620.30	2,810
1620.30 - 1789.20	3,071
1789.20 - 1958.10	3,159
1958.10 - 2127.00	2,547
2127.00 - 2295.90	1,947
2295.90 - 2464.80	1,444
2464.80 - 2633.70	952
2633.70 - 2802.60	624
2802.60 - 2971.50	454
2971.50 - 3140.40	259
3140.40 - 3309.30	129
3309.30 - 3478.20	52
3478.20 - 3647.10	27
3647.10 - 3816.00	4
438
3816
Valid
33.9k
56%
Mismatched
0
0%
Missing
26.6k
44%
Mean
1.52k
Std. Deviation
614
Quantiles
438
Min
906
25%
1487
50%
1957
75%
3816
Max
INTAKE_MANIFOLD_PRESSURE
Label	Count
13.00 - 17.40	98
17.40 - 21.80	941
21.80 - 26.20	1,535
26.20 - 30.60	2,748
30.60 - 35.00	2,932
35.00 - 39.40	2,396
39.40 - 43.80	2,154
43.80 - 48.20	2,539
48.20 - 52.60	1,784
52.60 - 57.00	1,201
57.00 - 61.40	1,440
61.40 - 65.80	830
65.80 - 70.20	905
70.20 - 74.60	606
74.60 - 79.00	614
79.00 - 83.40	441
83.40 - 87.80	352
87.80 - 92.20	317
92.20 - 96.60	320
96.60 - 101.00	936
13
101
Valid
25.1k
42%
Mismatched
0
0%
Missing
35.4k
58%
Mean
47.4
Std. Deviation
20.2
Quantiles
13
Min
32
25%
43
50%
58
75%
101
Max
MAF
Label	Count
2.00 - 262.25	2,771
262.25 - 522.50	2,947
522.50 - 782.75	1,086
782.75 - 1043.00	788
1043.00 - 1303.25	670
1303.25 - 1563.50	705
1563.50 - 1823.75	638
1823.75 - 2084.00	539
2084.00 - 2344.25	410
2344.25 - 2604.50	347
2604.50 - 2864.75	269
2864.75 - 3125.00	207
3125.00 - 3385.25	152
3385.25 - 3645.50	107
3645.50 - 3905.75	75
3905.75 - 4166.00	59
4166.00 - 4426.25	35
4426.25 - 4686.50	17
4686.50 - 4946.75	1
4946.75 - 5207.00	5
2
5.21k
Valid
11.8k
20%
Mismatched
0
0%
Missing
48.6k
80%
Mean
986
Std. Deviation
942
Quantiles
2
Min
267
25%
554
50%
1.53k
75%
5.21k
Max
LONG TERM FUEL TRIM BANK 2
[null]
78%
-100%
21%
Other (635)
1%
Valid
13.1k
22%
Mismatched
0
0%
Missing
47.4k
78%
Unique
21
Most Common
-100%
21%
FUEL_TYPE
[null]
67%
Biodiesel_Ethanol
33%
Other (138)
0%
Valid
20.0k
33%
Mismatched
0
0%
Missing
40.4k
67%
Unique
2
Most Common
Biodiesel_Ethanol
33%
AIR_INTAKE_TEMP
Label	Count
23.00 - 25.85	149
25.85 - 28.70	980
28.70 - 31.55	2,691
31.55 - 34.40	4,253
34.40 - 37.25	5,665
37.25 - 40.10	4,008
40.10 - 42.95	2,506
42.95 - 45.80	4,139
45.80 - 48.65	2,983
48.65 - 51.50	2,208
51.50 - 54.35	1,958
54.35 - 57.20	1,601
57.20 - 60.05	740
60.05 - 62.90	168
62.90 - 65.75	123
65.75 - 68.60	90
68.60 - 71.45	29
71.45 - 74.30	6
74.30 - 77.15	9
77.15 - 80.00	46
23
80
Valid
34.4k
57%
Mismatched
0
0%
Missing
26.1k
43%
Mean
41.2
Std. Deviation
8.52
Quantiles
23
Min
35
25%
40
50%
47
75%
80
Max
FUEL_PRESSURE
[null]
100%
48
0%
Valid
138
0%
Mismatched
0
0%
Missing
60.3k
100%
Unique
1
Most Common
48
0%
SPEED
Label	Count
0.00 - 7.15	21,149
7.15 - 14.30	2,224
14.30 - 21.45	2,494
21.45 - 28.60	3,013
28.60 - 35.75	2,913
35.75 - 42.90	3,142
42.90 - 50.05	2,802
50.05 - 57.20	2,010
57.20 - 64.35	1,443
64.35 - 71.50	1,238
71.50 - 78.65	1,062
78.65 - 85.80	804
85.80 - 92.95	643
92.95 - 100.10	598
100.10 - 107.25	357
107.25 - 114.40	305
114.40 - 121.55	155
121.55 - 128.70	102
128.70 - 135.85	54
135.85 - 143.00	21
0
143
Valid
46.5k
77%
Mismatched
0
0%
Missing
13.9k
23%
Mean
24.7
Std. Deviation
29.3
Quantiles
0
Min
0
25%
14
50%
42
75%
143
Max
SHORT TERM FUEL TRIM BANK 2
[null]
78%
-100%
21%
Other (636)
1%
Valid
13.1k
22%
Mismatched
0
0%
Missing
47.4k
78%
Unique
23
Most Common
-100%
21%
SHORT TERM FUEL TRIM BANK 1
[null]
38%
-100%
21%
Other (24871)
41%
Valid
37.6k
62%
Mismatched
0
0%
Missing
22.8k
38%
Unique
190
Most Common
-100%
21%
ENGINE_RUNTIME
DateTime	Count
10/04/2019 - 10/04/2019	1,925
10/04/2019 - 10/04/2019	2,268
10/04/2019 - 10/04/2019	1,780
10/04/2019 - 10/04/2019	1,233
10/04/2019 - 10/04/2019	865
10/04/2019 - 10/04/2019	576
10/04/2019 - 10/04/2019	558
10/04/2019 - 10/04/2019	499
10/04/2019 - 10/04/2019	413
10/04/2019 - 10/04/2019	344
10/04/2019 - 10/04/2019	297
10/04/2019 - 10/04/2019	307
10/04/2019 - 10/04/2019	231
10/04/2019 - 10/04/2019	176
10/04/2019 - 10/04/2019	129
10/04/2019 - 10/04/2019	66
10/04/2019 - 10/04/2019	66
10/04/2019 - 10/04/2019	67
10/04/2019 - 10/04/2019	67
10/04/2019 - 10/04/2019	35
2019-10-04
2019-10-04
Valid
11.9k
20%
Mismatched
0
0%
Missing
48.5k
80%
Minimum
4Oct19
Mean
4Oct19
Maximum
4Oct19
THROTTLE_POS
[null]
44%
13%
6%
Other (30142)
50%
Valid
33.9k
56%
Mismatched
0
0%
Missing
26.6k
44%
Unique
81
Most Common
13%
6%
DTC_NUMBER
MIL is OFF0 codes
68%
[null]
22%
Other (6078)
10%
Valid
47.1k
78%
Mismatched
0
0%
Missing
13.3k
22%
Unique
7
Most Common
MIL is OFF0 codes
68%
TROUBLE_CODES
[null]
80%
P0133
10%
Other (5855)
10%
Valid
11.9k
20%
Mismatched
0
0%
Missing
48.5k
80%
Unique
13
Most Common
P0133
10%
TIMING_ADVANCE
[null]
43%
49,8%
1%
Other (33279)
55%
Valid
34.2k
57%
Mismatched
0
0%
Missing
26.3k
43%
Unique
218
Most Common
49,8%
1%
EQUIV_RATIO
[null]
80%
1,0%
20%
Valid
11.9k
20%
Mismatched
0
0%
Missing
48.5k
80%
Unique
1
Most Common
1,0%
20%
MIN
Label	Count
0.00 - 2.65	4,875
5.30 - 7.95	3,212
10.60 - 13.25	8,486
18.55 - 21.20	5,170
23.85 - 26.50	4,888
31.80 - 34.45	3,820
39.75 - 42.40	7,707
45.05 - 47.70	5,012
50.35 - 53.00	4,342
0
53
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Mean
26.4
Std. Deviation
16.6
Quantiles
0
Min
13
25%
26
50%
40
75%
53
Max
HOURS
Label	Count
0.00 - 1.15	4,365
1.15 - 2.30	920
2.30 - 3.45	1,520
3.45 - 4.60	273
4.60 - 5.75	303
5.75 - 6.90	140
6.90 - 8.05	585
8.05 - 9.20	785
9.20 - 10.35	2,869
10.35 - 11.50	7,523
11.50 - 12.65	3,160
12.65 - 13.80	1,714
13.80 - 14.95	1,330
14.95 - 16.10	4,610
16.10 - 17.25	1,054
17.25 - 18.40	2,599
18.40 - 19.55	3,516
19.55 - 20.70	3,169
20.70 - 21.85	1,825
21.85 - 23.00	5,252
0
23
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Mean
13.4
Std. Deviation
6.55
Quantiles
0
Min
11
25%
13
50%
19
75%
23
Max
DAYS_OF_WEEK
Label	Count
0.00 - 0.30	9,830
0.90 - 1.20	5,051
1.80 - 2.10	5,913
3.00 - 3.30	5,835
3.90 - 4.20	11,705
4.80 - 5.10	5,538
5.70 - 6.00	3,640
0
6
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Mean
2.75
Std. Deviation
1.94
Quantiles
0
Min
1
25%
3
50%
4
75%
6
Max
MONTHS
Label	Count
7.00 - 7.10	10,758
8.00 - 8.10	25,646
8.90 - 9.00	11,108
7
9
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Mean
8.01
Std. Deviation
0.68
Quantiles
7
Min
8
25%
8
50%
8
75%
9
Max
YEAR
Label	Count
2017.00 - 2017.00	47,512
2017
2017
Valid
47.5k
79%
Mismatched
0
0%
Missing
12.9k
21%
Mean
2.02k
Std. Deviation
0
Quantiles
2017
Min
2017
25%
2017
50%
2017
75%
2017
Max
