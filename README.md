## Power Relay control daemon

`powerrelayd` is a Pyro frontend for controlling an [Arduino-controlled power relay](https://github.com/rockit-astro/dehumidifier-switch).

A separate control script is not needed; use [powerd](https://github.com/rockit-astro/powerd) to control the relay.

### Configuration

Configuration is read from json files that are installed by default to `/etc/powerrelayd`.
A configuration file is specified when launching the power relay server.

```python
{
  "daemon": "localhost_test", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "powerd", # The name to use when writing messages to the observatory log.
  "control_machines": ["LocalHost"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
}
```

### Initial Installation

The automated packaging scripts will push 2 RPM packages to the observatory package repository:

| Package                  | Description                                               |
|--------------------------|-----------------------------------------------------------|
| rockit-powerrelay-server | Contains the `powerd` server and systemd service file.    |
| rockit-powerrelay-sting  | Contains the json configuration and udev rules for STING. |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now powerrelayd@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the power relay config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart powerrelayd@<config>
```

### Testing Locally

The power server and client can be run directly from a git clone:
```
./powerrelayd test.json
```
