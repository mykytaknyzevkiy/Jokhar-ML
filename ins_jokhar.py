import argparse
from multiprocessing import freeze_support
from db.model.MoveEntity import MoveEntity, argsParams, initiationMoveArgsNameSpaceParam
from db.dao import MoveHistoryDao as _moveHistoryDao
from ml import MoveHistoryML as _moveHistoryML

parser = argparse.ArgumentParser(description="Hello, i am jokhar ml for ins")


def addInitiationMoveArgs():
    for d in argsParams:
        parser.add_argument(
            initiationMoveArgsNameSpaceParam(d[0]),
            type=d[1]
        )


def addEndMoveArgs():
    for d in argsParams:
        parser.add_argument(
            "-e_{0}".format(d[0]),
            type=d[1]
        )


addInitiationMoveArgs()
addEndMoveArgs()

parser.add_argument(
    "-method",
    type=str
)

args = parser.parse_args()

if args.method == "add":
    _moveHistoryDao.insert(MoveEntity(
        airSpeed=0.0,
        airPressure=0.0,
        airWayAngleFromNorth=0.,
        height=0.,
        datetime=0.,
        xAccel=0.,
        yAccel=0.,
        zAccel=0.,
        xGyro=0.,
        yGyro=0.,
        zGyro=0.,
        motorPower=0.,
        isGps=True,
        xCoordinate=0.,
        yCoordinate=0.,
        angleFromNorth=0.,
        stabilizerAngle=0.,
        rightEleronAngle=0.,
        leftEleronAngle=0.,
    ))

    freeze_support()

    _moveHistoryML.runTrain()

    print("stabiliztion on")
    print(_moveHistoryML.findEleronsAngleForStabilize(0., 0., 0., 0.))
