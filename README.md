# SUMO-Environment

一个单路口交通信号灯控制的SUMO环境demo

## 安装说明

### 使用命令行安装最新版SUMO

添加官网最新版本的源

`sudo add-apt-repository ppa:sumo/stable`

更新软件列表

`sudo apt-get update`

安装

`sudo apt-get install sumo sumo-tools sumo-doc`

## main.py脚本运行说明

运行脚本后，会自动弹出SUMO的GUI界面。

弹出界面后，先修改界面右上方工具栏中的Delay为非零数，否则仿真会瞬间完成，看不到仿真过程，数值越大，仿真过程越慢，可以先设置为100。

然后点击左上方绿色的开始箭头即可开始仿真，鼠标滚轮可以缩放仿真界面，按住鼠标左键可以拖动仿真界面。

## 仿真数据获取说明

```
print('红绿灯路口西侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('W'))
print('红绿灯路口西侧排队长度:', traci.lanearea.getJamLengthMeters('W'))
print('红绿灯路口东侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('E'))
print('红绿灯路口东侧排队长度:', traci.lanearea.getJamLengthMeters('E'))
print('红绿灯路口北侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('E'))
print('红绿灯路口北侧排队长度:', traci.lanearea.getJamLengthMeters('E'))
print('红绿灯路口南侧排队车辆数目:', traci.lanearea.getJamLengthVehicle('E'))
print('红绿灯路口南侧排队长度:', traci.lanearea.getJamLengthMeters('E'))
```

## 交通信号灯控制说明

```
traci.trafficlight.setPhase('3', 0)   # 改变红绿灯的相位为东西直行南北禁行
traci.trafficlight.setPhase('3', 1)   # 改变红绿灯的相位为南北直行东西禁行
```
