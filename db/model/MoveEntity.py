from unit.Json import getOr


class MoveEntity:
    airSpeed = 0.0
    airPressure = 0.0,
    airWayAngleFromNorth = 0.0
    height = 0.0
    datetime = 0
    xAccel = 0.0
    yAccel = 0.0
    zAccel = 0.0
    xGyro = 0.0
    yGyro = 0.0
    zGyro = 0.0
    motorPower = 0.0
    isGps = False
    xCoordinate = 0.0
    yCoordinate = 0.0
    angleFromNorth = 0.0,
    stabilizerAngle = 0.0,
    rightEleronAngle = 0.0,
    leftEleronAngle = 0.0

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
                 airSpeed,
                 airPressure,
                 airWayAngleFromNorth,
                 height,
                 datetime,
                 xAccel,
                 yAccel,
                 zAccel,
                 xGyro,
                 yGyro,
                 zGyro,
                 motorPower,
                 isGps,
                 xCoordinate,
                 yCoordinate,
                 angleFromNorth,
                 stabilizerAngle,
                 rightEleronAngle,
                 leftEleronAngle
                 ):
        self.angleFromNorth = angleFromNorth
        self.yCoordinate = yCoordinate
        self.xCoordinate = xCoordinate
        self.isGps = isGps
        self.motorPower = motorPower
        self.zGyro = zGyro
        self.yGyro = yGyro
        self.xGyro = xGyro
        self.yAccel = yAccel
        self.xAccel = xAccel
        self.datetime = datetime
        self.height = height
        self.airWayAngleFromNorth = airWayAngleFromNorth
        self.airPressure = airPressure
        self.zAccel = zAccel
        self.airSpeed = airSpeed
        self.stabilizerAngle = stabilizerAngle
        self.rightEleronAngle = rightEleronAngle
        self.leftEleronAngle = leftEleronAngle


#-method add -i_stabilizerAngle 0.0 -i_leftEleronAngle 0.0 -i_rightEleronAngle 0.0 -i_isGps true  -i_airSpeed 0.0  -i_airPressure 0.0  -i_airWayAngleFromNorth 0.0  -i_height 0.0  -i_datetime 0  -i_xAccel 0.0  -i_yAccel 0.0  -i_zAccel 0.0  -i_xGyro 0.0  -i_yGyro 0.0  -i_zGyro 0.0  -i_motorPower 0.0  -i_xCoordinate 0.0  -i_yCoordinate 0.0  -i_angleFromNorth 0.0
    @classmethod
    def createFromArgs(cls, args):
        argsdict = vars(args)
        return MoveEntity(
            airSpeed=argsdict[initiationMoveArgsNameSpace("airSpeed")],
            airPressure=argsdict[initiationMoveArgsNameSpace("airPressure")],
            airWayAngleFromNorth=argsdict[initiationMoveArgsNameSpace("airWayAngleFromNorth")],
            height=argsdict[initiationMoveArgsNameSpace("height")],
            datetime=argsdict[initiationMoveArgsNameSpace("datetime")],
            xAccel=argsdict[initiationMoveArgsNameSpace("xAccel")],
            yAccel=argsdict[initiationMoveArgsNameSpace("yAccel")],
            zAccel=argsdict[initiationMoveArgsNameSpace("zAccel")],
            xGyro=argsdict[initiationMoveArgsNameSpace("xGyro")],
            yGyro=argsdict[initiationMoveArgsNameSpace("yGyro")],
            zGyro=argsdict[initiationMoveArgsNameSpace("zGyro")],
            motorPower=argsdict[initiationMoveArgsNameSpace("motorPower")],
            isGps=argsdict[initiationMoveArgsNameSpace("isGps")],
            xCoordinate=argsdict[initiationMoveArgsNameSpace("xCoordinate")],
            yCoordinate=argsdict[initiationMoveArgsNameSpace("yCoordinate")],
            angleFromNorth=argsdict[initiationMoveArgsNameSpace("angleFromNorth")],
            stabilizerAngle=argsdict[initiationMoveArgsNameSpace("stabilizerAngle")],
            rightEleronAngle=argsdict[initiationMoveArgsNameSpace("rightEleronAngle")],
            leftEleronAngle=argsdict[initiationMoveArgsNameSpace("leftEleronAngle")]
        )

    @classmethod
    def createFromJson(cls, json):
        return MoveEntity(
            airSpeed=getOr(json, 'airSpeed', 0.),
            airPressure=getOr(json, 'airPressure', 0.),
            airWayAngleFromNorth=getOr(json, 'airWayAngleFromNorth', 0.),
            height=getOr(json, 'height', 0.),
            datetime=getOr(json, 'datetime', 0),
            xAccel=getOr(json, 'xAccel', 0.),
            yAccel=getOr(json, 'yAccel', 0.),
            zAccel=getOr(json, 'zAccel', 0.),
            xGyro=getOr(json, 'xGyro', 0.),
            yGyro=getOr(json, 'yGyro', 0.),
            zGyro=getOr(json, 'zGyro', 0.),
            motorPower=getOr(json, 'motorPower', 0.),
            isGps=getOr(json, 'isGps', False),
            xCoordinate=getOr(json, 'xCoordinate', 0.),
            yCoordinate=getOr(json, 'motorPower', 0.),
            angleFromNorth=getOr(json, 'angleFromNorth', 0.),
            stabilizerAngle=getOr(json, 'stabilizerAngle', 0.),
            rightEleronAngle=getOr(json, 'rightEleronAngle', 0.),
            leftEleronAngle=getOr(json, 'leftEleronAngle', 0.)
        )

    def toJson(self):
        return {
            'airSpeed': self.airSpeed,
            'airPressure': self.airPressure,
            'airWayAngleFromNorth': self.airWayAngleFromNorth,
            'height': self.height,
            'datetime': self.datetime,
            'xAccel': self.xAccel,
            'yAccel': self.yAccel,
            'zAccel': self.zAccel,
            'xGyro': self.xGyro,
            'yGyro': self.yGyro,
            'zGyro': self.zGyro,
            'motorPower': self.motorPower,
            'isGps': self.isGps,
            'xCoordinate': self.xCoordinate,
            'yCoordinate': self.yCoordinate,
            'angleFromNorth': self.angleFromNorth,
            'stabilizerAngle': self.stabilizerAngle,
            'rightEleronAngle': self.rightEleronAngle,
            'leftEleronAngle': self.leftEleronAngle
        }

    def toMLData(self):
        return (self.airSpeed,
                self.airPressure,
                self.airWayAngleFromNorth,
                self.height,
                self.xAccel,
                self.yAccel,
                self.zAccel,
                self.xGyro,
                self.yGyro,
                self.zGyro,
                self.motorPower,
                self.angleFromNorth,
                self.stabilizerAngle,
                self.rightEleronAngle,
                self.leftEleronAngle)


argsParams = [
    ("airSpeed", float),
    ("airPressure", float),
    ("airWayAngleFromNorth", float),
    ("height", float),
    ("datetime", int),
    ("xAccel", float),
    ("yAccel", float),
    ("zAccel", float),
    ("xGyro", float),
    ("yGyro", float),
    ("zGyro", float),
    ("motorPower", float),
    ("isGps", bool),
    ("xCoordinate", float),
    ("yCoordinate", float),
    ("angleFromNorth", float),
    ("stabilizerAngle", float),
    ("leftEleronAngle", float),
    ("rightEleronAngle", float)
]


def initiationMoveArgsNameSpace(name):
    return "i_{0}".format(name)


def initiationMoveArgsNameSpaceParam(name):
    return "-{0}".format(initiationMoveArgsNameSpace(name))
