# analysePwList

This script will go through a wordlist and analyse the pattern for each listet password.
You can choose between hashcat output pattern or crunch output pattern.
Default unicode is set to utf-8
You can give a easy list of words or a worlist in [username]:[password] pattern. Both options in a list are also possible.

[Hashcat format]:
```
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

[Crunch format (depending on your charset)]:
```
@  = abcdefghijklmnopqrstuvwxyz
,  = ABCDEFGHIJKLMNOPQRSTUVWXYZ
%  = 0123456789
^  = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

[Pattern options]
- hashcat
- crunch

for a more sortet output use this line of command:
python analysePwList.py -w [wordlist] -e [unicode] -p [pattern] | sort | uniq -c
