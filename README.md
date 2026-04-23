# 🚀 Phase 1: ROS2 Setup & Basic Node Development (WSL2)

---

## 🎯 Objective

Set up a development environment using WSL2 with Ubuntu and install ROS2 to understand core ROS2 concepts like nodes, topics, publishers, subscribers, and services.

---

## 🏗️ What Was Implemented

- Installed Ubuntu on WSL2
- Installed ROS2 (Humble)
- Created a ROS2 workspace
- Built and ran basic Publisher & Subscriber nodes
- Implemented Service and Client nodes
- Verified communication using ROS2 topics and services

### 🔹 Python Packages Created

- `my_topics_nodes` → All the Topic nodes are saved into this package
- `my_services_nodes` → All the Services nodes are saved into this package

### 🔹 Nodes Created

- `my_talker` → Publisher (publishes messages)
- `my_listener` → Subscriber (receives messages)
- `adder_gen` → Publisher (publishes random numbers)
- `adder_sum` → Subscriber (receives number and adds it to the previous sum of numbers )
- `add_two_ints_server` → Provides service
- `add_two_ints_client` → Calls service 

### 🔹 Topics Used

- `/topic` , `/number` , `/sum` → Used for Publisher-Subscriber communication

### 🔹 Services Used

- `/add_two_ints` (example service)

```bash
# Call service manually
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 2, b: 3}"
```

---

## ⚙️ Environment Setup

- OS: Ubuntu 22.04 (WSL2)
- ROS2 Version: Humble
- Shell: Bash

### Key Setup Steps

```bash
# Source ROS2
source /opt/ros/humble/setup.bash

# Create workspace
mkdir -p ~/phase1_practice_ws/src
cd ~/phase1_practice_ws

# Build workspace
colcon build

# Source workspace
source install/setup.bash
```

---

## 🧪 Basic ROS2 Commands Used

```bash
ros2 node list
ros2 topic list
ros2 topic echo /topic
ros2 service list
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 1, b: 2}"
ros2 run <package_name> <node_name>
```

---

## 🚧 Challenges Faced & Solutions

### 🔴 Issue 1: ROS2 commands not recognized after restarting terminal

**Problem:** `ros2: command not found`

**Root Cause:** ROS2 environment not sourced automatically

**Solution:** Added to `.bashrc`:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

### 🔴 Issue 2: Workspace packages not detected

**Problem:** Custom nodes not visible using `ros2 run`

**Root Cause:** Workspace not sourced after build

**Solution:**

```bash
source install/setup.bash
```

---

### 🔴 Issue 3: colcon build not working

**Problem:** `colcon: command not found`

**Solution:**

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
```

---

### 🔴 Issue 4: Python package not found (ModuleNotFoundError)

**Problem:** While running node: `ModuleNotFoundError`

**Root Cause:** Dependencies not installed

**Solution:**

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install rclpy std_msgs vision_msgs
```

---

### 🔴 Issue 5: Permission issues in WSL workspace

**Problem:** Permission denied while building or editing files

**Solution:**

```bash
sudo chown -R $USER:$USER ~/ros2_ws
```

---

### 🔴 Issue 6: ROS2 nodes not communicating

**Problem:** Publisher and Subscriber not exchanging messages

**Root Cause:** Topic mismatch or node not running

**Debug Steps:**

```bash
ros2 topic list
ros2 node list
ros2 topic echo /topic_name
```

**Solution:**

- Ensured topic names match
- Verified both nodes are running

---

### 🔴 Issue 7: WSL performance / slowness

**Problem:** Slow build times and lag

**Solution:**

- Avoided working in `/mnt/c/`
- Used Linux file system (`~/phase1_practice_ws`)

---

### 🔴 Issue 8: GUI tools not working (rqt / rviz)

**Problem:** GUI applications not opening

**Root Cause:** WSL needs GUI support

**Solution:**

- Used WSLg (Windows 11) OR
- Installed X Server (VcXsrv)

---

## 📊 Learnings

- Understood ROS2 architecture (Nodes, Topics, Services)
- Learned workspace creation and build process using colcon
- Gained experience debugging environment issues in WSL
- Learned importance of sourcing environments correctly
- Improved debugging using ROS2 CLI tools

---

## 🔮 Future Improvements

- Move from WSL to native hardware (Jetson Orin Nano)
- Build more complex multi-node systems
- Integrate sensors and real-time data

---

## 📂 Folder Structure

```
phase1_practice_ws/
├── src/
│   └── my_topics_nodes
|   └── my_services_nodes
├── build/
├── install/
└── log/
```

---

## 📌 References

- ROS2 Official Documentation
- WSL Documentation

---

## 💡 Key Takeaway

This phase was focused not just on setup, but on understanding how ROS2 works internally and learning how to debug environment and communication issues effectively.

---

