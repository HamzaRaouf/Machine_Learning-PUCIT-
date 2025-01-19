import numpy as np 
ts_msAcc = np.load("testMSAccelerometer.npy")
ts_msGyr = np.load("testMSGyroscope.npy")
ts_labels = np.load("testLabels.npy")

# OPEN_DOOR = 20
# RUB_HANDS = 36


WEAR_JACKET = 53
CLOSE_DOOR = 4 


# ts_labels_OPEN_DOOR_idx = ts_labels == OPEN_DOOR
# ts_labels_RUB_HANDS_idx = ts_labels == RUB_HANDS

ts_labels_WEAR_JACKET_idx = ts_labels == WEAR_JACKET
ts_labels_CLOSE_DOOR_idx = ts_labels == CLOSE_DOOR

ts_msAcc_WEAR_JACKET = ts_msAcc[ts_labels_WEAR_JACKET_idx]
ts_msGyr_WEAR_JACKET = ts_msGyr[ts_labels_WEAR_JACKET_idx]

ts_msAcc_CLOSE_DOOR = ts_msAcc[ts_labels_CLOSE_DOOR_idx]
ts_msGyr_CLOSE_DOOR = ts_msGyr[ts_labels_CLOSE_DOOR_idx]

ts_labels_WEAR_JACKET = ts_labels[ts_labels_WEAR_JACKET_idx]
ts_labels_CLOSE_DOOR = ts_labels[ts_labels_CLOSE_DOOR_idx]

ts_msAcc_Two_Activities = np.concatenate((ts_msAcc_WEAR_JACKET, ts_msAcc_CLOSE_DOOR))
ts_msGyr_Two_Activities = np.concatenate((ts_msGyr_WEAR_JACKET, ts_msGyr_CLOSE_DOOR))
ts_labels_Two_Activities = np.concatenate((ts_labels_WEAR_JACKET, ts_labels_CLOSE_DOOR))

np.save("test_MSAccelerometer_WearJacket_CloseDoor.npy", ts_msAcc_Two_Activities)
np.save("test_MSGyroscope_WearJacket_CloseDoor.npy", ts_msGyr_Two_Activities)
np.save("test_labels_WearJacket_CloseDoor.npy", ts_labels_Two_Activities)
