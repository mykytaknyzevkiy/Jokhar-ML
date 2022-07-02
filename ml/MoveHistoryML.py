import tensorflow as tf
import numpy as np
from tensorflow import keras
from db.dao import MoveHistoryDao as _moveHistoryDao
from db.model.MoveEntity import MoveEntity
from unit.ListUnit import grouped
import math
import os
import threading

_checkpoint_train_dir_path = "training_1"
_checkpoint_distance_path = _checkpoint_train_dir_path + "/move_history_find_distance.ckpt"
_checkpoint_stabilizer_path = _checkpoint_train_dir_path + "/move_history_stabilizer.ckpt"

_modelFindDistance = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[2, 15])])
_modelStabilizer = tf.keras.Sequential([keras.layers.Dense(units=2, input_shape=[7])])


def runTrain():
    threading.Thread(target=_trainFindDistance).start()

    threading.Thread(target=_trainStabilizer).start()


def _trainFindDistance():
    _moveHistoryList = _moveHistoryDao.listGps()

    _pairedList = list(grouped(_moveHistoryList, 2))

    if len(_pairedList) == 0:
        return

    def mapMoveHistoryPairToMLData(data: [MoveEntity, MoveEntity]):
        return [data[0].toMLData(), data[1].toMLData()]

    def mapMoveHistoryPairToMLResultData(data: [MoveEntity, MoveEntity]):
        # √((x2 - x1)2 + (y2-y1)2)
        return math.sqrt(
            math.pow((data[1].xCoordinate - data[0].xCoordinate), 2) +
            math.pow((data[1].yCoordinate - data[0].yCoordinate), 2)
        )

    xs = list(map(mapMoveHistoryPairToMLData, _pairedList))
    ys = list(map(mapMoveHistoryPairToMLResultData, _pairedList))

    if os.path.exists(_checkpoint_distance_path):
        _modelFindDistance.load_weights(_checkpoint_distance_path)

    _modelFindDistance.compile(optimizer='sgd', loss='mean_squared_error')

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=_checkpoint_distance_path,
                                                     save_weights_only=True,
                                                     verbose=1)

    _modelFindDistance.fit(xs, ys, epochs=500, callbacks=[cp_callback])


def _trainStabilizer():
    _moveHistoryList = _moveHistoryDao.listGps()

    if len(_moveHistoryList) == 0:
        return

    def mapMoveHistoryToMLData(data: MoveEntity):
        return (data.xAccel,
                data.yAccel,
                data.zAccel,
                data.airSpeed,
                data.airPressure,
                data.airWayAngleFromNorth,
                data.angleFromNorth)

    def mapMoveHistoryToMLResult(data: MoveEntity):
        return (data.leftEleronAngle,
                data.rightEleronAngle)

    xs = list(map(mapMoveHistoryToMLData, _moveHistoryList))
    ys = list(map(mapMoveHistoryToMLResult, _moveHistoryList))

    if os.path.exists(_checkpoint_stabilizer_path):
        _modelFindDistance.load_weights(_checkpoint_stabilizer_path)

    _modelStabilizer.compile(optimizer='sgd', loss='mean_squared_error')

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=_checkpoint_stabilizer_path,
                                                     save_weights_only=True,
                                                     verbose=1)

    _modelStabilizer.fit(xs, ys, epochs=500, callbacks=[cp_callback])


def findDistance(start: MoveEntity, end: MoveEntity):
    if not os.path.exists(_checkpoint_train_dir_path):
        return 0.0

    _modelFindDistance.load_weights(_checkpoint_distance_path)

    result = _modelFindDistance.predict([
        [start.toMLData(), end.toMLData()]
    ])

    return np.take(result, 0)


def findEleronsAngleForStabilize(airSpeed: float,
                                 airPressure: float,
                                 airWayAngleFromNorth: float,
                                 angleFromNorth: float):
    if not os.path.exists(_checkpoint_train_dir_path):
        return 0, 0

    _modelStabilizer.load_weights(_checkpoint_stabilizer_path)

    # (data.xAccel,
    # data.yAccel,
    #  data.zAccel,
    #  data.airSpeed,
    #  data.airPressure,
    #  data.airWayAngleFromNorth,
    #  data.angleFromNorth)

    result = _modelStabilizer.predict([
        (0.0, 0.0, 0.0, airSpeed, airPressure, airWayAngleFromNorth, angleFromNorth)
    ])

    return np.take(result, 0), np.take(result, 1)
