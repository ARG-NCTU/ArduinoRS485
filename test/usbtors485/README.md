# Python usb to rs485 serial test

![](figs/usbtors485.jpg)


# How to Run

## Gazebo setup
* open sender

```
Laptop $ python serial_test.py

```
![](figs/send.png)

* open receiver
```
Laptop $ python aserial_test.py
```
![](figs/receive.png)
* Localization using gps and imu (change veh for different robot)
```
Laptop $ source ipc_join.sh
Docker $ source environment.sh
Docker $ roslaunch localization localization_gps_imu_wamv.launch veh:=wamv num:=2 (default is for 4 wamvs.)
```

## Designated goal points and visualize robot radius and goal points on rviz
* localization/src/multi_goalpoint.py(multi_goalpoint1.py)
    * designated goal points and visualization
* launch goal points for each robot in a launch file

```
Laptop $ source ipc_join.sh
Docker $ source environment.sh
Docker $ roslaunch localization multi_goal.launch veh:=wamv
```

## Run HRVO algorithm

```
Laptop $ source ipc_join.sh
Docker $ source environment.sh

Docker $ roslaunch hrvo multi_wamv_hrvo.launch(2 robot)
Docker $ roslaunch hrvo multi_4_wamv_hrvo.launch(4 robot)
```

## Rviz visualization

```
Laptop $ source ipc_join.sh
Docker $ cd ~/robotx-2022
Docker $ source environment.sh
Docker $ rviz -d rviz/multi_wamv.rviz
```
