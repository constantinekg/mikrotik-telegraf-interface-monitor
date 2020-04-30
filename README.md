# mikrotik-telegraf-interface-monitor


Details you can see here: https://infdots.blogspot.com/2020/04/mikrotik-mikrotik-api-telegraf-grafana.html (russian language)

## telegraf config:

```
[[inputs.exec]]
command = "/opt/scripts/mikrotik-telegraf-interface-monitor/mikrotik-int-stat-getter.py"
timeout = "5s"
data_format = "influx"
```

