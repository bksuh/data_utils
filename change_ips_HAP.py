# Wrote by bksuh @https://github.com/bksuh
import json
import argparse

def update_json_fields(path, t_ip, l_ip):
    with open(path, 'r') as f:
        data = json.load(f)

    target_ip_host = t_ip
    lidar_ip = l_ip
    data["HAP"]["host_net_info"]["cmd_data_ip"] = target_ip_host
    data["HAP"]["host_net_info"]["push_msg_ip"] = target_ip_host
    data["HAP"]["host_net_info"]["point_data_ip"] = target_ip_host
    data["HAP"]["host_net_info"]["imu_data_ip"] = target_ip_host

    data["lidar_configs"][0]["ip"] = lidar_ip

    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Use argparse for argument parsing
    
    # Path to the JSON file
    json_path = "/root/ros2_ws/src/install/livox_ros_driver2/share/livox_ros_driver2/config/HAP_config.json"
    
    parser = argparse.ArgumentParser(description="Update IP addresses in a JSON configuration file.")
    parser.add_argument("--j_path", required=True, default=json_path, help="JSON Path")
    parser.add_argument("--t_ip", required=True, default ="192.168.1.5", help="Target IP address")
    parser.add_argument("--l_ip", required=True, default ="192.168.1.100", help="Lidar IP address")
    args = parser.parse_args()

    # Update JSON fields
    update_json_fields(args.j_path, args.t_ip, args.l_ip)
    print(f"Updated JSON file at {args.j_path} with t_ip={args.t_ip} and l_ip={args.l_ip}")
