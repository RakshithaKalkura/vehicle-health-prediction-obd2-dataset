# Vehicle Engine Health Preditcion
Used 6 models - ANN, CNN, LSTM, Transformer-based, GNN and GRU. Each model was evaluated on 10 metrics - (Accuracy, Precision, Recall (Sensitivity), F1-Score, AUC-ROC, Log Loss (Cross-Entropy Loss), Cohen’s Kappa, Confusion Matrix, Mean Squared Error (MSE)) and the results were compared.

# Dataset Features Summary

## 1. TIMESTAMP
- **Description:** Timestamp for the request
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 1503b
- **Std. Deviation:** 0.57b
- **Quantiles:**
  - **Min:** 1500b
  - **25%:** 1503b
  - **50%:** 1504b
  - **75%:** 1504b
  - **Max:** 1505b

## 2. MARK
- **Description:** Vehicle's mark
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.0k (21%)
- **Unique:** 10
- **Most Common:** chevrolet (23%)

## 3. MODEL
- **Description:** Vehicle's model
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.0k (21%)
- **Unique:** 13
- **Most Common:** agile (23%)

## 4. CAR_YEAR
- **Description:** Vehicle's year
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.0k (21%)
- **Mean:** 2.01k
- **Std. Deviation:** 2.93
- **Quantiles:**
  - **Min:** 2003
  - **25%:** 2009
  - **50%:** 2011
  - **75%:** 2012
  - **Max:** 2016

## 5. ENGINE_POWER
- **Description:** Engine nominal power of the vehicle
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.0k (21%)
- **Mean:** 13.9
- **Std. Deviation:** 4.89
- **Quantiles:**
  - **Min:** 1
  - **25%:** 14
  - **50%:** 16
  - **75%:** 16
  - **Max:** 18

## 6. AUTOMATIC
- **Description:** Indicates whether the vehicle is automatic (Boolean)
- **Valid:** 0 (0%)
- **Mismatched:** 47.5k (79%)
- **Missing:** 13.0k (21%)
- **True Count:** 0 (0%)
- **False Count:** 0 (0%)

## 7. VEHICLE_ID
- **Description:** ID from the vehicle
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Unique:** 14
- **Most Common:** car1 (23%)

## 8. BAROMETRIC_PRESSURE(KPA)
- **Description:** Barometric pressure (self-explanatory)
- **Valid:** 10.2k (17%)
- **Mismatched:** 0 (0%)
- **Missing:** 50.2k (83%)
- **Mean:** 96.4
- **Std. Deviation:** 2.87
- **Quantiles:**
  - **Min:** 89
  - **25%:** 95
  - **50%:** 96
  - **75%:** 100
  - **Max:** 101

## 9. ENGINE_COOLANT_TEMP
- **Description:** Main cooler temperature
- **Valid:** 34.0k (56%)
- **Mismatched:** 0 (0%)
- **Missing:** 26.5k (44%)
- **Mean:** 81.8
- **Std. Deviation:** 10.9
- **Quantiles:**
  - **Min:** 22
  - **25%:** 78
  - **50%:** 85
  - **75%:** 88
  - **Max:** 105

## 10. FUEL_LEVEL
- **Description:** Level of vehicle fuel at the moment of request
- **Valid:** 2,994 (5%)
- **Mismatched:** 0 (0%)
- **Missing:** 57.4k (95%)
- **Unique:** 195
- **Most Common:** 6,30%

## 11. ENGINE_LOAD
- **Description:** Engine load
- **Valid:** 31.0k (51%)
- **Mismatched:** 0 (0%)
- **Missing:** 29.5k (49%)
- **Unique:** 244
- **Most Common:** 41% (6%)

## 12. AMBIENT_AIR_TEMP
- **Description:** Ambient air temperature
- **Valid:** 3,619 (6%)
- **Mismatched:** 0 (0%)
- **Missing:** 56.8k (94%)
- **Mean:** 27.6
- **Std. Deviation:** 4.29
- **Quantiles:**
  - **Min:** 12
  - **25%:** 27
  - **50%:** 27
  - **75%:** 30
  - **Max:** 38

## 13. ENGINE_RPM
- **Description:** Engine revolutions per minute
- **Valid:** 33.9k (56%)
- **Mismatched:** 0 (0%)
- **Missing:** 26.6k (44%)
- **Mean:** 1.52k
- **Std. Deviation:** 614
- **Quantiles:**
  - **Min:** 438
  - **25%:** 906
  - **50%:** 1487
  - **75%:** 1957
  - **Max:** 3816

## 14. INTAKE_MANIFOLD_PRESSURE
- **Description:** Intake manifold pressure
- **Valid:** 25.1k (42%)
- **Mismatched:** 0 (0%)
- **Missing:** 35.4k (58%)
- **Mean:** 47.4
- **Std. Deviation:** 20.2
- **Quantiles:**
  - **Min:** 13
  - **25%:** 32
  - **50%:** 43
  - **75%:** 58
  - **Max:** 101

## 15. MAF
- **Description:** Mass Air Flow sensor reading
- **Valid:** 11.8k (20%)
- **Mismatched:** 0 (0%)
- **Missing:** 48.6k (80%)
- **Mean:** 986
- **Std. Deviation:** 942
- **Quantiles:**
  - **Min:** 2
  - **25%:** 267
  - **50%:** 554
  - **75%:** 1.53k
  - **Max:** 5.21k

## 16. LONG TERM FUEL TRIM BANK 2
- **Description:** Long term fuel trim for bank 2
- **Valid:** 13.1k (22%)
- **Mismatched:** 0 (0%)
- **Missing:** 47.4k (78%)
- **Unique:** 21
- **Most Common:** -100% (21%)

## 17. FUEL_TYPE
- **Description:** Fuel type of the vehicle
- **Valid:** 20.0k (33%)
- **Mismatched:** 0 (0%)
- **Missing:** 40.4k (67%)
- **Unique:** 2
- **Most Common:** Biodiesel_Ethanol (33%)

## 18. AIR_INTAKE_TEMP
- **Description:** Air intake temperature
- **Valid:** 34.4k (57%)
- **Mismatched:** 0 (0%)
- **Missing:** 26.1k (43%)
- **Mean:** 41.2
- **Std. Deviation:** 8.52
- **Quantiles:**
  - **Min:** 23
  - **25%:** 35
  - **50%:** 40
  - **75%:** 47
  - **Max:** 80

## 19. FUEL_PRESSURE
- **Description:** Fuel pressure
- **Valid:** 138 (0%)
- **Mismatched:** 0 (0%)
- **Missing:** 60.3k (100%)
- **Unique:** 1
- **Most Common:** 48 (0%)

## 20. SPEED
- **Description:** Vehicle speed
- **Valid:** 46.5k (77%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.9k (23%)
- **Mean:** 24.7
- **Std. Deviation:** 29.3
- **Quantiles:**
  - **Min:** 0
  - **25%:** 0
  - **50%:** 14
  - **75%:** 42
  - **Max:** 143

## 21. SHORT TERM FUEL TRIM BANK 2
- **Description:** Short term fuel trim for bank 2
- **Valid:** 13.1k (22%)
- **Mismatched:** 0 (0%)
- **Missing:** 47.4k (78%)
- **Unique:** 23
- **Most Common:** -100% (21%)

## 22. SHORT TERM FUEL TRIM BANK 1
- **Description:** Short term fuel trim for bank 1
- **Valid:** 37.6k (62%)
- **Mismatched:** 0 (0%)
- **Missing:** 22.8k (38%)
- **Unique:** 190
- **Most Common:** -100% (21%)

## 23. ENGINE_RUNTIME
- **Description:** Engine runtime
- **Valid:** 11.9k (20%)
- **Mismatched:** 0 (0%)
- **Missing:** 48.5k (80%)
- **Minimum:** 4Oct19
- **Mean:** 4Oct19
- **Maximum:** 4Oct19

## 24. THROTTLE_POS
- **Description:** Throttle position
- **Valid:** 33.9k (56%)
- **Mismatched:** 0 (0%)
- **Missing:** 26.6k (44%)
- **Unique:** 81
- **Most Common:** 13% (6%)

## 25. DTC_NUMBER
- **Description:** MIL is OFF0 codes (diagnostic trouble code numbers)
- **Valid:** 47.1k (78%)
- **Mismatched:** 0 (0%)
- **Missing:** 13.3k (22%)
- **Unique:** 7
- **Most Common:** MIL is OFF0 codes (68%)

## 26. TROUBLE_CODES
- **Description:** Diagnostic trouble codes
- **Valid:** 11.9k (20%)
- **Mismatched:** 0 (0%)
- **Missing:** 48.5k (80%)
- **Unique:** 13
- **Most Common:** P0133 (10%)

## 27. TIMING_ADVANCE
- **Description:** Timing advance
- **Valid:** 34.2k (57%)
- **Mismatched:** 0 (0%)
- **Missing:** 26.3k (43%)
- **Unique:** 218
- **Most Common:** 49.8% (1%)

## 28. EQUIV_RATIO
- **Description:** Equivalence ratio
- **Valid:** 11.9k (20%)
- **Mismatched:** 0 (0%)
- **Missing:** 48.5k (80%)
- **Unique:** 1
- **Most Common:** 1.0% (20%)

## 29. MIN
- **Description:** MIN value (minutes)
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 26.4
- **Std. Deviation:** 16.6
- **Quantiles:**
  - **Min:** 0
  - **25%:** 13
  - **50%:** 26
  - **75%:** 40
  - **Max:** 53

## 30. HOURS
- **Description:** Hours (e.g., engine hours)
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 13.4
- **Std. Deviation:** 6.55
- **Quantiles:**
  - **Min:** 0
  - **25%:** 11
  - **50%:** 13
  - **75%:** 19
  - **Max:** 23

## 31. DAYS_OF_WEEK
- **Description:** Day of the week of the request
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 2.75
- **Std. Deviation:** 1.94
- **Quantiles:**
  - **Min:** 0
  - **25%:** 1
  - **50%:** 3
  - **75%:** 4
  - **Max:** 6

## 32. MONTHS
- **Description:** Month of the request
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 8.01
- **Std. Deviation:** 0.68
- **Quantiles:**
  - **Min:** 7
  - **25%:** 8
  - **50%:** 8
  - **75%:** 8
  - **Max:** 9

## 33. YEAR
- **Description:** Year of the request
- **Valid:** 47.5k (79%)
- **Mismatched:** 0 (0%)
- **Missing:** 12.9k (21%)
- **Mean:** 2.02k
- **Std. Deviation:** 0
- **Quantiles:**
  - **Min:** 2017
  - **25%:** 2017
  - **50%:** 2017
  - **75%:** 2017
  - **Max:** 2017
