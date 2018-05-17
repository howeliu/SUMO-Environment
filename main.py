#!/usr/bin/env python
# -*- coding:utf8 -*-

from __future__ import print_function
import sys

sys.path.append("/usr/share/sumo/tools")   # 将SUMO安装路径下的tools文件夹添加到环境变量中，否则无法使用SUMO自带的traci包
import traci                               # 导入SUMO自带的traci包

sumoBinary = "/usr/bin/sumo-gui"           # 无需图形界面时，可以将sumo-gui改为sumo
sumoConfig = "data/demo.sumocfg"

def main():
    sumoCmd = [sumoBinary, "-c", sumoConfig]
    traci.start(sumoCmd)                               # 开始仿真
    simulationSteps = 0
    Phaseflag = 0
    while simulationSteps < 1000:                      # 仿真1000个步长
        traci.simulationStep()                         # 执行一步仿真

        # 获取仿真环境中当前仿真步的实时信息
        print('红绿灯路口西侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('W'))
        print('红绿灯路口西侧排队长度:', traci.lanearea.getJamLengthMeters('W'))
        print('红绿灯路口东侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('E'))
        print('红绿灯路口东侧排队长度:', traci.lanearea.getJamLengthMeters('E'))
        print('红绿灯路口北侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('N'))
        print('红绿灯路口北侧排队长度:', traci.lanearea.getJamLengthMeters('N'))
        print('红绿灯路口南侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('S'))
        print('红绿灯路口南侧排队长度:', traci.lanearea.getJamLengthMeters('S'))

        # 红绿灯控制程序
        # 所控红绿灯的相位顺序为：东西直行南北禁行（30秒），南北直行东西禁行（30秒）
        if simulationSteps % 30 == 0:
            if Phaseflag % 2 == 0:
                traci.trafficlight.setPhase('3', 0)   # 改变红绿灯的相位为东西直行南北禁行
            else:
                traci.trafficlight.setPhase('3', 1)   # 改变红绿灯的相位为南北直行东西禁行
            Phaseflag += 1
        simulationSteps += 1
    traci.close()                                     # 结束仿真

if __name__ == '__main__':
    main()
