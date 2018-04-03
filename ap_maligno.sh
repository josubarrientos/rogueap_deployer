#!/bin/bash

MONITOR_DEVICE=wlan1
OUTPUT_DEVICE=wlan0

# Catch ctrl c so we can exit cleanly
trap ctrl_c INT
function ctrl_c(){
    echo Killing processes..
    killall dnsmasq
    killall hostapd
}

ifconfig $MONITOR_DEVICE 10.0.0.1/24 up
dnsmasq -C dnsmasq.conf -H fakehosts.conf
sysctl -w net.ipv4.ip_forward=1
iptables -P FORWARD ACCEPT
iptables --table nat -A POSTROUTING -o $OUTPUT_DEVICE -j MASQUERADE
hostapd ./hostapd.conf -B
tshark -i $MONITOR_DEVICE  -w output.pcap -P
