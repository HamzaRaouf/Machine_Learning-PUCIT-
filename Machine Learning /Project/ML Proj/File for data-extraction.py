import numpy as np 
ts_msAcc = np.load("/Users/siblingsmac/Desktop/bbh/Training/trainMSAccelerometer.npy")
ts_msGyr = np.load("/Users/siblingsmac/Desktop/bbh/Training/trainMSGyroscope.npy")
ts_labels = np.load("/Users/siblingsmac/Desktop/bbh/Training/trainLabels.npy")

READ = 20
THROW_OUT = 36

ts_labels_READ_idx = ts_labels == READ
ts_labels_THROW_OUT_idx = ts_labels == THROW_OUT

ts_msAcc_READ = ts_msAcc[ts_labels_READ_idx]
ts_msGyr_READ = ts_msGyr[ts_labels_READ_idx]

ts_msAcc_THROW_OUT = ts_msAcc[ts_labels_THROW_OUT_idx]
ts_msGyr_THROW_OUT = ts_msGyr[ts_labels_THROW_OUT_idx]

ts_labels_READ = ts_labels[ts_labels_READ_idx]
ts_labels_THROW_OUT = ts_labels[ts_labels_THROW_OUT_idx]

ts_msAcc_Two_Activities = np.concatenate((ts_msAcc_READ, ts_msAcc_THROW_OUT))
ts_msGyr_Two_Activities = np.concatenate((ts_msGyr_READ, ts_msGyr_THROW_OUT))
ts_labels_Two_Activities = np.concatenate((ts_labels_READ, ts_labels_THROW_OUT))

np.save("train_MSAccelerometer_READ_THROW_OUT.npy", ts_msAcc_Two_Activities)
np.save("train_MSGyroscope_READ_THROW_OUT.npy", ts_msGyr_Two_Activities)
np.save("train_labels_READ_THROW_OUT.npy", ts_labels_Two_Activities)
